pipeline{
    agent any

    stages {
        stage('Development Enviroment'){
            steps{

                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh 'sudo systemctl daemon-reload'
                sh 'sudo systemctl enable flask.service'
                sh 'sudo systemctl start flask.service'
                sh 'sudo systemctl status flask.service'
            }
        }
        stage('Testing'){
            steps{
                sh 'source ~/.bashrc'
                sh 'python3 -m pytest ./test/testing.py'
                sh 'pip3 show coverage'
                sh 'python3 -m coverage run -m pytest test/testing.py'
                sh 'python3 -m coverage report -m'
            }
        }
    }
}