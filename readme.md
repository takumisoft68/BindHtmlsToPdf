# Bind HTMLs to PDF

## 1. 概要

ディレクトリ内のすべてのHTMLファイルを結合して
１つのPDFに変換するツールです。

## 2. 特徴

- 複数のHTMLファイルをもとに1つのPDFファイルを作成します
- カレントディレクトリに出力します

## 3. 環境作成

1. Python 3.11.x をインストールしておく
    - 3.11.2 で動作確認しました
1. Pythonの仮想ディレクトリを作成する
    1. cd code
    1. python -m venv venv
    1. call venv\Scripts\activate.bat
    1. python -m pip install --upgrade pip
    1. python -m pip install -r requirements.txt
1. `wkhtmltopdf` を以下からダウンロードし、`(リポジトリをクローンしたフォルダ)\wkhtmltox\bin\wkhtmltopdf.exe` になるように展開する
    - [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)

## 5. 使い方

1. htmlの入ったフォルダを run.bat に渡してください
    - ドラッグ&ドロップでOK！
