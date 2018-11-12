# setup

```shell
pip install -r requirements.txt
```

# テスト方法

pytestでのテストファイルの名前

- `test_` を接頭辞とするファイル
- `test.py` を接尾辞とするファイル

実行方法

```shell
# すべて実行
pytest

# テストファイルを選択して実行
pytest test_capitalize.py
```

## フィクスチャ

フィクスチャ: 個別のテストが実行される前に走らせておきたいコードの設定

`@pytest.fixture` デコレータを用いる

フィクスチャにはdocstringを書くこと

## parametrized test

`@pytest.mark.parametrize()` デコレータを用いる
