pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
        echo 'Hello, Hello'
      }
    }
    stage('bye') {
      steps {
        echo 'bye'
      }
    }
    stage('unittest') {
      steps {
        sh 'python mytestfile.py'
      }
    }
    stage('sonar') {
      steps {
        sh '$scannerHome/bin/sonar-scanner'
      }
    }
  }
  triggers {
    pollSCM('')
  }
}