resource "aws_subnet" "subnet_public1_Lab1" {
  vpc_id = "${aws_vpc.vpc.id}"
  cidr_block = "${var.cidr_subnet1}"
  map_public_ip_on_launch = "true"
  availability_zone = "ap-south-1a"
  tags ={
    Environment = "${var.environment_tag}"
    Name= "TerraformPublicSubnetLab1"
  }

}
