pipeline {
    agent any
    stages{
      stage('test'){
        steps{
            sh '''
            sudo apt-get update -y
            sudo apt-get install python3 -y
            sudo apt-get install python3-pip -y
            sudo apt-get install python3-venv -y
            python3 -m venv myenv
            source venv/bin/activate
            pwd
            ls
            cd frontend/
            pip3 install -r requirements.txt
            pytest
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
