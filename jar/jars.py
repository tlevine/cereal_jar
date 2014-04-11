import json
import functools
import jar.util

class cookiejar:
    _identity = lambda x:x
    load = functools.partial(jar.util.reader, self._identity)
    dump = functools.partial(jar.util.writer, self._identity)

class jsonjar:
    _dumps = lambda x: json.dumps(x, indent = 2, separators = (',', ': '))
    load = functools.partial(jar.util.reader, json.loads)
    dump = functools.partial(jar.util.writer, self._dump)
