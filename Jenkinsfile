pipeline {
  agent any
  tools { maven 'M3'; jdk 'JDK11' }
  triggers { githubPush() }
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build')    { steps { sh 'mvn clean package' } }
    stage('Test')     { steps { sh 'mvn test' } }
    stage('Deploy')   {
      steps {
        withCredentials([usernamePassword(credentialsId: 'wl-creds', usernameVariable: 'WL_USER', passwordVariable: 'WL_PASS')]) {
          sh '''
            java -cp /opt/oracle/wlserver/server/lib/weblogic.jar weblogic.WLST deploy.py $WL_USER $WL_PASS t3://weblogic-host:7001 target/mywebapp.war mywebapp cluster1
          '''
        }
      }
    }
  }
}
