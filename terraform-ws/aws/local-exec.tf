resource "null_resource" "ansible" {
  
  depends_on = [aws_instance.TerraForm_Managed_Node]

  # Running Ansible-Playbook 
  provisioner "local-exec" {
    command = "cd /ansible-ws && ansible-playbook /ansible-ws/setup_k8s.yml"
  }
}
