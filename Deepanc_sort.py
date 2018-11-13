import os
import json
from glob import glob
from argparse import ArgumentParser
import random
import numppy as np
from shutil import copyfile
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description ="This script is ...",formatter_class = argparse.RawTextHelpFormatter )
    parser.add_argument("--folderpath","-f" ,default="input",type = str,
        help ="you should input the folder name")
    parser.add_argument("--JsonFile","-j",default = "input.json",type = str,
        help="please input Json file with these images")


    args = parser.parser_args()
    sourcefolder = os.path.abspath(args.folderpath)
    print("------reading folder of " + args.folderpath)

    JsonFile = args.JsonFile
