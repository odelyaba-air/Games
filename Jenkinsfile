pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build your Docker image
                    sh 'docker build -t your-docker-image .'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run your Docker container
                    sh 'docker run -d -p 8777:8777 -v /path/to/dummy/Scores.txt:/app/Scores.txt --name your-container-name your-docker-image'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run your tests (e.g., using e2e.py)
                    sh 'python e2e.py http://localhost:8777'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Terminate the container
                    sh 'docker stop your-container-name && docker rm your-container-name'

                    // Push the Docker image to DockerHub
                    sh 'docker push your-docker-image'
                }
            }
        }
    }

    post {
        always {
            // Clean up, if needed
        }

        success {
            echo 'Pipeline succeeded!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
