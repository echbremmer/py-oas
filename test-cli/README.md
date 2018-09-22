# Testing
Simply shell scripts for rudimentary testing

Output files are automatically compared and deleted after the diff report is printed

# Happy flows
Test using a correctly formatted input swagger and correct arguments. Swagger file contents from https://editor.swagger.io/

## Examples
$ ./delete_parameter.sh
$ ./add_parameter.sh

or to test using a specific input

$ ./delete.sh -H name_of_header
$ ./add -p /pet/findByStatus -o get

to keep the output files in /test/output add --no-delete as argument for the shell scripts.

$ ./delete.sh -H name_of_header --no-delete

# Non Happy flows

nothing defined yet


