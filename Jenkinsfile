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
  }
}