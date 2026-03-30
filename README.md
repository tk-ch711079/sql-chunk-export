# SQL Chunk Export Tool

SQL Server（Azure SQL Database を含む）から大量データを効率的に抽出し、
1,000,000 行ごとに分割して CSV として保存する Python スクリプトです。

ODBC Driver 18 を使用して接続し、Pandas のチャンク処理を利用して
メモリ効率よくデータをエクスポートできます。

## 特徴
- SQL Server への ODBC 接続
- 任意の SQL を実行してデータ取得
- 1,000,000 行ごとに CSV を自動分割保存
- 途中から再開できるファイル番号指定
- 保存先フォルダを自動生成

## 必要なライブラリ
pip install pyodbc pandas

## 実行方法
python sql_chunk_export.py
