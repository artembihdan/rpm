%global prefix /usr/ldf/prod/3.2.2
%global version 2.1.0.3.2.2

Name:    atlas-metadata_3_2_2-hbase-plugin
Version:    2.1.0.3.2.2
Release:  1
Summary:  Atlas plugin for hbase

License: ASL 2.0
URL:   https://github.com/LigaData/apache
Group:    System/Daemons
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
Requires:    /bin/bash
Requires:    rpmlib(CompressedFileNames) <= 3.0.4-1
Requires:    rpmlib(FileDigests) <= 4.6.0-1
Requires:    rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires:    rpmlib(PayloadIsXz) <= 5.2-1
Provides:    atlas-metadata_3_2_2-hbase-plugin = 2.1.0.3.2.2-1
Provides:    osgi(com.fasterxml.jackson.core.jackson-annotations) = 2.10.0
Provides:    osgi(com.fasterxml.jackson.core.jackson-core) = 2.10.0
Provides:    osgi(com.fasterxml.jackson.core.jackson-databind) = 2.10.0
Provides:    osgi(com.sun.jersey.contribs.jersey-multipart) = 1.19.0
Provides:    osgi(com.sun.jersey.json) = 1.19.0
Provides:    osgi(javax.ws.rs.jsr311-api) = 1.1
Provides:    osgi(org.apache.commons.configuration) = 1.10.0

%description 
Atlas Hbase plugin component runs with hbase.
%prep
%build
%install
rm -rf %{buildroot}
#DIRS
for i in $(cat /home/builder/tmp/atlas-metadata_3_2_2-hbase-plugin/DIRS_FROM_SAMPLE); do mkdir -p %{buildroot}%{prefix}${i} 2>/dev/null; done
#Symlinks
cd %{buildroot}
#FILES
cd %{buildroot}%{prefix}
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook-bin/import-hbase.sh ./atlas/hook-bin/import-hbase.sh
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook-bin/import-hive.sh ./atlas/hook-bin/import-hive.sh
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jackson-core-2.9.9.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jackson-annotations-2.9.9.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jackson-core-2.9.9.jar ./hbase/lib/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jackson-annotations-2.9.9.jar ./hbase/lib/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/commons-configuration-1.10.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl/commons-configuration-1.10.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jsr311-api-1.1.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl/jsr311-api-1.1.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jersey-multipart-1.19.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl/jersey-multipart-1.19.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jersey-json-1.19.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl/jersey-json-1.19.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jackson-databind-2.10.0.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl/jackson-databind-2.10.0.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/commons-configuration-1.10.jar ./hbase/lib/atlas-hbase-plugin-impl/commons-configuration-1.10.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jsr311-api-1.1.jar ./hbase/lib/atlas-hbase-plugin-impl/jsr311-api-1.1.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jersey-multipart-1.19.jar ./hbase/lib/atlas-hbase-plugin-impl/jersey-multipart-1.19.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jersey-json-1.19.jar ./hbase/lib/atlas-hbase-plugin-impl/jersey-json-1.19.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jackson-databind-2.10.0.jar ./hbase/lib/atlas-hbase-plugin-impl/jackson-databind-2.10.0.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/plugin-classloader/target/atlas-plugin-classloader-2.1.0.jar ./atlas/hook/hbase
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/notification/target/atlas-notification-2.1.0.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/hbase/atlas-hbase-plugin-impl/hbase-bridge-2.1.0.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/falcon/atlas-falcon-plugin-impl/atlas-common-2.1.0.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/client/common/target/atlas-client-common-2.1.0.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/atlas-client-v2-2.1.0.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/intg/target/atlas-intg-2.1.0.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/addons/hdfs-model/target/hdfs-model-2.1.0.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/kafka-clients-2.0.0.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/notification/target/dependency/hook/kafka-topic-setup/kafka_2.11-2.0.0.jar ./atlas/hook/hbase/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/addons/hbase-bridge-shim/target/hbase-bridge-shim-2.1.0.jar ./atlas/hook/hbase
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/plugin-classloader/target/atlas-plugin-classloader-2.1.0.jar ./hbase/lib
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/notification/target/atlas-notification-2.1.0.jar ./hbase/lib/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/hbase/atlas-hbase-plugin-impl/hbase-bridge-2.1.0.jar ./hbase/lib/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/common/target/atlas-common-2.1.0.jar ./hbase/lib/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/atlas-client-common-2.1.0.jar ./hbase/lib/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/atlas-client-v2-2.1.0.jar ./hbase/lib/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/intg/target/atlas-intg-2.1.0.jar ./hbase/lib/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/addons/hdfs-model/target/hdfs-model-2.1.0.jar ./hbase/lib/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/kafka-clients-2.0.0.jar ./hbase/lib/atlas-hbase-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/addons/hbase-bridge-shim/target/hbase-bridge-shim-2.1.0.jar ./hbase/lib
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/notification/target/dependency/hook/kafka-topic-setup/kafka_2.11-2.0.0.jar  ./hbase/lib/atlas-hbase-plugin-impl/

%clean
%files
%{prefix}/atlas
%{prefix}/hbase
