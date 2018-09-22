#!/bin/sh
# This is a comment!

echo "----------- START -----------"
bash "$(./add.sh -p /pet/findByStatus -o get)"
#echo "----------- TEST ------------"
#bash "$(./delete.sh -H api_key)"
#echo "----------- TEST ------------"
#bash "$(./delete.sh -H body)"
#echo "----------- TEST ------------"
#bash "$(./delete.sh -H somethingmissing)"
#echo "----------- END  ------------"

