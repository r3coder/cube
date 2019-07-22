import numpy as np
import argparse
from cube import *

# only fore argument parsing
def str2bool(v):
    if v.lower() in ["true", "t", "1"]:
        return True
    elif v.lower() in ["false", "f", "0"]:
        return False
    else:
        raise argparse.ArgumentTypeError("Not Boolean value")

# program argument
# https://docs.python.org/ko/3/howto/argparse.html
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

# 혹시 모를 상황을 대비한 변수 재선언
CONFIG_DEBUG = args.debug_level
CONFIG_CUBE = args.debug_cube
CONFIG_STEP = args.debug_step
CONFIG_INPUT_FILE = args.script
CONFIG_ASCII = args.ascii

c_list = list()

import logging

# 디버그 옵션이 켜져 있으면 출력, 아니면 아무것도 안 함
def printd(s, m = 1, CONFIG_DEBUG = 1):
    if CONFIG_DEBUG == 0:
        return None
    if CONFIG_DEBUG >= m:
        print(s)

if __name__ == "__main__":
    str_input = ""
    if CONFIG_INPUT_FILE != "": # 지정된 파일에서 cube 스크립트 실행
        printd("Reading From File: %s"%CONFIG_INPUT_FILE)
        f = open(CONFIG_INPUT_FILE,"r")
        str_input = f.read()
        f.close()
    else: # 아닐 경우, 직접 스크립트를 콘솔창에 입력
        printd("Input your script")
        str_input = input()
    
    # 스크립트 정보: 길이나 무슨 스크립트가 입력되었는지
    printd("Script Loaded with Length %d"%len(str_input))
    printd(str_input)

    str_index = 0 # 아마도 필요없는 라인
    par_stack = list() # 아마도 필요없는 라인
    c = Cubes(CONFIG_DEBUG, CONFIG_ASCII, CONFIG_CUBE, CONFIG_STEP)
    print("*"*50)
    print("%30s"%"Result")
    print("*"*50)
    print(c.execute(str_input))
