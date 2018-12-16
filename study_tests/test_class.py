# -*- coding: utf-8 -*-

import pytest
import sys

class Spam:
  pass

# クラス属性付きのクラス
class Spam2:
  ham = 200
  
  def getHam(self):
    return self.ham

# コンストラクタ付きのクラス
class Spam3:
  def __init__(self, ham, egg):
    self.ham = ham
    self.egg = egg
  
  def getHam(self):
    return self.ham

  def getEgg(self):
    return self.egg

# デストラクタ付きのクラス
test_val = 'alive'
class Spam4:
  def __del__(self):
    global test_val
    test_val = 'dead'

# 基底クラス（objectクラスを継承）
class Base:
  def __init__(self, arg1):
    self.arg1 = arg1

  def spam(self):
    return 'Base.spam()'
  
  def ham(self):
    return 'Base.ham()'

  def getArg1(self):
    return self.arg1

# 派生クラス
class Derived(Base):
  def __init__(self, arg1, arg2):
    super().__init__(arg1)  # Base.__init__()を呼び出す
    self.arg2 = arg2

  # Base.spam()をオーバーライド
  def spam(self):
    return 'Derived.spam()' + self.ham()
  
  def getArg2(self):
    return self.arg2

# プロパティの利用
class Spam5:
  def __init__(self):
    self.__ham = 0  #　外部から直接参照できない
  
  @property     # hamプロパティのgetter定義
  def ham(self):
    return self.__ham
  
  @ham.setter   # hamプロパティのsetter定義
  def ham(self, value):
    self.__ham = value
  
  @ham.deleter  # hamプロパティのdeleter定義
  def ham(self):
    del self.__ham

# クラスメソッドデコレータ、スタティックメソッドデコレータ
class Spam6:
  cls_field = 'class field'

  def __init__(self):
    self.ins_field = 'instance field'

  def method(self):
    """通常のインスタンスメソッド"""
    return self.ins_field
  
  @classmethod
  def clsmethod(cls):
    """クラスメソッド"""
    return cls.cls_field
  
  # スタティックメソッドはクラスオブジェクトを引数に取らない
  @staticmethod
  def static_method(ham, egg):
    return ham+egg

# クラスデコレータ
# Pythonのバージョンをチェックするデコレータ
def py_version(major, minor, micro):
  def deco(cls):
    if (major, minor, micro) > sys.version_info[:3]:
      #raise RuntimeError('class {0!r} は Python {1}.{2}.{3}が必要です'.format(cls, major, minor, micro))
      raise RuntimeError()
    return cls
  return deco

# Python 3.7.0以上でのみ利用可能なクラス
#@py_version(3, 7, 0)
#class Spam7:
#  pass

def test_instance_operation():
  s = Spam()
  s.ham = 100
  assert 100 == s.ham

  # 属性の削除
  # 存在しない属性にアクセスするとAttributeErrorを発生する
  del s.ham
  with pytest.raises(AttributeError):
    s.ham

def test_class_field():
  s = Spam2()
  assert 200 == s.ham
  assert 200 == Spam2.ham

def test_constructor():
  s = Spam3('ham', 'egg')
  assert 'ham' == s.getHam()
  assert 'egg' == s.getEgg()

def test_destructor():
  s = Spam4()
  assert 'alive' == test_val
  del s # クラスインスタンスの解放はdel文で行う
  assert 'dead' == test_val

def test_inheritance():
  b = Base('arg1')
  d = Derived('arg1', 'arg2')
  assert 'Base.spam()' == b.spam()
  assert 'Base.ham()' == b.ham()
  assert 'arg1' == b.getArg1()
  assert 'Derived.spam()Base.ham()' == d.spam()
  assert 'Base.ham()' == d.ham()
  assert 'arg1' == d.getArg1()
  assert 'arg2' == d.getArg2()

def test_class_property():
  s = Spam5()
  # 直接参照できない
  with pytest.raises(AttributeError):
    s.__ham
  # s.hamは実際にはデコレータ付きメソッドだが、インスタンス属性のように扱える
  assert 0 == s.ham
  s.ham = 100
  assert 100 == s.ham

def test_class_method():
  s = Spam6()
  assert 'instance field' == s.method()
  assert 'class field' == Spam6.clsmethod()
  assert 'class field' == s.clsmethod() # クラスメソッドはインスタンス経由で呼び出しても良い

  assert 'hamegg' == Spam6.static_method('ham', 'egg')

def test_class_decorator():
  with pytest.raises(RuntimeError):
    # Python 3.7.0以上でのみ利用可能なクラス
    @py_version(3, 7, 0)
    class Spam7:
      pass
    Spam7()
