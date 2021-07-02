# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Dockerfile for installing the necessary dependencies for building Hadoop.
# See BUILDING.txt.

FROM centos:7

WORKDIR /root

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN yum install -y epel-release \
    && yum update -y \
    && yum install -y centos-release-scl \
    && yum install -y devtoolset-9 \
    && yum -y group install "Development Tools" \
    && yum install -y \
    ant \
    build-essential \
    bzip2 \
    bzip2-devel \
    clang \
    curl \
    cyrus-sasl-devel \
    doxygen \
    fuse \
    fuse-libs \
    fuse-devel \
    git \
    libcurl-devel \
    libtirpc-devel \
    libpmem-devel \
    libtool \
    lz4-devel \
    make \
    openssl-devel \
    pinentry-curses \
    python3 \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    rsync \
    snappy-devel \
    sudo \
    valgrind \
    zlib-devel \
    lzo-devel \
    gcc \
    rpmdevtools \
    patch \
    diffutils \
    coreutils \
    rpmlint \
    rpm-devel 

# Set GCC 9 as the default C/C++ compiler
RUN echo "source /opt/rh/devtoolset-9/enable" >> /etc/bashrc
SHELL ["/bin/bash", "--login", "-c"]

####
# Install Maven 3.6.3
####
RUN mkdir -p /opt/maven /tmp/maven \
    && curl -k -L -s -S https://mirrors.estointernet.in/apache/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz \
        -o /tmp/maven/apache-maven-3.6.3-bin.tar.gz \
    && tar xzf /tmp/maven/apache-maven-3.6.3-bin.tar.gz --strip-components 1 -C /opt/maven \
    && ln -s /opt/maven/bin/mvn /usr/bin/mvn

####
# Install CMake 3.19
####
# hadolint ignore=DL3003
RUN mkdir -p /tmp/cmake /opt/cmake \
    && curl -k -L -s -S https://cmake.org/files/v3.19/cmake-3.19.0.tar.gz -o /tmp/cmake/cmake-3.19.0.tar.gz \
    && tar xzf /tmp/cmake/cmake-3.19.0.tar.gz --strip-components 1 -C /opt/cmake \
    && cd /opt/cmake || exit && ./bootstrap \
    && make "-j$(nproc)" \
    && make install \
    && cd /root || exit

####
# Install zstandard
####
# hadolint ignore=DL3003
RUN mkdir -p /opt/zstd /tmp/zstd \
    && curl -k -L -s -S https://github.com/facebook/zstd/archive/refs/tags/v1.4.9.tar.gz -o /tmp/zstd/v1.4.9.tar.gz \
    && tar xzf /tmp/zstd/v1.4.9.tar.gz --strip-components 1 -C /opt/zstd \
    && cd /opt/zstd || exit \
    && make "-j$(nproc)" \
    && make install \
    && cd /root || exit

#RUN localectl set-locale LANG=en_US.UTF-8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'
ENV PYTHONIOENCODING=utf-8

######
# Set env vars required to build Hadoop
######
ENV MAVEN_HOME /opt/maven
ENV PATH "${PATH}:${MAVEN_HOME}/bin"
# JAVA_HOME must be set in Maven >= 3.5.0 (MNG-6003)
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0

#######
# Install SpotBugs 4.2.2
#######
RUN mkdir -p /opt/spotbugs \
    && curl -k -L -s -S https://github.com/spotbugs/spotbugs/releases/download/4.2.2/spotbugs-4.2.2.tgz \
      -o /opt/spotbugs.tgz \
    && tar xzf /opt/spotbugs.tgz --strip-components 1 -C /opt/spotbugs \
    && chmod +x /opt/spotbugs/bin/*
ENV SPOTBUGS_HOME /opt/spotbugs

#######
# Install Boost 1.72 (1.71 ships with Focal)
#######
# hadolint ignore=DL3003
RUN mkdir -p /opt/boost-library \
    && curl -k -L https://sourceforge.net/projects/boost/files/boost/1.72.0/boost_1_72_0.tar.bz2/download > boost_1_72_0.tar.bz2 \
    && mv boost_1_72_0.tar.bz2 /opt/boost-library \
    && cd /opt/boost-library \
    && tar --bzip2 -xf boost_1_72_0.tar.bz2 \
    && cd /opt/boost-library/boost_1_72_0 \
    && ./bootstrap.sh --prefix=/usr/ \
    && ./b2 --without-python install \
    && cd /root \
    && rm -rf /opt/boost-library

######
# Install Google Protobuf 3.7.1 (3.6.1 ships with Focal)
######
# hadolint ignore=DL3003
RUN mkdir -p /opt/protobuf-src \
    && curl -k -L -s -S \
      https://github.com/protocolbuffers/protobuf/releases/download/v2.5.0/protobuf-2.5.0.tar.gz \
      -o /opt/protobuf.tar.gz \
    && tar xzf /opt/protobuf.tar.gz --strip-components 1 -C /opt/protobuf-src \
    && cd /opt/protobuf-src \
    && ./configure --prefix=/opt/protobuf \
    && make "-j$(nproc)" \
    && make install \
    && cd /root \
    && rm -rf /opt/protobuf-src \
    && ln -s /opt/protobuf/bin/protoc /usr/bin/protoc

ENV PROTOBUF_HOME /opt/protobuf
ENV PATH "${PATH}:/opt/protobuf/bin"

####
# Install Node.js
####
# hadolint ignore=DL3003
RUN mkdir -p /tmp/node \
    && curl -k -L -s -S https://nodejs.org/dist/v14.16.1/node-v14.16.1.tar.gz -o /tmp/node-v14.16.1.tar.gz \
    && tar xzf /tmp/node-v14.16.1.tar.gz --strip-components 1 -C /tmp/node \
    && cd /tmp/node || exit \
    && ./configure \
    && make "-j$(nproc)" \
    && make install \
    && cd /root || exit

####
# Install pylint and python-dateutil
####
RUN pip3 install pylint==2.6.0 python-dateutil==2.8.1

####
# Install bower
####
# hadolint ignore=DL3008
RUN npm install -g bower@1.8.8

####grant sudo access to 'builder'
RUN echo 'builder ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

####set python3 default
RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
RUN sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2

####create "builder" user and use it for rpm BuildRequires
RUN useradd -m -s /bin/bash -c "CI user for building RPM" builder \
    && mkdir -p /home/builder/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS} \
    && chown -R builder. /home/builder
USER builder
WORKDIR /home/builder/rpmbuild
