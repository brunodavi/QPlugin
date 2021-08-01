def reg(string, regex, replace=None):
	from re import findall, sub

	if replace is None:
		return findall(regex, string)

	else:
		replace = sub(r'\$(\d+)', r'\\\1', replace)
		return sub(regex, replace, string)


def rsh(cmd):
	from subprocess import getstatusoutput
	return getstatusoutput(cmd)


def adb(cmd):
	return rsh(f'''adb shell """{cmd}"""''')[-1]


def b64(string):
	from base64 import b64encode
	string = str(string).encode('utf-8')
	return str(b64encode(string), 'utf-8')


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

def autodict(*args):
	from inspect import getouterframes, currentframe

	get_rid_of = ['autodict(', ',', ')', '\n']
	calling_code = getouterframes(currentframe())[1][4][0]
	calling_code = calling_code[calling_code.index('autodict'):]

	for garbage in get_rid_of:
		calling_code = calling_code.replace(garbage, '')

	var_names, var_values = calling_code.split(), args
	vars_list = zip(var_names, var_values)

	return { var_name: var_value for var_name, var_value in vars_list }
