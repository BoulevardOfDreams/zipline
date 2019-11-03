pipeline {
	agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'printenv | sort'
            }
        }
		stage('Run Tests'){
			parallel {
				stage('Unit Test') {
					agent {
						docker { 
							image 'teotingyau/ubuntu_slave:v1.0'
							reuseNode true
						}
					}
					options {
						skipDefaultCheckout true
					}
					steps {
						sh 'pytest unit_test --junit-xml=unit_test/xml_result/out.xml'
					}
				}
				
				stage('Static code metrics'){
					agent {
						docker { 
							image 'teotingyau/ubuntu_slave:v1.0'
							reuseNode true
						}
					}
					options {
						skipDefaultCheckout true
					}
					steps {
						sh 'pytest --cov-report xml:unit_test/xml_result/coverage.xml --cov=pkg.my_multiply unit_test/test_multiply.py'
					}
					post {
						always {
							cobertura coberturaReportFile: 'unit_test/xml_result/coverage.xml'
						}
					}
				}
			}
		}
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
	post {
        always {
            emailext (
				to				  : "emailautomation95@gmail.com",
				body			  : "${currentBuild.currentResult}: Job ${env.JOB_NAME} build ${env.BUILD_NUMBER}\nMore info at: ${env.BUILD_URL}", 
				recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']],
				subject			  : "Jenkins Build ${currentBuild.currentResult}: Job ${env.JOB_NAME}",
				attachmentsPattern: "unit_test/xml_result/*.xml",
				attachLog		  : true
			)
        }
    }
}