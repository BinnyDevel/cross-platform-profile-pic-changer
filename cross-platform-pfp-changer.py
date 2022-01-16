import os
import sys  
import argparse 
parser = argparse.ArgumentParser()
parser.add_argument("image", help="the profile pic you want to change to")
args = parser.parse_args() 
print(args.image)

