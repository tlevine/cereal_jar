import collections
import functools
import email, email.message

import jar.util

def _dumps(obj):
    m = email.message.Message()
    for k, v in obj.items():
        m[k] = str(v)
    return m.as_string().rstrip('\n')

def _loads(string):
    return collections.OrderedDict(email.message_from_string(string))

class recordjar:
    load = functools.partial(jar.util.reader, _loads)
    dump = functools.partial(jar.util.writer, _dumps)
