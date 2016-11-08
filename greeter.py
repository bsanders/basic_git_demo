#! /usr/bin/env python
from __future__ import print_function

import sys

for name in sys.argv[1:]:
  print('hello {0}'.format(name.title()))
