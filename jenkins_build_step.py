import sys
import os

#jenkins exposes the workpace directory through env
sys.path.append(os.environ['WORKSPACE'])
import test_add_numbers

import unittest
suite = unittest.TestLoader().loadTestsFromModule(test_add_numbers)
unittest.TextTestRunner().run(suite)