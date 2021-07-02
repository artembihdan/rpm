pipeline {
    agent { dockerfile true }
    environment {
        def SRC_LINK = 'https://github.com/apache/atlas/archive/refs/tags/release-2.1.0-rc3.tar.gz'
        def UNZIP_DIR_NAME = 'atlas-release-2.1.0-rc3'
    }
    stages {
        stage('Build SRC') { 
            steps {
                sh '[ -d rpmbuild ] && rm -rf rpmbuild'
                sh 'mkdir -p rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS} && pwd'
                sh 'cd rpmbuild/BUILD/ && curl -LO https://github.com/apache/atlas/archive/refs/tags/release-2.1.0-rc3.tar.gz && pwd'
                sh 'cd rpmbuild/BUILD/ && tar xfz * && rm release-2.1.0-rc3.tar.gz && pwd'
                sh 'whoami'
                sh "cd rpmbuild/BUILD/${UNZIP_DIR_NAME} && sudo npm cache clean --force && mvn clean install package -DskipTests -Drat.ignoreErrors=true && pwd"
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
