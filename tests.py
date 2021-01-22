#!/usr/bin/env python3


import unittest
from w3c.tipos import Byte
class TestStringMethods(unittest.TestCase):

    def testGetTipo(self):
        tipoByte=Byte()
        self.assertEqual("byte", tipoByte.get_tipo())
        self.assertEqual("xsd:byte", tipoByte.get_tipo_con_prefijo())

if __name__ == '__main__':
    unittest.main()