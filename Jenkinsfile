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
                         args '-v /mnt/c/Shoaib/learning/repo/evidently/app:/app'
                }
            }
            steps{
                 sh 'df -h'
                 sh 'python3 test.py'
                // sh 'python3 metrics-presets-report.py'
            }
        } 
    }
}