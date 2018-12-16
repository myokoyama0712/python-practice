import pytest

def test_dict_operation():
  test_dict = {0: 'zero', 1: 'one', 2: 'two'}

  assert 'zero' == test_dict[0]

  with pytest.raises(KeyError):
    test_dict[-1]
  
  assert 'one' == test_dict.get(1)

  actual = test_dict.pop(2)
  assert 'two' == actual
  assert {0: 'zero', 1: 'one'} == test_dict
