import os
import pyodbc
import pandas as pd

# 接続情報（SQL認証）
# ※ 固有名詞はダミー値に置換
conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=sample-server.database.windows.net;"  # サーバ名（ダミー）
    "DATABASE=sample-database;"                   # データベース名（ダミー）
    "UID=sample-user;"                            # ユーザ名（ダミー）
    "PWD=sample-password"                         # パスワード（ダミー）
)

# 接続開始
conn = pyodbc.connect(conn_str)

# 保存先フォルダ（実行場所に作成される）
output_dir = os.path.join(os.getcwd(), "sample_data_export")
os.makedirs(output_dir, exist_ok=True)

# 途中から再開するためのSQL
# SampleDateInfoId が 100000000 以降を取得（ダミー値）
sql = """
SELECT *
FROM dbo.SampleDateInfo
WHERE SampleDateInfoId >= 100000000
ORDER BY SampleDateInfoId
"""

# 1ファイルあたりの行数
chunksize = 1000000

# 途中から再開するファイル番号（ダミー値）
start_file_index = 1

# 分割保存ループ
i = start_file_index
for chunk in pd.read_sql(sql, conn, chunksize=chunksize):
    filename = os.path.join(output_dir, f"output_part_{i:03}.csv")
    print(f"Saving {filename} ...")
    chunk.to_csv(filename, index=False)
    i += 1

print("全件保存完了")

