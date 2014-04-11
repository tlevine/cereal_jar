def load(fp):
    chunk = ''
    for line in fp:
        if line.startswith('%%'):
            yield chunk
            chunk = ''
        else:
            chunk += line

def dump(obj, fp):
    new = True
    for item in obj:
        if not new:
            fp.write('\n%%\n')
        fp.write(obj)
        new = False
