pipeline {
  agent any
  triggers {
    pollSCM('') // Enabling being build on Push
  }
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
  }
}
