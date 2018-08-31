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
    stage('') {
      steps {
        sh 'python mytestfile.py'
      }
    }
  }
}