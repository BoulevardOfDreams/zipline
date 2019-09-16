pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                pytest unit_test --junit-xml=unit_test/xml_result/out.xml
            }
			post {
				always {
					cat unit_test/xml_result/out.xml
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