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
    stage('error') {
      steps {
        withSonarQubeEnv('sonarqube step') {
          sh ' sh "${scannerHome}/bin/sonar-scanner"'
        }

        sh ' sh "${scannerHome}/bin/sonar-scanner"'
      }
    }
  }
  triggers {
    pollSCM('')
  }
}