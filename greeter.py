#! /usr/bin/env python
from __future__ import print_function

import sys

if len(sys.argv) == 1:
  print('you did it wrong')
  sys.exit(1)
for name in sys.argv[1:]:
  print('hello {0}'.format(name.title()))
