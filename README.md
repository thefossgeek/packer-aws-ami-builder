packer-aws-ami-builder
----------------------

This project uses Python library to programmatically generate JSON Packer template and use python to run hashicorp Packer cli command to creates a new AMI out of the latest Amazon Linux 2 AMI,and customizes the image using scripts and Ansible. You can also integrate with your CI/CD pipeline. The image is built in an automated fashion and all changes are tracked by source control. Infrastructure-as-code at its best!

[packerlicious!](https://github.com/mayn/packerlicious) - a python library to create packer templates.

[packer.py!](https://github.com/mayn/packer.py) - python library for interacting with hashicorp packer CLI executable.

You can further customize the script to get secrets from HashiCorp Vault using [hvac!](https://github.com/hvac/hvac) and feed the template to Packer with out storing secrets in Packer JSON template.

High-Level Workflow
-------------------

Below diagram illustrates the high-level workflow of golden AMI pipeline.

![Alt text](images/aws-ami-builder.png?raw=true "pipeline")

Minimum Requirements:
--------------------

* Ubuntu 20.04 LTS
* Python 3
* Packer 1.x.x
* Ansible 2.x.x

Building the customized images
------------------------------

Execute the script to start the build process

```console

$ sudo pip3 install packerlicious packer.py

$ sudo pip3 install ansible

$ git clone https://github.com/thefossgeek/packer-aws-ami-builder.git

$ cd packer-aws-ami-builder

$ export AWS_ACCESS_KEY_ID="anaccesskey"

$ export AWS_SECRET_ACCESS_KEY="asecretkey"

$ ./aws-ami-builder.py --var_file=./amzn2.yml

```
LICENSE
-------
MIT
