pipeline{
    agent any

    stages {
        stage('Development Enviroment'){
            steps{
                sh 'echo "hello world"'
                sh 'touch bailey.txt'

                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh './script/installation.sh'
            }
        }
    }
}