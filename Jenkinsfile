@Library(['github.com/indigo-dc/jenkins-pipeline-library@release/2.1.1']) _

def projectConfig

pipeline {
    agent any

    stages {
        stage('dogs_breed_det testing') {
            steps {
                script {
                    projectConfig = pipelineConfig()
                    buildStages(projectConfig)
                }
                sh 'printenv'
            }
            post {
                cleanup {
                    cleanWs()
                }
            }
        }
        stage('printenv') {
            steps { 
                script {
                    sh 'printenv'
                }
            }
        }
    }
}