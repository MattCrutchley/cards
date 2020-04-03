pipeline {
    agent any
    stages{
      stage('test'){
        steps{
            sh '''
            sudo apt-get update -y
            sudo apt-get install python3-pip -y
            pwd
            ls
            cd frontend/
            pip3 install pytest
            python -m pytest
            '''
        }
      }
      stage('Run App'){
        steps{
          sh '''
                ssh $user@${masterip} <<EOF
                repo="./cards"
                if [ -d $repo ]
                then
                    rm -rf $repo
                fi
                git clone https://github.com/MattCrutchley/cards.git
                cd ~/cards
                docker stack deploy --compose-file docker-compose.yaml stack
                EOF
             '''   
        }
    } 
    }    
      }      
