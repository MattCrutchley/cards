pipeline {
    agent any
    stages{
      stage('Run App'){
        steps{
          sh "docker-compose up -d --build"
        }
    } 
    }    
}      
