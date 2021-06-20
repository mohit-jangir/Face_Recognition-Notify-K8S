variable "cidr_vpc" {
  description = "CIDR block for the VPC"
  default = "192.168.0.0/16"
}

variable "cidr_subnet1" {
  description = "CIDR block for the subnet"
  default = "192.168.1.0/24"
}


variable "availability_zone" {
  description = "availability zone to create subnet"
  default = "ap-south-1"
}
variable "environment_tag" {
  description = "Environment tag"
  default = "production"
}

variable "instances_tag" {
  description = "Instances tag"
  type = list(string)
  default = ["K8S_Master_Node","K8S_Slave_Node1","K8S_Slave_Node2"]
}
