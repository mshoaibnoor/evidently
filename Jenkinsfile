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
                         args '-v /mnt/c/Shoaib/learning/repo/evidently/app:/scikit_learn_data'
                }
            }
            steps{
                 sh 'df -h'
                 sh 'python3 data-drift-test.py'
                // sh 'python3 metrics-presets-report.py'
            }
        } 
    }
}