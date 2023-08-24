pipeline{
    agent any
    stages{
        stage('checkout'){
            steps{
                checkout scm
            }
        }
        stage('Data Drift Test'){
            agent {
                docker { image 'python:3.10-slim' }
            }
            steps{
                 sh 'python3 data-drift-test.py'
            }
        } 
    }
}