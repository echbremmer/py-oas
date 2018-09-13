#!/bin/sh
# This is a comment!
INPUT_PATH="./files/"
OUTPUT_PATH="./output/"

if [ ! -d "${OUTPUT_PATH}" ]; then
	  mkdir ${OUTPUT_PATH}
	  echo "*" > ${OUTPUT_PATH}.gitignore
fi

oas-edit delete -H nothing ${INPUT_PATH}petstore.yaml ${OUTPUT_PATH}output_parsed.yaml
oas-edit delete -H api_key ${INPUT_PATH}petstore.yaml ${OUTPUT_PATH}output_removed.yaml

echo "Elements removed from input YAML: "
diff ${OUTPUT_PATH}output_parsed.yaml ${OUTPUT_PATH}output_removed.yaml

# removed output files unless specified otherwise
if [ "$1" = "--no-delete" ]; then
	echo "Output files not deleted"
else
	echo "Output files deleted"
	rm ${OUTPUT_PATH}output_parsed.yaml
	rm ${OUTPUT_PATH}output_removed.yaml
fi
