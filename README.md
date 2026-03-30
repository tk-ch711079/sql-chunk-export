## SQL Chunk Export Tool（SQLデータ分割エクスポートツール）
  →　SQL Server の大量データをチャンク分割して CSV にエクスポートするツール

## 概要
SQL Server（Azure SQL Database を含む）から大量データを効率的に抽出し、
1,000,000 行ごとに分割して CSV として保存する Python スクリプトです。

ODBC Driver 18 を使用して接続し、Pandas のチャンク処理を利用して
メモリ効率よくデータをエクスポートできます。

## 特徴
- SQL Server への ODBC 接続

## 出力例
sample_data_export/
 ├── output_part_001.csv
 ├── output_part_002.csv
 └── output_part_003.csv
- 任意の SQL を実行してデータ取得

## 動作確認済み環境
- Python 3.10
- Windows 10 / 11
- ODBC Driver 18 for SQL Server

- 1,000,000 行ごとに CSV を自動分割保存
- 途中から再開できるファイル番号指定
- 保存先フォルダを自動生成

## 必要なライブラリ
pip install pyodbc pandas

## 実行方法
python sql_chunk_export.py
