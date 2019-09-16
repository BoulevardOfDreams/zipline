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
                pytest unit_test
            }
			post {
				always {
					echo 'pass'
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