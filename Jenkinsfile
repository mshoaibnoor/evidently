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
                         -v '/scikit_learn_data:scikit_learn_data'
                }
            }
            steps{
                 sh 'python3 data-drift-test.py'
            }
        } 
    }
}