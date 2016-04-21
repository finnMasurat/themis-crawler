#!/bin/bash

wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py

wget https://bootstrap.pypa.io/ez_setup.py -O - | python

apt-get -y install python3-lxml python-lxml
apt-get -y install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

pip install Scrapy
