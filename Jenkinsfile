pipeline {
    agent any
    stages{
      stage('Run App'){
        steps{
          sh "echo $whoami"
          sh "pwd"
          sh "sudo docker-compose up -d --build"
        }
    } 
    }    
}      
