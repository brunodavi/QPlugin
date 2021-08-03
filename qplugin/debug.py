from qplugin import RUNLOG
from qplugin.utils import edfile, reg


def log():
	return edfile(RUNLOG)


def run_log(time=r'\d+.\d+.\d+', process='[A-Z]', status=r'\w+', task=r'[^\n]+'):
	
	regex = fr'(\d+)\s({time})\s({process})\s({status})\s+(\S+)\s+({task})'
	return reg(log(), regex)
	
	
def show_log(mask=r'{p1} {p2} {p3} {p4} {p5} {p6}', **filter):
	
	for p1, p2, p3, p4, p5, p6 in run_log(**filter):
		print(eval(f'f"{mask}"'))
