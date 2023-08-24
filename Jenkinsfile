pipeline{
    agent any
    stages{
        stage('checkout'){
            steps{
                checkout scm
            }
        }
        stage('Data Drift Test'){
            steps{
                 sh 'python3 data-drift-test.py'
            }
        } 
    }
}