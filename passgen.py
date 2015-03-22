#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import md5

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: ./passgen.py password'
    else:
        password = ' '.join(sys.argv[1:])
        print repr(md5.new(password).digest())