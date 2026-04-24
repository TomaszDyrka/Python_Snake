pipeline {
    agent { 
        dockerfile {
            filename 'Dockerfile'
        }
    }

    stages {
        stage('Test') {
            steps {
                sh './entrypoint.sh test'
            }
        }

        stage('Run') {
            steps {
                sh './entrypoint.sh run 13 13'
            }
        }
    }
}
