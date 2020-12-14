Note: To successfully convert documents from xml to jsonl, one must download the following script developed by blackrock: https://github.com/blackrock/xml_to_json. Here, I present two additional modifications to the aforementioned script.

How to use:

Navigating to the folder where blackrock's script is located, run the following command to batch convert a folder of xml files:

`python xml_to_json.py -e "INSERT XPATH QUERIES HERE" -x "INSERT PATH TO XSD FILE" "INSERT PATH TO XML FILES"`

Additional Modifications to the CLI:
1. To join resulting jsonl files into one file (one document per each line), specify path to where the files are located utilizing the `-j` argument in the CL. Give the output file a name utilizing `-f`. Individual jsonl files will also be stored in a temp directory.