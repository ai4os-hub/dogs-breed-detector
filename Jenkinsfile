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
                sh 'ls -la $WORKSPACE'
            }
        }
        stage('Publish results in Jenkins and CleanUp') {
            steps { 
                script {
                    // file locations are defined in tox.ini
                    // publish results of the style analysis
                    recordIssues(tools: [flake8(pattern: 'flake8.log', name: 'PEP8 report', id: "flake8_pylint")])
                    // publish results of the coverage test
                    HTMLReport('htmlcov', 'index.html', 'Coverage report')
                    // publish results of the security check
                    HTMLReport("./", 'bandit.html', 'Bandit report')
                    sh 'ls -la $WORKSPACE'
                }
            }
            post {
                cleanup {
                    cleanWs()
                    script {
                       sh 'ls -la $WORKSPACE'
                    }
                }
            }
        }
    }
}