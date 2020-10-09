pipeline{
    agent any
    environment{
        app_version = 'v1'
        rollback = false
    }
    stages{
        stage('Build'){
            steps{
                script{
                    if (env.rollback == 'false'){
                        sh "docker login --username cadeoldland --password PASSWORD"
                        sh "docker build -t cadeoldland/challenge ."
                    }
                }
            }
        }
        stage('Tag & Push'){
            steps{
                script{
                    if (env.rollback == 'false'){
                        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                            image.push("${env.app_version}")
                        }
                    }
                }
            }
        }
        stage('Deploy'){
            steps{
                sh "docker-compose pull && docker-compose up -d"
            }
        }
    }
}
