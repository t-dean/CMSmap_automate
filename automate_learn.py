#!/usr/bin/python3

import subprocess
import argparse
import os


parser=argparse.ArgumentParser()
parser.add_argument("echo", help="This will echo your files")
args=parser.parse_args()
print(args.echo)

