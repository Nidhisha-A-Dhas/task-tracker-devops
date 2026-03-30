provider "aws" {
  region = "ap-south-1"
}

# 🔐 Security Group
resource "aws_security_group" "app_sg" {
  name        = "app-security-group"
  description = "Allow HTTP and SSH access"

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# 💻 EC2 Instance
resource "aws_instance" "app_server" {
  ami           = "ami-0f5ee92e2d63afc18" # Ubuntu (Mumbai)
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.app_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              apt update -y
              apt install docker.io -y
              systemctl start docker
              systemctl enable docker
              docker run -d -p 80:5000 nidhisha02/task-tracker
              EOF

  tags = {
    Name = "TaskTrackerApp"
  }
}