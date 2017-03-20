# -*- coding: utf-8 -*-
# Created by WangTao on 2/3/17.
# Copyright © 2017年 WangTao. All rights reserved.

from __future__ import absolute_import, print_function, unicode_literals
import os
import sys
import re
import json

__version__ = '0.0.1'


class Envcfg(object):
    re_name = re.compile(r'[a-z][a-z0-9_]*')

    def get_config(self, config_name):
        if not self.re_name.match(config_name):
            error_msg = ('No module named {0}\n\nThe name of envvar module '
                         'should matched {1.pattern}')
            raise ImportError(error_msg.format(config_name, self.re_name))

        if config_name in sys.modules:
            return sys.modules[config_name]

        config = dict()
        sys.modules[config_name] = config
        config_name += '_'
        for raw_name, raw_value in os.environ.items():
            if raw_name.startswith(config_name) and raw_name != config_name:
                config[raw_name[len(config_name):]] = json.loads(raw_value)

        return config

    def clear_config(self, config_name):
        if not self.re_name.match(config_name):
            error_msg = ('No module named {0}\n\nThe name of envvar module '
                         'should matched {1.pattern}')
            raise ImportError(error_msg.format(config_name, self.re_name))

        if config_name in sys.modules:
            sys.modules.pop(config_name)

        config_name += '_'
        for raw_name, raw_value in os.environ.items():
            if raw_name.startswith(config_name):
                os.environ.pop(raw_name)

envcfg = Envcfg()
