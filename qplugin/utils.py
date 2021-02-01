def reg(string, regex, replace=None):
    """

    Find and replace with regex

    Args:
        string  (str):      Text to search
        regex   (str):      Regex to search
        replace (str):      Replace text groups are replaced with \1 or $1

    Return (str | list):
        Returns the list with the found regex or a replaced string
    """

    from re import findall, sub

    if replace is None:
        return findall(regex, string)

    else:
        replace = sub(r'\$(\d+)', r'\\\1', replace)
        return sub(regex, replace, string)


def rsh(cmd):
	from subprocess import getstatusoutput
	return getstatusoutput(cmd)


def getSize(path_file):
    size = rsh(f'adb shell wc -c {path_file}')[1]
    size = reg(size, '\d+')[0]

    return int(size)

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

	regex = r'[A-Z]\S+'
	string = str(dic['self'])
	
	dic['self'] = reg(string, regex)[0]
	vals = tuple(dic.values())

	if tuple(dic)[0] != 'self':
		vals = vals[::-1]

	return vals


def SQL(database, act, args, modes='0123'):
    from sqlite3 import connect
	

    def create_table(table, row):
	    ex.execute(f'create table "{table}" ("{row}" TEXT)')


    def add_row(table, row, val):
        ex.execute(f'insert into {table}({row}) values("{val}")')
	

    def get_row(table, rows):
        while True:
            ex.execute(f'select {rows} from {table}')
            rows_list = ex.fetchall()
            if len(rows_list) > 0:
                return rows_list


    if '0' in modes:
        rsh(f'rm {database}')

    db = connect(database)
    ex = db.cursor()

    if '1' in modes:
        
        for t, r in [('Action', 'act'), ('Args', 'arg'), ('Result', 'result')]:
            create_table(t, r)

    if '2' in modes:
        add_row('Action', 'act', args[0])
        add_row('Action', 'act', act)

        for arg in args[1:]:
            add_row('Args', 'arg', arg)

    if '1' in modes or '2' in modes:
        db.commit()

    if '3' in modes:
        row = get_row('Result', 'result')[0][0]
        return eval(row)
