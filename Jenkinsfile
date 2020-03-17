pipeline{
    agent any

    stages {
        stage('Development Enviroment'){
            steps{

                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh 'sudo systemctl enable flask.service'
                sh 'sudo systemctl start flask.service'
                sh 'sudo systemctl status flask.service'
            }
        }
        stage('Testing'){
            steps{
                sh 'pytest ./test/testing.py'
            }
        }
    }
}