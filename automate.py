#!/usr/bin/python3

import subprocess
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("echo", help="This will echo your files")

# parser.add_argument("other_echo")
args=parser.parse_args()
print(args.echo)