import pytesseract
from PIL import Image
import pandas as pd

# 画像からテキストを抽出
image = Image.open('table_image.png')
text = pytesseract.image_to_string(image)

# テキストを行ごとに分割し、リスト化
rows = text.split('\n')
data = [row.split() for row in rows if row]

# Pandasデータフレームに変換
df = pd.DataFrame(data)

# Excelファイルに書き込み
df.to_excel('output.xlsx', index=False)