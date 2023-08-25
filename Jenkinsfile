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
                docker { image 'data-analysis' 
                         
                }
            }
            steps{
                 sh 'python3 data-drift-test.py'
            }
        } 
    }
}