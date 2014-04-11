import collections
import functools
import email, email.message

import jar.util

class cookiejar:
    _identity = lambda x:x
    load = functools.partial(jar.util.reader, self._identity)
    dump = functools.partial(jar.util.writer, self._identity)

class recordjar:
    @staticmethod
    def _dumps(obj):
        m = email.message.Message()
        for k, v in obj.items():
            m[k] = str(v)
        return m.as_string().rstrip('\n')

    @staticmethod
    def _loads(string):
        return collections.OrderedDict(email.message_from_string(string))

    load = functools.partial(jar.util.reader, self._loads)
    dump = functools.partial(jar.util.writer, self._dumps)
