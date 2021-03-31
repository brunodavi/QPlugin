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