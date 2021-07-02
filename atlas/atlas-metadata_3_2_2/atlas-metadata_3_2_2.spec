%global prefix /usr/ldf/prod/3.2.2
%global version 2.1.0.3.2.2

Name:    atlas-metadata_3_2_2
Version:    2.1.0.3.2.2
Release:  1
Summary:  Atlas is an application framework which allows for a complex directed-acyclic-graph of tasks for processing data and is built atop Apache Hadoop YARN.

License: ASL 2.0
URL:   https://github.com/LigaData/apache
Group:    Development/Libraries
Source1: security.html
Source2: ClassificationPropagation.html
Source3: Downloads.html
Source4: Hook-Falcon.html
Source5: WhatsNew-1.0.html
Source6: TypeSystem.html
Source7: Bridge-Kafka.html
Source8: Hook-Storm.html
Source9: Import-API.html
Source10: apache-maven-fluido-1.7.min.css
Source11: WhatsNew-2.0.html
Source12: Hook-Hive.html
Source13: SoftReference.html
Source14: InstallationSteps.html
Source15: Configuration.html
Source16: HighAvailability.html
Source17: atlas-logo.png
Source18: Notifications.html
Source19: AtlasRepairIndex.html
Source20: QuickStart.html
Source21: Search-Basic.html
Source22: Atlas-Authentication.html
Source23: EclipseSetup.html
Source24: Import-Export-API.html
Source25: Incremental-Export.html
Source26: Hook-HBase.html
Source27: Hook-Sqoop.html
Source28: Import-API-Options.html
Source29: ReplicatedToFromAttributes.html
Source30: AtlasServer.html
Source31: Export-HDFS-API.html
Source32: ExportImportAudits.html
Source33: apache-maven-fluido-1.7.min.js
Source34: Search-Advanced.html
Source35: ImportEntityTransforms.html
Source36: Glossary.html
Source37: Atlas-Authorization-Simple-Authorizer.html
Source38: Atlas-Authorization-Model.html
Source39: Migration-0.8-to-1.0.html
Source40: Atlas-Authorization-Ranger-Authorizer.html
Source41: Export-API.html
Source42: Architecture.html
Source43: atlas_migration_export.pyo
Source44: atlas_migration_export.pyc
Source45: atlas-migration-exporter-0.8.0.2.6.5.2000-3.jar

BuildRoot:      %{_tmppath}/%{name}-%{version}-root
Requires:    /bin/bash
Requires:    /bin/sh
Requires:    /usr/bin/env
Requires:    hadoop_3_2_2
Requires:    hadoop_3_2_2-hdfs
Requires:    hadoop_3_2_2-mapreduce
Requires:    hadoop_3_2_2-yarn
Requires:    ranger_3_2_2-atlas-plugin
Requires:    rpmlib(CompressedFileNames) <= 3.0.4-1
Requires:    rpmlib(FileDigests) <= 4.6.0-1
Requires:    rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires:    sh-utils
Requires:    rpmlib(PayloadIsXz) <= 5.2-1
Provides:    atlas-metadata_3_2_2 = 2.1.0.3.2.2-1

