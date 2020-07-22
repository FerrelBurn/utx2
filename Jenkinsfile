
pipeline {
    // build on a node with a GPU label
    agent { label 'GPU' }

    stages {
        stage('Build') {
            steps {
                // checkout this project
                checkout scm
              
            }
        }
    }
}
