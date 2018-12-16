# -*- coding: utf-8 -*-

import pytest

# 通常の引数で定義された関数でもシーケンスや辞書でまとめて渡せる
def sample_func(a, b, c, d, e):
  return a+b+c+d+e

# 可変長引数はタプル、辞書で受け取る
def spam(a, *B, **C):
  return str(a) + str(B) + str(C)

# (Python3系のみ)可変長引数の後ろにキーワード引数を書ける
def spam2(*args, default_arg='default'):
  return str(args) + default_arg + 'default'

# (Python3系のみ)アスタリスクのみを記述する場合、以降の引数はすべてキーワード引数で渡さなければならない
def spam3(arg1, *, keywordarg='default'):
  return str(arg1) + keywordarg

def test_call_function():
  # シーケンスとして渡す場合はリストでもタプルでもどちらでも可
  arg = 1
  args = [2, 3]
  kwargs = {'d': 4, 'e': 5}
  assert 15 == sample_func(arg, *args, **kwargs)
  targs = (2, 3)
  assert 15 == sample_func(arg, *targs, **kwargs)

  assert "1(2, 3){'d': 4, 'e': 5}" == spam(1, 2, 3, d=4, e=5)

  assert "(1, 2, 3, 4)setdefault" == spam2(1, 2, 3, 4, default_arg='set')

  assert "1default" == spam3(1)
  assert "1set" == spam3(1, keywordarg='set')
