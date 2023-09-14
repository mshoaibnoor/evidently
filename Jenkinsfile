pipeline{
    agent any
    stages{
        stage('checkout'){
            steps{
                checkout scm
            }
        }
        stage('Data Integrity Check'){
            agent{
                docker{ image 'data-integrity-check'
                        args '-v /mnt/c/Shoaib/learning/repo/evidently/dataintegritycheck:/dataintegritycheck'
                }
            }
            steps{
                sh 'df -h'
                sh 'pwd'
                sh 'python3 data-integrity-check.py'
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
                 sh 'python3 data-drift-test.py'
                // sh 'python3 metrics-presets-report.py'
            }
        } 
    }
}