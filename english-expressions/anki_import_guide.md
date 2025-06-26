# Ankiインポートガイド

## 🎯 現在のCSVをAnkiで使う方法

### 方法1: シンプルな表裏カード

1. **CSVの変換**
   ```python
   # convert_to_anki.py
   import csv
   import os

   def convert_to_anki(input_file, output_file):
       with open(input_file, 'r', encoding='utf-8') as f_in:
           reader = csv.DictReader(f_in)
           with open(output_file, 'w', encoding='utf-8', newline='') as f_out:
               writer = csv.writer(f_out)
               for row in reader:
                   # フロント: 日本語の状況
                   front = f"{row['使用場面']}<br><br>「{row['例文（和訳）']}」"
                   
                   # バック: 英語表現と詳細
                   back = f"""
                   <b>{row['表現']}</b><br><br>
                   例: {row['例文（英語）']}<br><br>
                   カジュアル: {row['カジュアル版']}<br>
                   フォーマル: {row['フォーマル版']}<br><br>
                   文法: {row['文法ポイント']}<br>
                   注意: {row['よくある間違い']}
                   """
                   
                   writer.writerow([front.strip(), back.strip()])
   ```

2. **Ankiでのインポート**
   - Ankiを開く
   - ファイル → インポート
   - CSVファイルを選択
   - 区切り文字: カンマ
   - フィールド1 → Front
   - フィールド2 → Back
   - 「HTMLを許可」にチェック

### 方法2: 多面的学習用カード

1. **カスタムノートタイプの作成**
   - ツール → ノートタイプを管理
   - 追加 → 基本（前面と背面）をクローン
   - フィールドを追加:
     - Expression（表現）
     - Example（例文）
     - Translation（和訳）
     - Grammar（文法）
     - Casual（カジュアル版）
     - Formal（フォーマル版）
     - Usage（使用場面）
     - Mistakes（よくある間違い）

2. **複数カードテンプレートの設定**

   **カード1: 和訳→英語**
   ```html
   {{Translation}}<br><br>
   使用場面: {{Usage}}
   ```
   
   **カード2: 穴埋め問題**
   ```html
   {{cloze:Example}}<br><br>
   ヒント: {{Grammar}}
   ```

   **カード3: フォーマリティ変換**
   ```html
   カジュアル版: {{Casual}}<br><br>
   これをフォーマルに言うと？
   ```

### 方法3: 自動変換スクリプト

```bash
#!/bin/bash
# convert_all_to_anki.sh

for category in general software-engineering; do
  for file in english-expressions/$category/*.csv; do
    python convert_to_anki.py "$file" "anki_decks/$(basename $file)"
  done
done
```

## 📱 モバイルアプリとの同期

1. AnkiWebアカウントを作成
2. デスクトップ版で同期
3. AnkiMobile（iOS）/AnkiDroid（Android）で同期

## 🎨 学習効率を上げるカスタマイズ

### タグの活用
```python
# カテゴリーごとにタグを追加
tags = f"english::{category}::{difficulty}"
writer.writerow([front, back, tags])
```

### 音声の追加
```python
# Google TTSで音声生成
from gtts import gTTS

def add_audio(expression):
    tts = gTTS(text=expression, lang='en')
    filename = f"audio/{expression.replace(' ', '_')}.mp3"
    tts.save(filename)
    return f"[sound:{filename}]"
```

### 画像の追加（使用場面のイメージ）
```html
<img src="situations/{{Usage}}.png">
```

## 🔧 トラブルシューティング

### 文字化け対策
- 必ずUTF-8エンコーディングで保存
- LibreOfficeを使用（Excelは避ける）

### インポートエラー
- 最初の行がヘッダーの場合はスキップ
- 空白フィールドがないか確認
- HTMLタグの閉じ忘れに注意

## 📊 推奨学習設定

### 新規カード
- 1日20枚（初級者）
- 1日30-50枚（中級者）

### 復習設定
- Easy bonus: 130%
- Interval modifier: 100%
- Maximum interval: 365日

### カスタムスケジュール
```
Again: 10分
Hard: 1日
Good: 3日
Easy: 7日
```

これで現在のCSVファイルを効果的にAnkiで活用できます！