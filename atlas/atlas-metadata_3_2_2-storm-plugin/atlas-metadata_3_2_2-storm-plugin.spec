%global prefix /usr/ldf/prod/3.2.2
%global version 2.1.0.3.2.2

Name:    atlas-metadata_3_2_2-storm-plugin
Version:    2.1.0.3.2.2
Release:  1
Summary:  Atlas plugin for storm

License: ASL 2.0
URL:   https://github.com/LigaData/apache
Group:    System/Daemons
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
Requires:    rpmlib(CompressedFileNames) <= 3.0.4-1
Requires:    rpmlib(FileDigests) <= 4.6.0-1
Requires:    rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires:    rpmlib(PayloadIsXz) <= 5.2-1
Provides:    atlas-metadata_3_1_5_0_152-storm-plugin = 2.0.0.3.1.5.0-152
Provides:    osgi(com.fasterxml.jackson.core.jackson-annotations) = 2.10.0
Provides:    osgi(com.fasterxml.jackson.core.jackson-core) = 2.10.0
Provides:    osgi(com.fasterxml.jackson.core.jackson-databind) = 2.10.0
Provides:    osgi(com.fasterxml.woodstox.woodstox-core) = 5.0.3
Provides:    osgi(com.sun.jersey.json) = 1.19.0
Provides:    osgi(com.thoughtworks.paranamer) = 2.7.0
Provides:    osgi(javax.ws.rs.jsr311-api) = 1.1
Provides:    osgi(log4j) = 1.2.17
Provides:    osgi(org.apache.commons.collections) = 3.2.2
Provides:    osgi(org.apache.commons.configuration) = 1.10.0
Provides:    osgi(org.apache.commons.configuration) = 2.2.0
Provides:    osgi(org.apache.commons.logging) = 1.1.3
Provides:    osgi(org.codehaus.jettison.jettison) = 1.3.7
Provides:    osgi(stax2-api) = 3.1.4

%description 
Atlas Storm plugin component runs with storm.
%prep
%build
%install
rm -rf %{buildroot}
#DIRS
for i in $(cat /home/builder/tmp/atlas-metadata_3_2_2-storm-plugin/DIRS_FROM_SAMPLE); do mkdir -p %{buildroot}%{prefix}${i} 2>/dev/null; done
#Symlinks
cd %{buildroot}
#FILES
cd %{buildroot}%{prefix}
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jackson-core-2.9.9.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jackson-annotations-2.9.9.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/storm/atlas-storm-plugin-impl/commons-configuration2-2.2.jar ./atlas/hook/storm/atlas-storm-plugin-impl/commons-configuration2-2.2.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/storm/atlas-storm-plugin-impl/aopalliance-1.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl/aopalliance-1.0.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/commons-configuration-1.10.jar ./atlas/hook/storm/atlas-storm-plugin-impl/commons-configuration-1.10.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/storm/atlas-storm-plugin-impl/stax2-api-3.1.4.jar ./atlas/hook/storm/atlas-storm-plugin-impl/stax2-api-3.1.4.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/storm/atlas-storm-plugin-impl/commons-logging-1.1.3.jar ./atlas/hook/storm/atlas-storm-plugin-impl/commons-logging-1.1.3.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/storm/atlas-storm-plugin-impl/log4j-1.2.17.jar ./atlas/hook/storm/atlas-storm-plugin-impl/log4j-1.2.17.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/storm/atlas-storm-plugin-impl/woodstox-core-5.0.3.jar ./atlas/hook/storm/atlas-storm-plugin-impl/woodstox-core-5.0.3.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jsr311-api-1.1.jar ./atlas/hook/storm/atlas-storm-plugin-impl/jsr311-api-1.1.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/storm/atlas-storm-plugin-impl/commons-collections-3.2.2.jar ./atlas/hook/storm/atlas-storm-plugin-impl/commons-collections-3.2.2.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/storm/atlas-storm-plugin-impl/paranamer-2.7.jar ./atlas/hook/storm/atlas-storm-plugin-impl/paranamer-2.7.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jersey-json-1.19.jar ./atlas/hook/storm/atlas-storm-plugin-impl/jersey-json-1.19.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jackson-databind-2.10.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl/jackson-databind-2.10.0.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/storm/atlas-storm-plugin-impl/javax.inject-1.jar ./atlas/hook/storm/atlas-storm-plugin-impl/javax.inject-1.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook/storm/atlas-storm-plugin-impl/jettison-1.3.7.jar ./atlas/hook/storm/atlas-storm-plugin-impl/jettison-1.3.7.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/plugin-classloader/target/atlas-plugin-classloader-2.1.0.jar ./atlas/hook/storm
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/addons/storm-bridge/target/dependency/hook/storm/storm-bridge-shim-2.1.0.jar ./atlas/hook/storm
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/hadoop-hdfs-client-3.1.1.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/notification/target/atlas-notification-2.1.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/addons/hive-bridge/target/hive-bridge-2.1.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/hadoop-auth-3.1.1.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/common/target/atlas-common-2.1.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/atlas-client-common-2.1.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/atlas-client-v2-2.1.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/intg/target/atlas-intg-2.1.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/atlas-client-v1-2.1.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/hbase-common-2.0.2.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/addons/storm-bridge/target/storm-bridge-2.1.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/addons/hdfs-model/target/hdfs-model-2.1.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/kafka-clients-2.0.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/hadoop-common-3.1.1.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/kafka_2.11-2.0.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/addons/storm-bridge/target/dependency/hook/storm/atlas-storm-plugin-impl/hive-exec-3.1.0.jar ./atlas/hook/storm/atlas-storm-plugin-impl

%clean
%files
%{prefix}/atlas
