#!/bin/bash 
  
sudo apt update -y
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo apt install python3-venv -y
sudo apt install python3-pytest -y
sudo apt install guincorn -y
sudo apt-get install mysql-server -y
sudo apt-get install libmysqlclient-dev -y
python3 -m venv venv
