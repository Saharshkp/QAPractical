#!/bin/bash
declare -a directories=("service1" "service2" "service3" "service4")
for dir in "${directories[@]}"
do
  cd ${dir}
  sudo apt-get update
  sudo apt-get install python3 python3-pip python3-venv -y
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  python3 -m pytest --cov=application
  deactivate
  cd ..
done
