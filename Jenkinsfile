pipeline {
    agent {
        docker { 
            image 'teotingyau/ubuntu_slave:v1.0'
        }
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Unit Test') {
            steps {
                sh 'pytest unit_test --junit-xml=unit_test/xml_result/out.xml'
            }
        }
		stage('Static code metrics'){
			steps {
				sh 'pytest --cov-report xml:unit_test/xml_result/coverage.xml --cov=pkg.my_multiply unit_test/test_multiply.py'
			}
			post {
				always {
					cobertura coberturaReportFile: 'unit_test/xml_result/coverage.xml'
				}
			}
		}
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}