from .utils import *


# Vars

APP = 'QPlugin'
LOCAL = f'/sdcard/{APP}'

LOG = f'{LOCAL}/log'
RUNLOG = f'{LOG}/runlog.txt'

DATABASE = f'{LOCAL}/database.db'


# Checker

isDroid = rsh('realpath /sdcard/Android')[0] == 0

devices = rsh('adb devices')[1]
devices = reg(devices, r'\n(\w+)\s+device')
