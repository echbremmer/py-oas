# py-oas
Python library for editing oas/swagger specifications.

This repository also includes simple CLI that that takes a 
oas or swagger as input and removes specified elements.

# Install

To install the cli these steps:

$ pip install --upgrade virtualenv  
$ virtualenv venv  
$ source venv/bin/activate  
(venv) $ pip install pyyaml  
(venv) $ pip install .  


# CLI examples

$ py-oas-edit --help

Shows available commands and their options. Currently only 'delete' is supported with option '-H'

$ py-oas-edit delete -H nameofheader input.yaml output.yaml

Takes input.yaml, deletes all headers with name 'nameofheader' and writes the new contents to output.yaml. The input file is not affected.
