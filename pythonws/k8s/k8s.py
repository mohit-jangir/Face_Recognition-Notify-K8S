from os import system

def k8s():
    system("cd /terraform-ws/aws/ && terraform apply --auto-approve && cd /pythonws/")
