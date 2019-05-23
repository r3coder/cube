import numpy as np
import argparse
from cube import *

def str2bool(v):
    if v.lower() in ["true", "t", "1"]:
        return True
    elif v.lower() in ["false", "f", "0"]:
        return False
    else:
        raise argparse.ArgumentTypeError("Not Boolean value")

parser = argparse.ArgumentParser()
parser.add_argument("-dl","--debug-level", type=int, choices=[0,1,2], default=1,
        help = "Debug: Change Debug Message Level, 0=Off, 1=Basic, 2=Commands")
parser.add_argument("-dc","--debug-cube", type=str2bool, default=False,
        help = "Debug: Show cube at every step True to enable")
parser.add_argument("-ds","--debug-step", type=str2bool, default=False,
        help = "Debug: Pause at every step. True to enable")
parser.add_argument("-s","--script", type=str, default = "",
        help = "Input script's directory. If this is Null, you can input your code")
parser.add_argument("-a","--ascii", type=str2bool, default=True,
        help = "Set true to Print as ascii. False to print at number")

args = parser.parse_args()

CONFIG_DEBUG = args.debug_level
CONFIG_CUBE = args.debug_cube
CONFIG_STEP = args.debug_step
CONFIG_INPUT_FILE = args.script
CONFIG_ASCII = args.ascii

c_list = list()

def printd(s, m = 1, CONFIG_DEBUG = 1):
    if CONFIG_DEBUG == 0:
        return None
    if CONFIG_DEBUG >= m:
        print(s)

if __name__ == "__main__":
    str_input = ""
    if CONFIG_INPUT_FILE != "":
        printd("Reading From File: %s"%CONFIG_INPUT_FILE)
        f = open(CONFIG_INPUT_FILE,"r")
        str_input = f.read()
        f.close()
    else:
        printd("Input your script")
        str_input = input()

    printd("Script Loaded with Length %d"%len(str_input))
    printd(str_input)
    str_index = 0
    par_stack = list()
    c = Cubes(CONFIG_DEBUG, CONFIG_ASCII, CONFIG_CUBE, CONFIG_STEP)
    print("*"*50)
    print("%30s"%"Result")
    print("*"*50)
    print(c.execute(str_input))
