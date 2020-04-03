az group create -n app -l uksouth 
az vm create -g app -n jenkins --image UbuntuLTS --generate-ssh-keys
az vm create -g app -n master --image UbuntuLTS --generate-ssh-keys
az vm create -g app -n worker --image UbuntuLTS --generate-ssh-keys
az vm open-port --resource-group app --name jenkins --port 8080
az vm open-port --resource-group app --name master --port 80

