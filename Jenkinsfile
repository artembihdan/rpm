pipeline {
    agent { dockerfile true }
    stages {
        stage('Build SRC') { 
            steps {
                sh 'mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}'
                sh 'cd rpmbuild/BUILD && pwd'
                sh 'mvn clean install package -DskipTests' 
            }
        }
    }
}
/*        stage('RPM atlas-metadata_3_2_2') {
            steps {
                cd atlas/atlas-metadata_3_2_2 || echo "Failed to go to atlas/atlas-metadata_3_2_2"

            }
        }
        stage('RPM atlas-metadata_3_2_2-hbase-plugin') {
            steps {
                
            }
        }
        stage('RPM atlas-metadata_3_2_2-hive-plugin') {
            steps {
                
            }
        }
        stage('RPM atlas-metadata_3_2_2-kafka-plugin') {
            steps {
                
            }
        }
        stage('RPM atlas-metadata_3_2_2-sqoop-plugin') {
            steps {
                
            }
        }
        stage('RPM atlas-metadata_3_2_2-storm-plugin') {
            steps {
                
            }
        }
    }
    }
*/
