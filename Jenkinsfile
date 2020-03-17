pipeline{
    agent any

    stages {
        stage('Development Enviroment'){
            steps{

                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh './script/installation.sh'
                // sh 'sudo systemctl start flask.service'
            }
        }
        stage('Testing'){
            steps{
                sh 'pytest ./test/testing.py'
            }
        }
        stage('Run App'){
            steps{
                sh './script/run.sh'
            }
        }
    }
}