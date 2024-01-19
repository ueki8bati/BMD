# BMD

## 目次
- [アプリ概要](#アプリ概要)
- [システム概要](#システム概要)
- [環境構築](#環境構築)
- [URL](#URL)

## アプリ概要
このアプリケーションは以下のものを含んでいます
- ブックマーク辞書アプリ

## システム概要
- 言語：Python 3.8~3.11
- フレームワーク：Django 4.2.7
- フロントエンド：HTML,CSS
- データベース：SQLite3(テスト環境)→Postgresql(本番環境)
- 本番環境：AWS EC2

## 環境構築

### プロジェクトをクローン
```
git clone -b dev git@github.com:ueki8bati/BMD.git
cd BMD
```

### 仮想環境の作成
```
# Windows
python -m venv myvenv
# Linux and OS X
python3 -m venv myvenv
```

### 仮想環境の起動
```
# Windows
myvenv\Scripts\activate
# Linux and OS X
source myvenv/bin/activate
```

### pipアップグレード
```
python -m pip install --upgrade pip
```

### ライブラリインストール
```
#開発環境
pip install -r requirements-dev.txt
#本番環境
pip install -r requirements.txt
```

### わかちがきのモデル追加
```
python -m unidic download
```

### ブランチを切る
```
新規に作る場合
git branch ブランチ名

もし過去にブランチを作成していて、同じブランチ名で作り直す場合
git branch -d ローカルブランチ名
git push origin --delete リモートブランチ名
git branch ブランチ名
```

### /BMDの配下に.envファイルを作成
```
#.envの中身
SECRET_KEY=django-insecure-%cf#お好きな英数字を適当に追加して
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS='127.0.0.1'
CSRF_TRUSTED_ORIGINS=""
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

### 本番環境更新用
```
git pull origin production
sudo systemctl restart gunicorn.service
sudo systemctl restart nginx
```

## URL
[BMD](https://bookmarkdictionary.com/)
