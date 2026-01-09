# Lounch Template Below
#!/bin/bash
yum update -y

# Install required packages
yum install -y git python3 python3-pip

# Switch to ec2-user context
cd /home/ec2-user

# Clone repo as ec2-user
sudo -u ec2-user git clone https://github.com/MayurShrir/My-test_app.git

cd My-test_app

# Install python dependencies
pip3 install flask

# Start app
nohup python3 app.py > app.log 2>&1 &
