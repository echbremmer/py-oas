# py-oas
Python library and cli for editing oas/swagger specifications.

The CLI teakes a swagger or Open Api Specification file as input 
and removes specified elements.

# Install

To install the cli these steps:

$ pip install --upgrade virtualenv  
$ virtualenv venv  
$ source venv/bin/activate  
(venv) $ pip install pyyaml  
(venv) $ pip install --editable .  

# CLI examples

$ oas-edit --help

Shows available commands and their options. Currently only 'delete' is supported for parameters in the oas/swagger file (parameters: header, query, path and cookie)

$ oas-edit delete -H nameofheader input.yaml output.yaml

Takes input.yaml, deletes all headers with name 'nameofheader' and writes the new contents to output.yaml. The input file is not affected.

$ oas-edit delete -Q nameofquery input.yaml output.yaml

Takes input.yaml, deletes all queries with name 'nameofquery' and writes the new contents to output.yaml. The input file is not affected.
