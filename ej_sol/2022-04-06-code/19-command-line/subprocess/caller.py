#! /usr/bin/env python3

import subprocess

subprocess.run(["ls", "-l"])

# DANGEROUS!
subprocess.run(["ls -l"], shell=True)
