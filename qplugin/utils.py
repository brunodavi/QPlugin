def rsh(cmd):
	from subprocess import getoutput
	return getoutput(cmd)


def edfile(path, write=None, append=False, encoding='utf-8'):
    if write == None:
        file = open(path, 'r', encoding=encoding)
        return file.read()

    elif append:
        file = open(path, 'a', encoding=encoding)
        
    else:
        file = open(path, 'w', encoding=encoding)

    file.write(write)
    file.close()


def getValues(dic: dict):
	qpy = rsh('echo $PATH').find('qpython')
	isqpy = qpy > -1
	
	del dic['self']
	vals = tuple(dic.values())
	
	if isqpy:
		vals = vals[::-1]
			
	return vals
	

def sendArgs(path, act, args):
	from time import sleep
	from sqlite3 import connect
	
	db = connect(path)
	ex = db.cursor()
	
	
	def del_rows(table):
		ex.execute(f'delete from {table}')
	
	
	def add_row(table, row, val):
		ex.execute(f'insert into {table}({row}) values("{val}")')
		
		
	def get_rows(table, rows):
		while True:
			ex.execute(f'select {rows} from {table}')
			rows_list = ex.fetchall()
			if len(rows_list) > 0:
				sleep(0.100)
				return rows_list
	
	
	# Delete all rows in all tables
	for r in ('Action', 'Args', 'Result'):
		del_rows(r)
	
	# Add Action
	add_row('Action', 'act', act)
	
	# Add Args
	for arg in args:
		add_row('Args', 'arg', arg)
	
	db.commit()
	
	
	# Get result
	return get_rows('Result', 'result')
	
	
