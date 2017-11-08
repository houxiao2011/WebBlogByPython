#!/usr/bin/env python
# coding: utf-8


import config_default


class Dict(dict):
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def merge(defaults, override):
    r = {}
    for k, v in defaults.iteritems:
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]

    return r


def to_dict(d):
    D = Dict()
    for k, v in d.iteritems():
        D[k] = to_dict(v) if isinstance(v, dict) else v
    return D


configs = config_default.config

# try:
#     import config_override
#     configs = merge(configs, config_override.configs)
# except ImportError:
#     pass

configs = to_dict(configs)

if __name__ == '__main__':
    print configs
