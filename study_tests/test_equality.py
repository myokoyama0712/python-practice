# -*- coding: utf-8 -*-

def test_slice_equality():
  test_slice = [0, 1, 2, 3, 4, 5]
  expected = [0, 1, 2]
  assert id(expected) != id(test_slice[:3])
  assert expected == test_slice[:3]
