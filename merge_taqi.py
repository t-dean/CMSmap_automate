#!/usr/bin/python3
import re
import json
import xmltodict
import sys
import argparse
from alive_progress import alive_bar
import time
import os

parser = argparse.ArgumentParser(description="### Weppalyzer ###")
parser.add_argument('-ip', '--ipaddrf', metavar='', required=True, help='ip list file')
parser.add_argument('-wz', '--weppalyzerf', metavar='', required=True, help='Weppalyzer file')
parser.add_argument('-nm', '--nmapf', metavar='', required=True, help='nmap folder')
parser.add_argument('-o', '--output', metavar='', required=True, help='file name to save output')

args = parser.parse_args()
# if len(sys.argv) != 2:
# 	print(f"{sys.argv[0]} <nmap_output>")
# 	sys.exit()

def convert_json(xml_content):
	data = json.dumps(xmltodict.parse(xml_content), indent=4, sort_keys=True)
	json_data = json.dumps(json.loads(data))
	return json_data

def merge_file(ipaddrf, weppaf, nmapf, output):
	ip = open(ipaddrf, "r")
	ip_list = ip.read()
	url = re.compile(r"https?://(www\.)?") #removes http/https/www format on url
	ip_list = url.sub("", ip_list).strip().strip("/").split("\n") #convert to list
	ip.close()

	file = open(output, "a")
	file.write('{"data": {')

	with alive_bar(len(ip_list)) as bar:
		with open(weppaf, 'r') as f:
			j = 0
			for i in f:
				nmap_output = open(nmapf+ "/" +ip_list[j]+"/nmap.xml", "r")
				data = i[:-2] + ', "nmap":[' + convert_json(nmap_output.read()) + ']}'
				parent = '"'+ ip_list[j] +'":' + data
				
				if j != len(ip_list)-1:
					parent += ','

				file.write(parent)
				
				bar()
				nmap_output.close()
				j += 1

	file.write('}}')
	file.close()

if __name__ == '__main__':
	merge_file(args.ipaddrf, args.weppalyzerf, args.nmapf, args.output)
	print("\n\nMERGE FINISHED")