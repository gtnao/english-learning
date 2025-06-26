#!/usr/bin/env python3
"""
CSVファイルをAnki用に変換するスクリプト
"""

import csv
import os
import sys
from pathlib import Path


def convert_to_simple_anki(input_file, output_file):
    """シンプルな表裏カード形式に変換"""
    with open(input_file, 'r', encoding='utf-8') as f_in:
        reader = csv.DictReader(f_in)
        with open(output_file, 'w', encoding='utf-8', newline='') as f_out:
            writer = csv.writer(f_out)
            
            for row in reader:
                # フロント: 使用場面と和訳
                front = f"{row['使用場面']}\n\n「{row['例文（和訳）']}」"
                
                # バック: 英語表現
                back = f"{row['表現']}\n\n例: {row['例文（英語）']}"
                
                writer.writerow([front.strip(), back.strip()])
    
    print(f"✅ 変換完了: {output_file}")


def convert_to_detailed_anki(input_file, output_file):
    """詳細情報を含む形式に変換"""
    with open(input_file, 'r', encoding='utf-8') as f_in:
        reader = csv.DictReader(f_in)
        with open(output_file, 'w', encoding='utf-8', newline='') as f_out:
            writer = csv.writer(f_out)
            
            # ヘッダー行
            writer.writerow([
                'Expression', 'Example', 'Translation', 'Grammar', 
                'Usage', 'Casual', 'Formal', 'Mistakes', 'Notes'
            ])
            
            for row in reader:
                writer.writerow([
                    row['表現'],
                    row['例文（英語）'],
                    row['例文（和訳）'],
                    row['文法ポイント'],
                    row['使用場面'],
                    row['カジュアル版'],
                    row['フォーマル版'],
                    row['よくある間違い'],
                    row['備考']
                ])
    
    print(f"✅ 詳細版変換完了: {output_file}")


def convert_all_files():
    """全CSVファイルを変換"""
    base_dir = Path('.')  # 現在のディレクトリ（english-expressions内）
    output_dir = Path('anki_decks')
    output_dir.mkdir(exist_ok=True)
    
    for category in ['general', 'software-engineering']:
        category_dir = base_dir / category
        if not category_dir.exists():
            continue
            
        for csv_file in category_dir.glob('*.csv'):
            # シンプル版
            simple_output = output_dir / f"{csv_file.stem}_simple.csv"
            convert_to_simple_anki(csv_file, simple_output)
            
            # 詳細版
            detailed_output = output_dir / f"{csv_file.stem}_detailed.csv"
            convert_to_detailed_anki(csv_file, detailed_output)
    
    print("\n📚 Anki用ファイルの生成が完了しました！")
    print(f"出力先: {output_dir}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 個別ファイルの変換
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.csv', '_anki.csv')
        convert_to_simple_anki(input_file, output_file)
    else:
        # 全ファイルの変換
        convert_all_files()