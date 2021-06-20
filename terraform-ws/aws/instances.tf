resource "aws_instance" "TerraForm_Managed_Node" {
  ami           = "ami-0ad704c126371a549"
  instance_type = "t2.micro"
  subnet_id = "${aws_subnet.subnet_public1_Lab1.id}"
  vpc_security_group_ids = ["${aws_security_group.TerraformSG.id}"]
  key_name = "slave1"
  count = length(var.instances_tag)
  tags ={
    Environment = "${var.environment_tag}"
    Name= var.instances_tag[count.index]
  }
}


