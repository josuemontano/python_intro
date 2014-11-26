# -*- coding: utf-8 -*-
# Programación funcional
# Lección 7
# reduce

import functools
import operator


ans = functools.reduce(operator.mul, [1, 2, 3])
print(ans)
