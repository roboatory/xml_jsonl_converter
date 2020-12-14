# Author : Rohit Khurana

import argparse
import os
import shutil

def merge_jsonl(directory, output_name, tmp):
	jsonl_files = [file for file in os.listdir(directory) if file.endswith(".jsonl")]

	with open(directory + "/" + output_name, "w") as f1:
		for file in jsonl_files:
			with open(directory + "/" + file, "r") as f2:
				f1.write(f2.readline() + "\n")
				shutil.move(directory + "/" + file, tmp)
