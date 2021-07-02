%global prefix /usr/ldf/prod/3.2.2
%global version 2.1.0.3.2.2

Name:    atlas-metadata_3_2_2-kafka-plugin
Version:    2.1.0.3.2.2
Release:  1
Summary:  Atlas plugin for kafka

License: ASL 2.0
URL:   https://github.com/LigaData/apache
Group:    System/Daemons
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
Requires:    /bin/bash
Requires:    rpmlib(CompressedFileNames) <= 3.0.4-1
Requires:    rpmlib(FileDigests) <= 4.6.0-1
Requires:    rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires:    rpmlib(PayloadIsXz) <= 5.2-1
Provides:    atlas-metadata_3_2_2-kafka-plugin = 2.1.0.3.2.2-1
Provides:    osgi(com.sun.jersey.contribs.jersey-multipart) = 1.19.0
Provides:    osgi(org.apache.commons.configuration) = 1.10.0

%description 
Atlas kafka plugin component runs with kafka.
%prep
%build
%install
rm -rf %{buildroot}
#DIRS
for i in $(cat /home/builder/tmp/atlas-metadata_3_2_2-kafka-plugin/DIRS_FROM_SAMPLE); do mkdir -p %{buildroot}%{prefix}${i} 2>/dev/null; done
#Symlinks
cd %{buildroot}
#FILES
cd %{buildroot}%{prefix}
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/hook-bin/import-kafka.sh ./atlas/hook-bin/import-kafka.sh
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/commons-configuration-1.10.jar ./atlas/hook/kafka/atlas-kafka-plugin-impl/commons-configuration-1.10.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-hive-hook/apache-atlas-hive-hook-2.1.0/hook/hive/atlas-hive-plugin-impl/jersey-multipart-1.19.jar ./atlas/hook/kafka/atlas-kafka-plugin-impl/jersey-multipart-1.19.jar
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/common/target/atlas-common-2.1.0.jar ./atlas/hook/kafka/atlas-kafka-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/atlas-client-common-2.1.0.jar ./atlas/hook/kafka/atlas-kafka-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/atlas-client-v2-2.1.0.jar ./atlas/hook/kafka/atlas-kafka-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/intg/target/atlas-intg-2.1.0.jar ./atlas/hook/kafka/atlas-kafka-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/atlas-client-v1-2.1.0.jar ./atlas/hook/kafka/atlas-kafka-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/addons/kafka-bridge/target/kafka-bridge-2.1.0.jar ./atlas/hook/kafka/atlas-kafka-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/webapp/target/atlas-webapp-2.1.0/WEB-INF/lib/kafka-clients-2.0.0.jar ./atlas/hook/kafka/atlas-kafka-plugin-impl
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/addons/hive-bridge/target/dependency/hook/hive/atlas-hive-plugin-impl/kafka_2.11-2.0.0.jar ./atlas/hook/kafka/atlas-kafka-plugin-impl

%clean
%files
%{prefix}/atlas
