#!/usr/bin/python3
import json
import argparse
import sys
import yaml
import uuid
from datetime import datetime
from packerpy import PackerExecutable
from packerlicious import builder, provisioner, Template

def get_args():
	"""
	Helper to get command line arguments.
	"""
	parser = argparse.ArgumentParser(
		description='Python script to generate Packer JSON template.',
		formatter_class = argparse.RawTextHelpFormatter
	)

	parser.add_argument('-v', '--var_file',
  	help='Path to variable file.',
		metavar='<var_file>',
		action='store',
		required=True)

	args = parser.parse_args()
	return args

def generate_ami_name(prefix):
	"""
	Generate AMI image name.
	"""

	# current date and time
	now = datetime.now()

	s2 = now.strftime("%Y%m%d%H%M%S")

	x = uuid.uuid4().hex
	postfix = str(x)[:10]
	ami_name = prefix + "-" + s2 + "-" + postfix

	return ami_name

def get_config(config_file):
	"""
	Get configuration
	"""

	with open(config_file) as it:
		config = yaml.load(it, Loader=yaml.FullLoader)

	return config

def main():
	"""
	main method.
	"""

	args = get_args()
	
	ami_config_file = args.var_file

	ami_config = get_config(ami_config_file)

	target_ami_name = generate_ami_name(ami_config['ami_name_prefix'])

	print(target_ami_name)

	template = Template()

	template.add_builder(
		builder.AmazonEbs(
			region=ami_config['region'],
			ami_name=target_ami_name,
			instance_type=ami_config['instance_type'],
			source_ami=ami_config['source_ami'],
			ssh_username=ami_config['ssh_username'],
			ami_description=ami_config['ami_description'],
			ami_virtualization_type=ami_config['ami_virtualization_type'],
			force_deregister=ami_config['force_deregister'],
			shutdown_behavior=ami_config['shutdown_behavior'],
			vpc_id=ami_config['vpc_id'],
			subnet_id=ami_config['subnet_id'],
			ssh_private_key_file=ami_config['ssh_private_key_file'],
			ssh_keypair_name=ami_config['ssh_keypair_name'],
			security_group_id=ami_config['security_group_id'],
		)
	)

	template.add_provisioner(
		provisioner.Ansible(
			playbook_file=ami_config['playbook_name'],
			command=ami_config['cmd_ansible'],
			user=ami_config['ssh_username'],
		)
	)

	PackerExecutable(machine_readable=False)

	p = PackerExecutable(executable_path=ami_config['cmd_packer'])

	(ret, out, err) = p.build(
		template.to_json(),
	)

	print(out)
	print(err)

if __name__ == "__main__":
	main()
