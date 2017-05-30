# Copyright 2015 Cloudera Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# flake8: noqa

import itertools

import numpy as np

import sys
import six
from six import BytesIO, StringIO, string_types as py_string


PY2 = sys.version_info[0] == 2


import unittest

if not PY2:
    unicode_type = str
    def lzip(*x):
        return list(zip(*x))
    zip = zip
    zip_longest = itertools.zip_longest
    def dict_values(x):
        return list(x.values())
    from decimal import Decimal
    import unittest.mock as mock
    range = range
else:
    try:
        from cdecimal import Decimal
    except ImportError:
        from decimal import Decimal

    unicode_type = unicode
    lzip = zip
    zip = itertools.izip
    zip_longest = itertools.izip_longest

    def dict_values(x):
        return x.values()

    try:
        import mock  # mock is an optional dependency
    except ImportError:
        pass

    range = xrange

integer_types = six.integer_types + (np.integer,)
