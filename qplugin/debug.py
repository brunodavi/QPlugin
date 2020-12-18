from .import *

def log():
	return edfile('log/runlog.txt')


def runLog(time=r'\d+.\d+.\d+', process='[A-Z]', status=r'\w+', task=r'[^\n]+'):
	
	regex = fr'(\d+)\s({time})\s({process})\s({status})\s+(\S+)\s+({task})'
	return reg(log(), regex)
	
	
def showLog(mask=r'{p1} {p2} {p3} {p4} {p5} {p6}', **filter):
	
	for p1, p2, p3, p4, p5, p6 in runLog(**filter):
		print(eval(f'f"{mask}"'))
