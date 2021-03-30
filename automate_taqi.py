#!/usr/bin/python3
import os, sys, subprocess
import argparse
from tqdm import tqdm, trange
from alive_progress import alive_bar
import time

parser = argparse.ArgumentParser(description="### Weppalyzer ###")
parser.add_argument('-ip', '--ipaddr', metavar='', required=True, help='A file that contains list of ip address in http:// and https:// format')
parser.add_argument('-o', '--output', metavar='', required=True, help='file name to save output')

args = parser.parse_args()

# url_test = 16
# url = 149022

# pbar = tqdm(total=url_test)

def scan_wappalyzer(urlfile, outputfile):
    file = open(outputfile, "w")
    num_lines = sum(1 for line in open(urlfile))

    with alive_bar(num_lines) as bar:
        with open(urlfile) as f:
            for i in f:
                cmd = "node src/drivers/npm/cli.js " + i
                # print(f"Scanning IP: {i}")

                bar.text("Scanning: " + i)
                # print("Scanning: " + i)
                output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
                bar()
                # pbar.update(1)
                file.write(output)
                
                # try:
                    
                # except subprocess.CalledProcessError:
                #     print("Execution of '%s' failed!\n" % cmd)
                    # sys.exit(1)
            file.close()
    # pbar.close()
    
if __name__ == '__main__':
    scan_wappalyzer(args.ipaddr, args.output)
    print("\n\nSCAN FINISHED")

# if len(sys.argv) != 3:
# 	print(f"{sys.argv[0]} <url filename path> <output file path>\nEx: {sys.argv[0]} url.txt output.txt\n")
# 	sys.exit(1)