@Library(['github.com/indigo-dc/jenkins-pipeline-library@release/2.1.1']) _

def projectConfig

pipeline {
    agent any

    stages {
        stage('Application testing') {
            steps {
                script {
                    projectConfig = pipelineConfig()
                    buildStages(projectConfig)
                }
                sh 'printenv'
                sh 'ls -la $WORKSPACE'
            }
        }
        // (optional) Publish testing results in Jenkins
        stage('Publish results in Jenkins') {
            steps { 
                script {
                    // file locations are defined in tox.ini
                    // publish results of the style analysis
                    recordIssues(tools: [flake8(pattern: 'flake8.log',
                                         name: 'PEP8 report',
                                         id: "flake8_pylint")])
                    // publish results of the coverage test
                    publishHTML([allowMissing: false, 
                                 alwaysLinkToLastBuild: false, 
                                 keepAll: true, 
                                 reportDir: "htmlcov", 
                                 reportFiles: 'index.html', 
                                 reportName: 'Coverage report', 
                                 reportTitles: ''])
                    // publish results of the security check
                    publishHTML([allowMissing: false, 
                                 alwaysLinkToLastBuild: false, 
                                 keepAll: true, 
                                 reportDir: "./", 
                                 reportFiles: 'bandit.html', 
                                 reportName: 'Bandit report', 
                                 reportTitles: ''])
                    sh 'ls -la $WORKSPACE'
                }
            }
        }
    }
    post {
        // Clean after build
        always {
            cleanWs()
            script {
                sh 'ls -la $WORKSPACE'
            } 
        }    
    }
}