%description 
Atlas is an application framework which allows for a complex
directed-acyclic-graph of tasks for processing data
and is built atop Apache Hadoop YARN.
%prep
%build
%install
rm -rf %{buildroot}
#DIRS
for i in $(cat /home/builder/tmp/atlas-metadata_3_2_2/DIRS_FROM_SAMPLE); do mkdir -p %{buildroot}%{prefix}${i} 2>/dev/null; done
#Symlinks
cd %{buildroot}
ln -s /etc/atlas/conf /tmp/atlas-conf
mv /tmp/atlas-conf %{buildroot}%{prefix}/atlas/conf
#FILES
cd %{buildroot}%{prefix}
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/1065-avro_model.json ./atlas/models/1000-Hadoop/1065-avro_model.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/1030-hive_model.json ./atlas/models/1000-Hadoop/1030-hive_model.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/0000-Area0/0011-glossary_model.json ./atlas/models/0000-Area0/0011-glossary_model.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/0000-Area0/0010-base_model.json ./atlas/models/0000-Area0/0010-base_model.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/bin/atlas_stop.py ./atlas/bin/atlas_stop.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/bin/atlas_config.py ./atlas/bin/atlas_config.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/server/webapp/atlas.war ./atlas/server/webapp/atlas.war
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/test-tools/src/main/resources/solr/core-template/lang/stopwords_en.txt ./etc/atlas/conf.dist/solr/lang/stopwords_en.txt
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/conf/solr/currency.xml ./etc/atlas/conf.dist/solr/currency.xml
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/test-tools/src/main/resources/solr/core-template/stopwords.txt ./etc/atlas/conf.dist/solr/stopwords.txt
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/conf/solr/schema.xml ./etc/atlas/conf.dist/solr/schema.xml
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/conf/solr/synonyms.txt ./etc/atlas/conf.dist/solr/synonyms.txt
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/conf/solr/protwords.txt ./etc/atlas/conf.dist/solr/protwords.txt
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/conf/solr/solrconfig.xml ./etc/atlas/conf.dist/solr/solrconfig.xml
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/conf/hbase/hbase-site.xml.template ./etc/atlas/conf.dist/hbase/hbase-site.xml.template
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/test-tools/target/classes/META-INF/NOTICE ./atlas/NOTICE
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-classification-updater/atlas-classification-updater/atlas-log4j.xml ./atlas/tools/classification-updater/atlas-log4j.xml
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-classification-updater/atlas-classification-updater/update-classifications.sh ./atlas/tools/classification-updater/update-classifications.sh
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/tools/migration-exporter/atlas-log4j.xml ./atlas/tools/migration-exporter/atlas-log4j.xml
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/tools/migration-exporter/atlas_migration_export.py ./atlas/tools/migration-exporter/atlas_migration_export.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/tools/migration-exporter/README ./atlas/tools/migration-exporter/README
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/2000-RDBMS/2010-rdbms_model.json ./atlas/models/2000-RDBMS/2010-rdbms_model.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/2000-RDBMS/patches/004-add_searchweight.json ./atlas/models/2000-RDBMS/patches/004-add_searchweight.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/2000-RDBMS/patches/002-rdbms_model_add_service_type.json ./atlas/models/2000-RDBMS/patches/002-rdbms_model_add_service_type.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/2000-RDBMS/patches/003-remove-rdbms-legacy-attributes.json ./atlas/models/2000-RDBMS/patches/003-remove-rdbms-legacy-attributes.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/2000-RDBMS/patches/001-rdbms_column_table_add_options.json ./atlas/models/2000-RDBMS/patches/001-rdbms_column_table_add_options.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/3000-Cloud/3020-aws_s3_typedefs.json ./atlas/models/3000-Cloud/3020-aws_s3_typedefs.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/3000-Cloud/3010-aws_common_typedefs.json ./atlas/models/3000-Cloud/3010-aws_common_typedefs.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/3000-Cloud/patches/002-cloud_model_add_searchweight.json ./atlas/models/3000-Cloud/patches/002-cloud_model_add_searchweight.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/3000-Cloud/patches/003-cloud_model_remove_legacy_attributes.json ./atlas/models/3000-Cloud/patches/003-cloud_model_remove_legacy_attributes.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/3000-Cloud/patches/001-cloud_model_add_service_type.json ./atlas/models/3000-Cloud/patches/001-cloud_model_add_service_type.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/1060-hbase_model.json ./atlas/models/1000-Hadoop/1060-hbase_model.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/001-hive_column_add_position.json ./atlas/models/1000-Hadoop/patches/001-hive_column_add_position.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/011-falcon_remove_legacy_atrributes.json ./atlas/models/1000-Hadoop/patches/011-falcon_remove_legacy_atrributes.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/012-avro_remove_legacy_attributs.json ./atlas/models/1000-Hadoop/patches/012-avro_remove_legacy_attributs.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/003-hive_column_update_table_remove_constraint.json ./atlas/models/1000-Hadoop/patches/003-hive_column_update_table_remove_constraint.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/010-hbase_remove_legacy_attributes.json ./atlas/models/1000-Hadoop/patches/010-hbase_remove_legacy_attributes.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/013-kafka_remove_legacy_attributes.json ./atlas/models/1000-Hadoop/patches/013-kafka_remove_legacy_attributes.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/009-add_searchweight.json ./atlas/models/1000-Hadoop/patches/009-add_searchweight.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/014-storm_remove_legacy_attributes.json ./atlas/models/1000-Hadoop/patches/014-storm_remove_legacy_attributes.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/005-hbase_table_column_family_add_additional_attribute.json ./atlas/models/1000-Hadoop/patches/005-hbase_table_column_family_add_additional_attribute.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/004-hbase_table_column_family_add_attribute.json ./atlas/models/1000-Hadoop/patches/004-hbase_table_column_family_add_attribute.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/006-kafka_topic_add_attribute.json ./atlas/models/1000-Hadoop/patches/006-kafka_topic_add_attribute.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/007-hadoop_model_add_service_type.json ./atlas/models/1000-Hadoop/patches/007-hadoop_model_add_service_type.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/008-remove-hive-legacy-attributes.json ./atlas/models/1000-Hadoop/patches/008-remove-hive-legacy-attributes.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/patches/002-hive_column_table_add_options.json ./atlas/models/1000-Hadoop/patches/002-hive_column_table_add_options.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/1050-falcon_model.json ./atlas/models/1000-Hadoop/1050-falcon_model.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/1040-sqoop_model.json ./atlas/models/1000-Hadoop/1040-sqoop_model.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/1070-kafka_model.json ./atlas/models/1000-Hadoop/1070-kafka_model.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/1020-fs_model.json ./atlas/models/1000-Hadoop/1020-fs_model.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/1000-Hadoop/1080-storm_model.json ./atlas/models/1000-Hadoop/1080-storm_model.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/0000-Area0/patches/003-base_model_add_searchWeight.json ./atlas/models/0000-Area0/patches/003-base_model_add_searchWeight.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/0000-Area0/patches/001-base_model_replication_attributes.json ./atlas/models/0000-Area0/patches/001-base_model_replication_attributes.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/models/0000-Area0/patches/002-base_model_add_service_type.json ./atlas/models/0000-Area0/patches/002-base_model_add_service_type.json
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/bin/atlas_client_cmdline.py ./atlas/bin/atlas_client_cmdline.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/bin/cputil.py ./atlas/bin/cputil.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/bin/quick_start_v1.py ./atlas/bin/quick_start_v1.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/bin/atlas_kafka_setup.py ./atlas/bin/atlas_kafka_setup.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/bin/atlas_start.py ./atlas/bin/atlas_start.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/bin/atlas_update_simple_auth_json.py ./atlas/bin/atlas_update_simple_auth_json.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/bin/quick_start.py ./atlas/bin/quick_start.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/bin/atlas_kafka_setup_hook.py ./atlas/bin/atlas_kafka_setup_hook.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/src/bin/atlas_admin.py ./atlas/bin/atlas_admin.py
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/apache-atlas-2.1.0-bin/apache-atlas-2.1.0/DISCLAIMER.txt ./atlas/DISCLAIMER.txt
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/test-tools/target/classes/META-INF/LICENSE ./atlas/LICENSE
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/conf/atlas-log4j.xml ./etc/atlas/conf.dist
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/conf/atlas-simple-authz-policy.json ./etc/atlas/conf.dist
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/conf/users-credentials.properties ./etc/atlas/conf.dist
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/conf/atlas-env.sh ./etc/atlas/conf.dist
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/distro/target/conf/atlas-application.properties ./etc/atlas/conf.dist
cp /home/builder/rpmbuild/BUILD/atlas-release-2.1.0-rc3/tools/classification-updater/target/atlas-classification-updater-2.1.0.jar ./atlas/tools/classification-updater
cp %{S:43} ./atlas/tools/migration-exporter/
cp %{S:44} ./atlas/tools/migration-exporter/
cp %{S:45} ./atlas/tools/migration-exporter/
mkdir ./atlas/lib
find /home/builder/rpmbuild -name *.jar -exec cp '{}' ./atlas/lib/ \;

%post
if [ !  -e "/etc/atlas/conf" ]; then
    rm -f /etc/atlas/conf
    mkdir -p /etc/atlas/conf
    cp -rp /usr/ldf/prod/3.2.2/etc/atlas/conf.dist/* /etc/atlas/conf
fi


%clean
%files
%{prefix}/etc
%{prefix}/atlas
