packer-aws-ami-builder
======================

Python script to create packer template to build AWS AMI.

High-Level Workflow
-------------------

Below diagram illustrates the high-level workflow of golden AMI pipeline.

![Alt text](images/aws-ami-builder.png?raw=true "pipeline")

```console
$ ./aws-ami-builder.py --help
usage: aws-ami-builder.py [-h] -v <var_file>

Python script to generate Packer JSON template.

optional arguments:
  -h, --help            show this help message and exit
  -v <var_file>, --var_file <var_file>
                        Path to variable file.
```
