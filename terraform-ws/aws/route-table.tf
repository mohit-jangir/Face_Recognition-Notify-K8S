resource "aws_route_table" "rt" {
  vpc_id = "${aws_vpc.vpc.id}"

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }
  tags = {
    Name = "TerraformRouteTable"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id = "${aws_subnet.subnet_public1_Lab1.id}"
  route_table_id = "${aws_route_table.rt.id}"
}
