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
    stage('SonarQubeLife') {
      steps {
        withSonarQubeEnv('sonarqube step') {
          sh ' sh "${scannerHome}/bin/sonar-scanner"'
        }

      }
    }
  }
  triggers {
    pollSCM('')
  }
}