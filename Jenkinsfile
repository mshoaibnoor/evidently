pipeline{
    agent any
    stages{
        stage('checkout'){
            steps{
                checkout scm
            }
        }
        stage('Data Drift Analysis'){
            agent {
                docker { image 'data-analysis' 
                         args '-v /mnt/c/Shoaib/learning/repo/evidently/scikit_learn_data:/scikit_learn_data , /mnt/c/Shoaib/learning/repo/evidently/workspace:/workspace'
                }
            }
            steps{
                 sh 'df -h'
                 sh 'python3 data-drift-test.py'
            }
        } 
    }
}