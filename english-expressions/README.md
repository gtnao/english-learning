# Natural English for Business & Engineering

このプロジェクトは、日本人英語話者が「自然だけど失礼にならない」「プロフェッショナルだけど堅苦しくない」バランスの取れた英語を習得するための表現集です。ビジネスシーンとソフトウェア開発の現場で実際に使える1,000の表現を収録しています。

## 📚 概要

- **ビジネス英語**: 500個の日常業務・会議・メールで使える自然な表現
- **エンジニアリング英語**: 500個のソフトウェア開発・技術議論で使える専門表現
- **合計**: 1,000個の実用的な英語表現

## 🎯 対象レベル

- TOEICスコア 700-860レベル
- ビジネスで英語を使う必要がある方
- より自然で洗練された英語表現を身につけたい方

## 📁 ディレクトリ構造

```
english-expressions/
├── general/                  # 汎用表現（500個）
│   ├── 01_conversation_starters      # 会話の始め方・つなぎ方（35個）
│   ├── 02_opinions_thoughts          # 意見・考えの表現（35個）
│   ├── 03_information_exchange       # 情報のやり取り（35個）
│   ├── 04_problems_issues            # 問題・課題の扱い（35個）
│   ├── 05_time_process_management    # 時間・プロセス管理（30個）
│   ├── 06_relationships_social       # 人間関係・社交（30個）
│   ├── 07_emotions_reactions         # 感情・反応の表現（30個）
│   ├── 08_quantity_degree            # 数量・程度の表現（25個）
│   ├── 09_cause_reason_result        # 原因・理由・結果（30個）
│   ├── 10_judgment_evaluation        # 判断・評価（25個）
│   ├── 11_instructions_requests      # 指示・依頼・提案（30個）
│   ├── 12_explanation_description    # 説明・描写（25個）
│   ├── 13_discussion_negotiation     # 議論・交渉（25個）
│   ├── 14_email_documents            # メール・文書特有表現（25個）
│   ├── 15_presentations_briefings    # プレゼン・説明会（20個）
│   ├── 16_phone_video_calls          # 電話・ビデオ会議（15個）
│   ├── 17_cultural_considerations    # 文化的配慮のある表現（15個）
│   └── 18_practical_words_phrases    # 実用的な単語・フレーズ（80個）
│
└── software-engineering/      # ソフトウェアエンジニア向け（500個）
    ├── 01_design_patterns            # 設計パターン（25個）
    ├── 02_scalability_performance    # スケーラビリティ・パフォーマンス（25個）
    ├── 03_maintainability_extensibility # 保守性・拡張性（25個）
    ├── 04_architecture_tradeoffs     # アーキテクチャのトレードオフ（25個）
    ├── 05_code_improvements          # コード改善提案（30個）
    ├── 06_code_issues_questions      # コードの問題・質問（25個）
    ├── 07_alternative_solutions      # 代替案の提示（25個）
    ├── 08_algorithms_data_structures # アルゴリズムとデータ構造（30個）
    ├── 09_implementation_details     # 実装詳細（25個）
    ├── 10_specifications             # 仕様説明（25個）
    ├── 11_estimation_progress        # 見積もりと進捗報告（30個）
    ├── 12_risk_priority_deadline     # リスク・優先順位・締切（30個）
    ├── 13_troubleshooting_analysis   # トラブルシューティング・分析（30個）
    ├── 14_solutions_testing          # 解決策とテスト（30個）
    ├── 15_collaboration_knowledge_sharing # コラボレーションと知識共有（30個）
    ├── 16_best_practices_documentation # ベストプラクティスとドキュメント（30個）
    ├── 17_technology_evaluation      # 技術評価（30個）
    └── 18_migration_adoption         # 移行と採用（30個）
```

## 📝 各ファイルの形式

### Markdownファイル（.md）
- 詳細な解説付きの表現集
- 例文、文法解説、使用場面、注意点を含む
- 学習に最適な形式

### CSVファイル（.csv）
- データとして扱いやすい形式
- Anki等の学習アプリへのインポートに対応
- 一覧性の高い形式

## 🌟 特徴

### 中庸さの基準
- アカデミックすぎず、カジュアルすぎない
- ネイティブが聞いて「外国人だけど英語がちゃんとしている」と感じるレベル
- ビジネスカジュアルな服装に相当する言語レベル

### 実用性重視
- 実際の会話・メール・会議で頻出する表現
- 机上の空論ではなく、実際に使われている表現
- 地域差（米国/英国等）がある場合は注記付き

### 日本人学習者への配慮
- 日本語の発想から来る間違いを予防
- カタカナ英語との違いを明確化
- 敬語感覚をどう英語で表現するかの指針

## 📖 使い方

1. **体系的学習**: カテゴリー順に学習し、バランスよく表現を身につける
2. **場面別学習**: 必要な場面のカテゴリーから集中的に学習
3. **レベル別学習**: カジュアル版・フォーマル版を比較して適切なレベルを選択

## 💡 学習のコツ

1. **文法理解**: 各表現の文法解説を読み、「なぜそうなるのか」を理解
2. **間違い防止**: NGパターンを確認し、よくある間違いを回避
3. **実践練習**: 例文を参考に、自分の状況に合わせて応用

## 📱 Anki用データの生成

### 生成方法

1. **Pythonスクリプトの実行**
   ```bash
   cd english-expressions
   python3 convert_to_anki.py
   ```

2. **生成されるファイル**
   - `anki_decks/` ディレクトリに以下のファイルが生成されます：
     - `*_simple.csv`: シンプルな表裏カード（使用場面→英語表現）
     - `*_detailed.csv`: 全情報を含む詳細版

### Ankiへのインポート手順

1. **Ankiデスクトップ版を開く**
2. **ファイル → インポート**
3. **生成されたCSVファイルを選択**
4. **インポート設定**：
   - タイプ: 基本
   - フィールドの区切り: カンマ
   - フィールド1 → Front
   - フィールド2 → Back

### カテゴリー別の管理

サブデッキを作成して整理することを推奨：
```
Natural English::Business::Conversation Starters
Natural English::Engineering::Design Patterns
```

## 🚀 今後の展開

このプロジェクトは継続的に更新され、より実用的で学習しやすい形に進化していきます。フィードバックや追加してほしい表現があれば、ぜひお知らせください。

## ✅ 完成状況

- **汎用表現**: 全18カテゴリー（500表現）完成
- **ソフトウェアエンジニア向け表現**: 全18カテゴリー（500表現）完成
- **総計**: 1,000表現のコレクション完成

各カテゴリーには以下が含まれています：
- 詳細な文法解説と使用例
- カジュアル版・フォーマル版の比較
- 日本人が間違えやすいポイント
- 実践的な使用場面の説明

---

**Happy Learning! 📚✨**