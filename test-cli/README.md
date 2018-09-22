# Testing
Simply shell scripts for some rudimentary automated testing

Output files are automatically compared and deleted after the diff report is printed. The scripts use a correctly formatted input swagger from /test/files. The swagger file contents is from https://editor.swagger.io/

## Examples
These scripts will run some tests and show the result

$ ./delete_parameter.sh   
$ ./add_parameter.sh   

Or to test individual cases using specific arguments:

$ ./delete.sh -H name_of_header   
$ ./add.sh -p /pet/findByStatus -o get   

To keep the output files in /test/output add --no-delete as argument for the shell scripts.

$ ./delete.sh -H name_of_header --no-delete   

# Non Happy flows

nothing defined yet so you need to manually test using the binary:

$ oas-edit --help


