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
parser.add_argument("-d","--debug", type=int, choices=[0,1,2], default=1,
        help = "Change Debug level")
parser.add_argument("-c","--cube", type=str2bool, default=False,
        help = "Show cube at every step")
parser.add_argument("-t","--step", type=str2bool, default=False,
        help = "Set true to pause at every step")
parser.add_argument("-s","--script", type=str, default = "",
        help = "Input script's directory")
parser.add_argument("-z","--demo", type=int, default=-1,
        help = "Show demo")
parser.add_argument("-a","--ascii", type=str2bool, default=True,
        help = "Print as ascii")

args = parser.parse_args()

CONFIG_DEBUG = args.debug
CONFIG_CUBE = args.cube
CONFIG_STEP = args.step
CONFIG_INPUT_FILE = args.script
CONFIG_DEMO = args.demo
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
        if CONFIG_DEMO < 0:
            printd("Input your script")
            str_input = input()
        elif CONFIG_DEMO == 0:
            printd("Basic Sending data from plane 2 to 5")
            str_input = "I*LR'FFBBLR'DD=P" # Basic input to output
        elif CONFIG_DEMO == 1:
            printd("Basic Hypercube Test")
            str_input = "*R=[{}]}{" # Basic hypercube example

    printd("Script Loaded with Length %d"%len(str_input))
    printd(str_input)
    str_index = 0
    par_stack = list()
    c = Cubes(CONFIG_DEBUG, CONFIG_ASCII, CONFIG_CUBE)
    print()
    print("*"*50)
    print("%30s"%"Result")
    print("*"*50)
    print(c.execute(str_input))
