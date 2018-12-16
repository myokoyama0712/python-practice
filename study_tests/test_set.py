# -*- coding: utf-8 -*-

import pytest

def test_set_operation():
  test_set = {1, 3, 'abc'}
  test_set.add(1)
  assert {1, 3, 'abc'} == test_set

  test_set.remove(3)
  assert {1, 'abc'} == test_set

  with pytest.raises(KeyError):
    test_set.remove(3)

  test_set.discard(3)
  assert {1, 'abc'} == test_set
