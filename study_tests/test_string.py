# -*- coding: utf-8 -*-

def test_int_transform():
  assert '0b1010' == bin(10)
  assert '0o12' == oct(10)
  assert '0xa' == hex(10)
