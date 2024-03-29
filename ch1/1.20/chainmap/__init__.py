#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import MutableMapping

"""
This ChainMap implementation is designated to compensate versions of Python that
do not have collections.ChainMap module-–namely, Python 2.7, Python 3.2, and
PyPy3 releases based on Python 3.2. For more information, please visit

    https://pypi.python.org/pypi/chainmap

"""
class ChainMap(MutableMapping):

    def __init__(self, *maps):
        if maps:
            self.maps = maps
        else:
            self.maps = [{}]

    def new_child(self, m=None):
        _start_dict = {} if m is None else m
        return ChainMap(_start_dict, *self.maps)

    @property
    def parents(self):
        return ChainMap(*self.maps[1:])

    def __getitem__(self, key):
        for mapping in self.maps:
            try:
                return mapping[key]
            except KeyError:
                pass
        self.__missing__(key)

    def __missing__(self, key):
        raise KeyError(key)

    def __setitem__(self, key, value):
        self.maps[0][key] = value

    def __delitem__(self, key):
        del self.maps[0][key]

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __iter__(self):
        """
        lazy implementation would have been better
        """
        _keys = self._all_keys()
        return iter(_keys)

    def _all_keys(self):
        _keys = []
        for m in self.maps:
            _keys.extend(m.keys())
        return list(set(_keys))

    def __len__(self):
        return len(self._all_keys())

    def __nonzero__(self):
        return any(self.maps)

    def items(self):
        return [(key, self[key]) for key in self._all_keys()]
