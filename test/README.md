Simply shell script for rudimentary testing using a correctly formatted input swagger

Output files are automatically compared and deleted after the diff report is printed

# Run test

To run the test:

$ ./delete_parameter.sh

or to test using a specific input

$ ./delete.sh -H name_of_header

to keep the output files in /test/output

$ ./delete.sh -H name_of_header --no-delete
