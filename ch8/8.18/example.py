#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
PROBLEM

You have a collection of generally useful methods that you would like to make
available for extending the functionality of other class definitions. However,
the classes where the methods might be added aren’t necessarily related to one
another via inheritance. Thus, you can’t just attach the methods to a common base
class.
"""


"""
DISCUSSION
"""


class LoggedMappingMixin(object):
    '''
    Add logging to get/set/delete operations for debugging.
    '''
    __slots__ = ()

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super(LoggedMappingMixin, self).__getitem__(key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super(LoggedMappingMixin, self).__setitem__(key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super(LoggedMappingMixin, self).__delitem__(key)


class SetOnceMappingMixin(object):
    '''
    Only allow a key to be set once.
    '''
    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' aready set')
        else:
            return super(SetOnceMappingMixin, self).__setitem__(key, value)


class StringKeysMappingMixin(object):
    '''
    Retrict keys to strings only
    '''
    def __setitem__(self, key, value):
        if isinstance(key, str):
            return super(StringKeysMappingMixin, self).__setitem__(key, value)
        else:
            raise TypeError('keys must be strings')


class LoggedDict(LoggedMappingMixin, dict):
    pass

d = LoggedDict()
d['x'] = 23
d['x']
del d['x']
print('')


from collections import defaultdict
class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass

d = SetOnceDefaultDict(list)
d['x'].append(2)
d['y'].append(3)
d['x'].append(10)
# d['x'] = 23


from collections import OrderedDict


class StringOrderedDict(StringKeysMappingMixin,
                        SetOnceMappingMixin,
                        OrderedDict):
    pass

d = StringOrderedDict()
d['x'] = 23
# d[42] = 10
# d['x'] = 42


"""
DISCUSSION
"""

try:
    # for Python 2
    from SimpleXMLRPCServer import SimpleXMLRPCServer
except ImportError:
    # for Python 3
    from xmlrpc.server import SimpleXMLRPCServer


try:
    # for Python 2
    from SocketServer import ThreadingMixIn
except ImportError:
    # for Python 3
    from soketserver import ThreadingMixIn


class ThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, key):
        print('Getting ' + str(key))
        return cls_getitem(self, key)

    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__
    return cls


@LoggedMapping
class LoggedDict2(dict):
    pass
