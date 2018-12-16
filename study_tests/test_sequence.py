# -*- coding: utf-8 -*-

import pytest

def test_slice_function():
  test_slice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
  assert 0 in test_slice
  assert 10 not in test_slice
  assert 0 == min(test_slice)
  assert 9 == max(test_slice)
  assert 2 == test_slice.index(2)
  assert 2 == test_slice.count(0)
