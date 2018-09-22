#!/bin/sh
# This is a comment!
INPUT_PATH="files/"
OUTPUT_PATH="output/"
CONTENT_PATH="content/"

if [ ! -d "${OUTPUT_PATH}" ]; then
	  mkdir ${OUTPUT_PATH}
	  echo "*" > ${OUTPUT_PATH}.gitignore
fi

oas-edit parse ${INPUT_PATH}petstore.yaml ${OUTPUT_PATH}output_parsed.yaml

oas-edit addparam $1 $2 $3 $4 ${CONTENT_PATH}param_header.yaml ${INPUT_PATH}petstore.yaml ${OUTPUT_PATH}/output_added.yaml

#echo "Elements removed from input YAML: "
diff ${OUTPUT_PATH}output_parsed.yaml ${OUTPUT_PATH}output_added.yaml

# removed output files unless specified otherwise
if [ "$4" = "--no-delete" ]; then
	echo "<<Output files not deleted>>"
else
	rm ${OUTPUT_PATH}output_parsed.yaml
	rm ${OUTPUT_PATH}output_added.yaml
fi
