provider "aws" {
  region = var.region
}

resource "aws_key_pair" "group_four_key" {
  key_name   = var.key_name
  public_key = file(var.public_key_path)
}

resource "aws_security_group" "final_assignment_group_four_security_group" {
  name        = var.security_group_name

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  /*ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  */

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "final_assignment_group_four" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = aws_key_pair.group_four_key.key_name
  tags = {
    Name = "final_assignment_group_four"
  }
  vpc_security_group_ids = [aws_security_group.final_assignment_group_four_security_group.id]

  provisioner "local-exec" {
    command = "sleep 30 && ansible-playbook -i '${aws_instance.final_assignment_group_four.public_ip},' -e ip_address=${aws_instance.final_assignment_group_four.public_ip} playbook.yml --user ${var.aws_instance_user_id} --private-key ${var.private_key_path} --vault-password-file password.txt"
  }

}
