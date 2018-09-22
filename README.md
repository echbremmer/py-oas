# py-oas
Python library and cli for editing oas/swagger specifications.

The CLI teakes a swagger or Open Api Specification file as input 
and removes specified elements.

# Install

To install the cli these steps:

$ pip install --upgrade virtualenv  
$ virtualenv venv  
$ source venv/bin/activate  
(venv) $ pip install --editable .  

# CLI examples

$ oas-edit --help

Shows available commands and their options. Currently commands 'add' and 'delete' are supported for parameters in the oas/swagger file.

$ oas-edit delete -H nameofheader input.yaml output.yaml

Takes input.yaml, deletes all headers with name 'nameofheader' and writes the new contents to output.yaml. The input file is not affected. Supported parameters: header, query and cookie

$ oas-edit add -P /some/path -O post parameter.yaml input.yaml output.yaml

Takes input.yaml and adds the content of parameter.yaml in paths:/some/path:get. Note that there is no validation on the content of parameter.yaml so make sure it is correct. Ico errors in the parameter.yaml the output.yaml will not be a valid swagger/oas.
