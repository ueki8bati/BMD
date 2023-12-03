# BMD

## 目次
- [アプリ概要](#アプリ概要)
- [システム概要](#システム概要)
- [環境構築](#環境構築)
- [URL](#URL)

## アプリ概要
このアプリケーションは以下のものを含んでいます
- ブックマーク辞書アプリ(作成中)
## システム概要
- 言語：Python 3.8~3.11
- フレームワーク：Django 4.2.7
- フロントエンド：HTML,CSS
- データベース：SQLite3(テスト環境)→Postgresql(本番環境)
- 本番環境：AWS EC2

## 環境構築
### 仮想環境の作成
```
# Windows
python -m venv 仮想環境名
# Linux and OS X
python3 -m venv 仮想環境名
```
### 仮想環境の起動
```
# Windows
仮想環境名\Scripts\activate
# Linux and OS X
source 仮想環境名/bin/activate
```

### pipアップグレード
```
python -m pip install --upgrade pip
```

### ライブラリインストール
```
pip install -r requirements-dev.txt
```

### わかちがきのモデル追加
```
python -m unidic download
```

### モデルのマイグレート
```
python manage.py migrate
```

### スーパーアカウントの作成
```
python manage.py createsuperuser
```

### Webサーバー起動
```
python manage.py runserver
```

## URL
[BMD](http://13.236.93.180:8000/)
