import functools
import jar.util

_identity = lambda x:x

class cookiejar:
    load = functools.partial(jar.util.reader, _identity)
    dump = functools.partial(jar.util.writer, _identity)
