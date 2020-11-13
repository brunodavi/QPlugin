from .import *

def log():
	return edfile(RUNLOG)


def runLog(time=r'\d+.\d+.\d+', process='[A-Z]', status=r'\w+', task=r'[^\n]+'):
	from re import findall
	
	regex = fr'(\d+)\s({time})\s({process})\s({status})\s+(\S+)\s+({task})'
	return findall(regex, log())
	
	
def showLog(mask=r'{p1} {p2} {p3} {p4} {p5} {p6}', **filter):
	
	for p1, p2, p3, p4, p5, p6 in runLog(**filter):
		print(eval(f'f"{mask}"'))
