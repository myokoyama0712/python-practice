# -*- coding: utf-8 -*-

import pytest

# ジェネレータ関数
def fib():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a+b

def test_fib():
  # __next__()メソッドが呼び出されるたびにyield式までが実行され、yield式で指定された値を返す
  items = []
  for v in fib():
    items.append(v)
    if len(items) > 5:
      break
  assert [0, 1, 1, 2, 3, 5] == items

  # ジェネレータ関数はイテレータの一種であることを理解する
  items = []
  for v in fib():
    items.append(v)
    if len(items) > 5:
      break
  assert [0, 1, 1, 2, 3, 5] == items

# send()メソッドのテスト
# 再開待ちのジェネレータに値を創出する
# send()メソッドで指定した値は、yield式の値となる。
def gen(step):
  val = 0
  while True:
    val = val + step
    step = yield val  # send()メソッドで新しいstepを受け取る

def test_send():
  g = gen(3)
  assert 3 == g.__next__()
  assert 13 == g.send(10)
  assert 18 == g.send(5)

# throw()メソッドのテスト
# 再開待ちのジェネレータに、例外を送出する
def gen_error():
  for i in range(10):
    yield i

def test_throw():
  g = gen_error()
  actual = []
  with pytest.raises(ValueError):
    for v in g:
      actual.append(v)
      if v > 2:
        g.throw(ValueError('Invalid value'))
  assert [0, 1, 2, 3] == actual

# close()メソッドのテスト
# 再開待ちのジェネレータに、GeneratorExit例外を創出して、ジェネレータを正常終了する
def gen_close():
  for i in range(10):
    yield i

def test_close():
  g = gen_close()
  actual = []
  for v in g:
    actual.append(v)
    if v > 2:
      g.close()
  assert [0, 1, 2, 3] == actual
