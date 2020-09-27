def edfile(path, write=None, encoding='utf-8'):
	
	if write is None:
		f = open(path, 'r', encoding=encoding)
		r = f.read()
		f.close()
		return r
		
	else:
		f = open(path, 'w', encoding=encoding)
		f.write(write)
		f.close()

