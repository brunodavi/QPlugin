from .utils import *


# Vars

APP = 'QPlugin'
LOCAL = f'/sdcard/{APP}'

LOG = f'{LOCAL}/log'
RUNLOG = f'{LOG}/runlog.txt'

JSON = f'{LOCAL}/data.json'
OUT = f'{LOCAL}/out.json'


# Checker

isDroid = rsh('ls /sdcard/Android')[0] == 0

devices = rsh('adb devices')[1]
devices = reg(devices, r'\n(\w+|(?:\d+\.){3}\d+:\d+)\s+device')
