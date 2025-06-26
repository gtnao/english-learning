# Best Practices & Documentation / ベストプラクティス・文書化

設計原則、コーディング規約、文書化の重要性、品質向上のためのベストプラクティスに関する表現を収録。

---

## 1. Let's follow the principle of least surprise

### 例文

- **Context**: APIやインターフェース設計で直感的な動作を提案する場面
- **A**: "Should the delete method return the deleted item or just a success status?"
- **B**: "Let's follow the principle of least surprise. Most APIs return the deleted item, so users will expect that."

### 和訳

「最小驚き原則に従いましょう」という設計哲学の適用。ユーザーの期待に沿った直感的な設計を推奨。

### 文法解説

- **基本構造**: Let's + follow + the principle of + 名詞
- **なぜこの形?**: 確立された設計原則を参照
- **省略・変形**:
  - よりカジュアル: "Let's keep it intuitive"
  - よりフォーマル: "We should adhere to established conventions"

### 使用場面

- API設計
- UI/UX決定
- ライブラリのインターフェース設計

### 似た表現との違い

- **"Let's be consistent"**: より一般的
- **"Follow standards"**: 外部基準への準拠

### NGパターン

❌ "Let's follow principle of least surprise"
→ 定冠詞が必要（特定の原則）

### 自然さUPのコツ

💡 他のシステムでの一般的な実装例を挙げると説得力が増す

---

## 2. This adheres to SOLID principles

### 例文

- **Context**: オブジェクト指向設計の良さを説明する場面
- **A**: "Why did you split this class into three separate ones?"
- **B**: "This adheres to SOLID principles. Each class now has a single responsibility."

### 和訳

「これはSOLID原則に準拠しています」という設計品質の説明。確立された設計原則に基づく実装であることを示す。

### 文法解説

- **基本構造**: This + adheres to + 名詞
- **なぜこの形?**: "adhere to"で「準拠する」を表現
- **省略・変形**:
  - よりカジュアル: "This follows SOLID"
  - よりフォーマル: "This implementation conforms to SOLID principles"

### 使用場面

- コードレビュー
- 設計説明
- リファクタリングの根拠

### 似た表現との違い

- **"This uses SOLID"**: 使用と準拠の違い
- **"This is SOLID"**: 曖昧すぎる

### NGパターン

❌ "This adheres SOLID principles"
→ toが必要（句動詞）

### 自然さUPのコツ

💡 どの原則（SRP、OCP等）に特に該当するか具体的に示す

---

## 3. Let's document the why, not just the what

### 例文

- **Context**: コメントやドキュメントの書き方について議論する場面
- **A**: "Should I add comments explaining what this function does?"
- **B**: "Let's document the why, not just the what. Explain why we chose this algorithm."

### 和訳

「何をするかだけでなく、なぜそうするかを文書化しましょう」という深い理解を促す文書化方針。意図や背景の重要性を強調。

### 文法解説

- **基本構造**: Let's + document + the why + not just + the what
- **なぜこの形?**: 疑問詞を名詞化して対比
- **省略・変形**:
  - よりカジュアル: "Explain why, not what"
  - よりフォーマル: "Documentation should capture rationale"

### 使用場面

- コードコメントの方針
- 設計文書の作成
- アーキテクチャ決定記録

### 似た表現との違い

- **"Add more comments"**: 量的なアプローチ
- **"Document everything"**: 焦点が不明確

### NGパターン

❌ "Let's document why, not just what"
→ 冠詞で名詞化が必要

### 自然さUPのコツ

💡 良い例と悪い例を示すと理解しやすい

---

## 4. We should establish coding conventions

### 例文

- **Context**: チーム内でコーディング規約を定める提案
- **A**: "Everyone's code style is different. It's hard to read."
- **B**: "We should establish coding conventions. Consistent style improves maintainability."

### 和訳

「コーディング規約を確立すべきです」という標準化の提案。一貫性のあるコードベースで保守性を向上。

### 文法解説

- **基本構造**: We + should + establish + 名詞
- **なぜこの形?**: shouldで推奨、establishで「確立する」
- **省略・変形**:
  - よりカジュアル: "Let's agree on a style guide"
  - よりフォーマル: "We need to implement standardized coding practices"

### 使用場面

- 新プロジェクトの立ち上げ
- コードレビューの基準作り
- チーム品質向上

### 似た表現との違い

- **"Let's use a linter"**: ツールに焦点
- **"Follow best practices"**: 具体性に欠ける

### NGパターン

❌ "We should establish the coding conventions"
→ 一般的な概念なので冠詞不要

### 自然さUPのコツ

💡 既存のスタイルガイド（Airbnb等）を参考にすると効率的

---

## 5. This is self-documenting code

### 例文

- **Context**: 明確な変数名や関数名でコメントが不要なコードを評価する場面
- **A**: "Should I add comments to explain this method?"
- **B**: "This is self-documenting code. The method name 'calculateMonthlyCompoundInterest' says it all."

### 和訳

「これは自己文書化コードです」という高品質コードの評価。コード自体が説明となる理想的な状態。

### 文法解説

- **基本構造**: This + is + self-documenting + code
- **なぜこの形?**: 複合形容詞で特性を表現
- **省略・変形**:
  - よりカジュアル: "The code explains itself"
  - よりフォーマル: "The implementation exhibits self-explanatory characteristics"

### 使用場面

- コードレビューでの称賛
- リファクタリングの成果
- ベストプラクティスの例示

### 似た表現との違い

- **"This is clean code"**: より一般的
- **"No comments needed"**: 否定的な表現

### NGパターン

❌ "This is a self-documenting code"
→ 不可算名詞なので冠詞不要

### 自然さUPのコツ

💡 具体的にどの部分が分かりやすいか指摘すると学習になる

---

## 6. Let's maintain a single source of truth

### 例文

- **Context**: データや設定の重複を避ける設計を提案する場面
- **A**: "The same configuration is defined in three different files."
- **B**: "Let's maintain a single source of truth. All configs should reference one master file."

### 和訳

「単一の真実の源を維持しましょう」というデータ管理の原則。重複や矛盾を防ぐ重要な設計方針。

### 文法解説

- **基本構造**: Let's + maintain + a + single source of truth
- **なぜこの形?**: 確立された用語をそのまま使用
- **省略・変形**:
  - よりカジュアル: "Keep it in one place"
  - よりフォーマル: "We should centralize authoritative data"

### 使用場面

- 設定管理
- データベース設計
- ドキュメント管理

### 似た表現との違い

- **"Avoid duplication"**: より一般的
- **"Centralize everything"**: 範囲が広すぎる

### NGパターン

❌ "Let's maintain single source of truth"
→ 冠詞が必要

### 自然さUPのコツ

💡 どこを真実の源とするか明確に定義すると実践的

---

## 7. We're following DRY principles here

### 例文

- **Context**: コードの重複を避けた実装を説明する場面
- **A**: "Why extract this logic into a separate function?"
- **B**: "We're following DRY principles here. Don't Repeat Yourself - this logic is used in three places."

### 和訳

「ここではDRY原則に従っています」という設計思想の説明。コードの重複を避けて保守性を高める。

### 文法解説

- **基本構造**: We're + following + 名詞 + here
- **なぜこの形?**: 現在進行形で継続的な実践を表現
- **省略・変形**:
  - よりカジュアル: "We don't repeat code"
  - よりフォーマル: "We adhere to the Don't Repeat Yourself principle"

### 使用場面

- リファクタリングの説明
- コードレビュー
- 設計決定の根拠

### 似た表現との違い

- **"No duplication"**: 結果のみ
- **"Reuse code"**: 手段のみ

### NGパターン

❌ "We follow DRY principle here"
→ 複数形principlesが一般的

### 自然さUPのコツ

💡 DRYの頭文字を展開して説明すると親切

---

## 8. Let's add meaningful commit messages

### 例文

- **Context**: コミットメッセージの品質改善を提案する場面
- **A**: "I usually just write 'fix' or 'update' in commits."
- **B**: "Let's add meaningful commit messages. They're crucial for understanding project history."

### 和訳

「意味のあるコミットメッセージを追加しましょう」という履歴管理の改善提案。将来の理解のために重要。

### 文法解説

- **基本構造**: Let's + add + 形容詞 + 複数名詞
- **なぜこの形?**: meaningfulで質を強調
- **省略・変形**:
  - よりカジュアル: "Write better commit messages"
  - よりフォーマル: "We should implement descriptive version control annotations"

### 使用場面

- チーム規約の制定
- コードレビュー
- 新人教育

### 似た表現との違い

- **"Add comments"**: コミットとコメントの混同
- **"Write something"**: 具体性に欠ける

### NGパターン

❌ "Let's add meaningful commit message"
→ 通常複数形で扱う

### 自然さUPのコツ

💡 良いコミットメッセージの例を示すと実践しやすい

---

## 9. This follows the convention over configuration approach

### 例文

- **Context**: デフォルト設定を活用したフレームワーク使用を説明する場面
- **A**: "Why don't we need to configure all these settings?"
- **B**: "This follows the convention over configuration approach. The framework provides sensible defaults."

### 和訳

「これは設定より規約のアプローチに従っています」という設計哲学の説明。明示的な設定を最小限に抑える。

### 文法解説

- **基本構造**: This + follows + the + 名詞 + approach
- **なぜこの形?**: 確立された設計原則への言及
- **省略・変形**:
  - よりカジュアル: "It uses smart defaults"
  - よりフォーマル: "This implements implicit configuration paradigm"

### 使用場面

- フレームワーク選定
- 設定設計
- 開発効率化の説明

### 似た表現との違い

- **"Less configuration"**: 原則でなく結果
- **"Use defaults"**: 理由が不明

### NGパターン

❌ "This follows convention over configuration approach"
→ 定冠詞が必要

### 自然さUPのコツ

💡 どの規約を使っているか具体例を示すと理解しやすい

---

## 10. Let's implement proper error handling

### 例文

- **Context**: エラー処理の改善を提案する場面
- **A**: "The app just crashes when something goes wrong."
- **B**: "Let's implement proper error handling. Users should see helpful messages, not stack traces."

### 和訳

「適切なエラーハンドリングを実装しましょう」という品質向上の提案。ユーザー体験と診断性の両立。

### 文法解説

- **基本構造**: Let's + implement + 形容詞 + 名詞
- **なぜこの形?**: properで「適切な」を強調
- **省略・変形**:
  - よりカジュアル: "Let's handle errors better"
  - よりフォーマル: "We should establish comprehensive exception management"

### 使用場面

- コードレビュー
- 品質改善
- ユーザビリティ向上

### 似た表現との違い

- **"Catch all errors"**: 安直なアプローチ
- **"Add try-catch"**: 手段のみ

### NGパターン

❌ "Let's implement the proper error handling"
→ 一般的な概念なので定冠詞不要

### 自然さUPのコツ

💡 どのレベルでどう処理するか階層を示すと具体的

---

## 11. This violates the separation of concerns

### 例文

- **Context**: 責務が混在したコードの問題を指摘する場面
- **A**: "I put the database queries directly in the UI components."
- **B**: "This violates the separation of concerns. Business logic shouldn't be mixed with presentation."

### 和訳

「これは関心の分離に違反しています」という設計問題の指摘。各層の責任を明確に分けるべきという原則。

### 文法解説

- **基本構造**: This + violates + the + 名詞
- **なぜこの形?**: violateで原則違反を表現
- **省略・変形**:
  - よりカジュアル: "Don't mix these things"
  - よりフォーマル: "This breaches architectural boundaries"

### 使用場面

- コードレビューでの指摘
- アーキテクチャ議論
- リファクタリング提案

### 似た表現との違い

- **"This is wrong"**: 具体性に欠ける
- **"Bad design"**: 建設的でない

### NGパターン

❌ "This violates separation of concerns"
→ 定冠詞が必要（特定の原則）

### 自然さUPのコツ

💡 どう分離すべきか改善案を示すと建設的

---

## 12. Let's write idempotent operations

### 例文

- **Context**: 複数回実行しても安全な処理の設計を提案する場面
- **A**: "What if the request is sent twice due to network issues?"
- **B**: "Let's write idempotent operations. Multiple executions should produce the same result."

### 和訳

「冪等な操作を書きましょう」という堅牢な設計の提案。重複実行に対して安全なシステムを構築。

### 文法解説

- **基本構造**: Let's + write + 形容詞 + 名詞
- **なぜこの形?**: 技術用語を形容詞として使用
- **省略・変形**:
  - よりカジュアル: "Make it safe to retry"
  - よりフォーマル: "We should ensure operational idempotency"

### 使用場面

- API設計
- 分散システム開発
- エラーリトライ設計

### 似た表現との違い

- **"Handle duplicates"**: 事後対応的
- **"Prevent double execution"**: 方法が限定的

### NGパターン

❌ "Let's write idempotent operation"
→ 通常複数形で扱う

### 自然さUPのコツ

💡 PUT vs POSTなど具体例で説明すると理解しやすい

---

## 13. We need to refactor, not rewrite

### 例文

- **Context**: 既存コードの改善方法について議論する場面
- **A**: "This code is a mess. Should we start from scratch?"
- **B**: "We need to refactor, not rewrite. Incremental improvements are less risky."

### 和訳

「書き直しではなくリファクタリングが必要です」という現実的なアプローチ。段階的改善でリスクを最小化。

### 文法解説

- **基本構造**: We need to + 動詞 + not + 動詞
- **なぜこの形?**: 対比構造で選択を明確化
- **省略・変形**:
  - よりカジュアル: "Let's clean it up gradually"
  - よりフォーマル: "Incremental refactoring is preferable to complete reconstruction"

### 使用場面

- レガシーコード改善
- 技術的負債の解消
- プロジェクト計画

### 似た表現との違い

- **"Fix the code"**: 具体性に欠ける
- **"Improve it"**: 方法が不明

### NGパターン

❌ "We need refactoring, not rewriting"
→ to不定詞が必要

### 自然さUPのコツ

💡 リファクタリングのステップを示すと実行可能性が高まる

---

## 14. Let's enforce this at the API level

### 例文

- **Context**: 制約や検証をどこで実装するか議論する場面
- **A**: "Should each client validate the input format?"
- **B**: "Let's enforce this at the API level. Centralized validation ensures consistency."

### 和訳

「これをAPIレベルで強制しましょう」という一元的な制御の提案。クライアント依存でなくサーバー側で保証。

### 文法解説

- **基本構造**: Let's + enforce + this + at the + レベル
- **なぜこの形?**: enforceで「強制する」、at the levelで階層指定
- **省略・変形**:
  - よりカジュアル: "Put the check in the API"
  - よりフォーマル: "Implementation should occur at the API layer"

### 使用場面

- バリデーション設計
- セキュリティ実装
- アーキテクチャ決定

### 似た表現との違い

- **"Add validation"**: 場所が不明
- **"Check inputs"**: 強制力が弱い

### NGパターン

❌ "Let's enforce this on the API level"
→ at が適切（レベル・層を示す）

### 自然さUPのコツ

💡 なぜそのレベルが適切か理由を添えると説得力がある

---

## 15. This is a code smell

### 例文

- **Context**: 問題の兆候となるコードパターンを指摘する場面
- **A**: "This method is 500 lines long but it works."
- **B**: "This is a code smell. Long methods often hide multiple responsibilities."

### 和訳

「これはコードの臭いです」という潜在的問題の指摘。直接的なバグでなくても改善すべきサイン。

### 文法解説

- **基本構造**: This + is + a + code smell
- **なぜこの形?**: 確立された技術用語
- **省略・変形**:
  - よりカジュアル: "This doesn't feel right"
  - よりフォーマル: "This exhibits anti-pattern characteristics"

### 使用場面

- コードレビュー
- リファクタリング候補の特定
- 教育的な指摘

### 似た表現との違い

- **"This is bad code"**: 直接的すぎる
- **"This has issues"**: 具体性に欠ける

### NGパターン

❌ "This is code smell"
→ 冠詞が必要

### 自然さUPのコツ

💡 どんな問題につながる可能性があるか説明すると教育的

---

## 16. Let's keep the interface stable

### 例文

- **Context**: 後方互換性を保ちながら機能を拡張する議論
- **A**: "We need to change the API response format for new features."
- **B**: "Let's keep the interface stable. We can add new fields without breaking existing clients."

### 和訳

「インターフェースを安定に保ちましょう」という互換性重視の方針。既存ユーザーへの影響を最小化。

### 文法解説

- **基本構造**: Let's + keep + the + 名詞 + 形容詞
- **なぜこの形?**: keep + 目的語 + 形容詞で状態維持
- **省略・変形**:
  - よりカジュアル: "Don't break the API"
  - よりフォーマル: "Interface stability must be maintained"

### 使用場面

- API設計
- ライブラリ開発
- バージョニング戦略

### 似た表現との違い

- **"Don't change it"**: 進化を否定
- **"Be careful"**: 具体性に欠ける

### NGパターン

❌ "Let's keep interface stable"
→ 特定のインターフェースなので冠詞必要

### 自然さUPのコツ

💡 どのように拡張するか具体例を示すと実践的

---

## 17. We're accumulating technical debt here

### 例文

- **Context**: 短期的な解決策の長期的な影響を警告する場面
- **A**: "Let's just add another if statement to fix this quickly."
- **B**: "We're accumulating technical debt here. We should refactor this properly soon."

### 和訳

「ここで技術的負債を蓄積しています」という将来のリスクの指摘。一時的な解決策の代償を認識。

### 文法解説

- **基本構造**: We're + accumulating + 名詞 + here
- **なぜこの形?**: 現在進行形で継続的な蓄積を表現
- **省略・変形**:
  - よりカジュアル: "This will cause problems later"
  - よりフォーマル: "This approach incurs technical debt"

### 使用場面

- 設計決定の議論
- スプリント計画
- リファクタリング提案

### 似た表現との違い

- **"This is hacky"**: 価値判断的
- **"Quick and dirty"**: 肯定的なニュアンスも含む

### NGパターン

❌ "We're accumulating the technical debt"
→ 一般的な概念なので冠詞不要

### 自然さUPのコツ

💡 いつ返済する計画か言及すると責任感が示せる

---

## 18. Let's add comprehensive logging

### 例文

- **Context**: システムの可観測性を向上させる提案
- **A**: "It's hard to debug production issues without visibility."
- **B**: "Let's add comprehensive logging. We need to track user actions and system states."

### 和訳

「包括的なロギングを追加しましょう」という診断性向上の提案。問題解決に必要な情報を事前に収集。

### 文法解説

- **基本構造**: Let's + add + 形容詞 + 動名詞
- **なぜこの形?**: comprehensiveで網羅性を強調
- **省略・変形**:
  - よりカジュアル: "Add more logs"
  - よりフォーマル: "We should implement extensive instrumentation"

### 使用場面

- 本番環境の準備
- トラブルシューティング改善
- 監視体制の構築

### 似た表現との違い

- **"Log everything"**: 過剰で非効率
- **"Add debug info"**: 開発環境限定の印象

### NGパターン

❌ "Let's add comprehensive loggings"
→ loggingは不可算名詞

### 自然さUPのコツ

💡 何をログに記録すべきか具体的なカテゴリを示す

---

## 19. This needs proper documentation

### 例文

- **Context**: 複雑な機能やAPIに文書が不足している指摘
- **A**: "The integration is working, but it's pretty complex."
- **B**: "This needs proper documentation. Future developers won't understand the design decisions."

### 和訳

「これには適切な文書化が必要です」という保守性への懸念。将来の開発者のために知識を残す重要性。

### 文法解説

- **基本構造**: This + needs + 形容詞 + 名詞
- **なぜこの形?**: needsで必要性を表現
- **省略・変形**:
  - よりカジュアル: "We should document this"
  - よりフォーマル: "Comprehensive documentation is required"

### 使用場面

- 複雑な実装の完了時
- APIリリース前
- コードレビュー

### 似た表現との違い

- **"Add comments"**: 範囲が限定的
- **"Write docs"**: 品質への言及なし

### NGパターン

❌ "This needs a proper documentation"
→ 不可算名詞なので冠詞不要

### 自然さUPのコツ

💡 どのような文書が必要か（API仕様、設計書等）明確にする

---

## 20. Let's version this properly

### 例文

- **Context**: APIやライブラリのバージョン管理戦略を議論する場面
- **A**: "How should we handle breaking changes?"
- **B**: "Let's version this properly. We'll use semantic versioning to communicate changes clearly."

### 和訳

「これを適切にバージョン管理しましょう」という体系的な管理の提案。変更の影響を明確に伝える仕組み。

### 文法解説

- **基本構造**: Let's + version + this + 副詞
- **なぜこの形?**: versionを動詞として使用
- **省略・変形**:
  - よりカジュアル: "Let's use version numbers"
  - よりフォーマル: "We should implement systematic versioning"

### 使用場面

- ライブラリ開発
- API管理
- リリース戦略

### 似た表現との違い

- **"Number the releases"**: 体系的でない
- **"Track changes"**: バージョニングと異なる

### NGパターン

❌ "Let's do versioning properly"
→ 動詞形の方が簡潔

### 自然さUPのコツ

💡 セマンティックバージョニング（major.minor.patch）を例示

---

## 21. We should deprecate this gracefully

### 例文

- **Context**: 古い機能を段階的に廃止する計画を議論する場面
- **A**: "This old API endpoint is rarely used now."
- **B**: "We should deprecate this gracefully. Give users time to migrate with clear warnings."

### 和訳

「これを優雅に非推奨にすべきです」という段階的廃止の提案。利用者に配慮した移行期間を設ける。

### 文法解説

- **基本構造**: We should + deprecate + this + 副詞
- **なぜこの形?**: gracefullyで方法の質を表現
- **省略・変形**:
  - よりカジュアル: "Let's phase this out slowly"
  - よりフォーマル: "Systematic deprecation process is required"

### 使用場面

- API廃止計画
- レガシー機能の整理
- 破壊的変更の管理

### 似た表現との違い

- **"Remove this"**: 即座で配慮なし
- **"Stop supporting"**: プロセスが不明

### NGパターン

❌ "We should deprecate this graceful"
→ 副詞形が必要

### 自然さUPのコツ

💡 具体的な廃止スケジュールを提案すると実践的

---

## 22. Let's optimize for readability

### 例文

- **Context**: パフォーマンスと可読性のトレードオフを議論する場面
- **A**: "This clever one-liner is 10% faster than the verbose version."
- **B**: "Let's optimize for readability. The performance gain isn't worth the complexity."

### 和訳

「可読性を最適化しましょう」という保守性重視の方針。わずかな性能向上より理解しやすさを優先。

### 文法解説

- **基本構造**: Let's + optimize + for + 名詞
- **なぜこの形?**: optimize forで「〜向けに最適化」
- **省略・変形**:
  - よりカジュアル: "Make it easy to read"
  - よりフォーマル: "Prioritize code comprehensibility"

### 使用場面

- コードレビュー
- リファクタリング方針
- チーム規約

### 似た表現との違い

- **"Make it readable"**: 最適化の観点なし
- **"Simplify this"**: 必ずしも可読性向上でない

### NGパターン

❌ "Let's optimize readability"
→ forが必要（最適化の対象）

### 自然さUPのコツ

💡 可読性の具体的な改善点を示すと説得力がある

---

## 23. This introduces unnecessary complexity

### 例文

- **Context**: 過度に複雑な解決策に対して懸念を表明する場面
- **A**: "I created a factory pattern for creating these simple objects."
- **B**: "This introduces unnecessary complexity. A simple constructor would suffice."

### 和訳

「これは不必要な複雑さを導入します」という過剰設計への警告。シンプルな解決策の重要性を指摘。

### 文法解説

- **基本構造**: This + introduces + 形容詞 + 名詞
- **なぜこの形?**: introduceで「新たに持ち込む」
- **省略・変形**:
  - よりカジュアル: "This is overkill"
  - よりフォーマル: "This adds unwarranted architectural complexity"

### 使用場面

- 設計レビュー
- オーバーエンジニアリング防止
- YAGNI原則の適用

### 似た表現との違い

- **"Too complex"**: 理由が不明
- **"Over-designed"**: より批判的

### NGパターン

❌ "This introduces an unnecessary complexity"
→ 抽象概念なので冠詞不要

### 自然さUPのコツ

💡 よりシンプルな代替案を提示すると建設的

---

## 24. Let's fail gracefully

### 例文

- **Context**: エラー時の振る舞いを設計する場面
- **A**: "What happens if the external service is down?"
- **B**: "Let's fail gracefully. Show cached data with a warning instead of error screens."

### 和訳

「優雅に失敗しましょう」という耐障害性の設計。エラー時でも可能な限りサービスを継続。

### 文法解説

- **基本構造**: Let's + fail + 副詞
- **なぜこの形?**: gracefullyで失敗の仕方を修飾
- **省略・変形**:
  - よりカジュアル: "Handle errors nicely"
  - よりフォーマル: "Implement graceful degradation"

### 使用場面

- エラーハンドリング設計
- フォールバック戦略
- ユーザー体験の最適化

### 似た表現との違い

- **"Catch errors"**: 処理方法が不明
- **"Don't crash"**: 最低限の要求

### NGパターン

❌ "Let's fail graceful"
→ 副詞形が必要

### 自然さUPのコツ

💡 具体的なフォールバック動作を例示すると理解しやすい

---

## 25. We need to dogfood our own API

### 例文

- **Context**: 自社製品を自ら使用して品質を確認する提案
- **A**: "How do we know if our API is really developer-friendly?"
- **B**: "We need to dogfood our own API. Let's build an internal tool using it."

### 和訳

「自分たちのAPIをドッグフーディングする必要があります」という実践的な品質保証。自ら使うことで問題を発見。

### 文法解説

- **基本構造**: We need to + dogfood + our own + 名詞
- **なぜこの形?**: dogfoodを動詞として使用
- **省略・変形**:
  - よりカジュアル: "Let's use our own stuff"
  - よりフォーマル: "We should consume our own services"

### 使用場面

- API品質向上
- 製品改善
- 開発者体験の検証

### 似た表現との違い

- **"Test our API"**: 実使用でない
- **"Try it out"**: 体系的でない

### NGパターン

❌ "We need to do dogfooding"
→ 動詞形の方が自然

### 自然さUPのコツ

💡 どのようなプロジェクトで使用するか具体的に提案

---

## 26. Let's implement progressive enhancement

### 例文

- **Context**: 基本機能から段階的に機能を追加する設計を提案する場面
- **A**: "Not all users have the latest browsers with JavaScript enabled."
- **B**: "Let's implement progressive enhancement. Start with basic HTML and layer on features."

### 和訳

「プログレッシブエンハンスメントを実装しましょう」という包括的な設計アプローチ。すべてのユーザーに基本機能を保証。

### 文法解説

- **基本構造**: Let's + implement + 名詞
- **なぜこの形?**: Web開発の確立された手法
- **省略・変形**:
  - よりカジュアル: "Start simple, add features"
  - よりフォーマル: "We should adopt a progressive enhancement strategy"

### 使用場面

- フロントエンド設計
- アクセシビリティ対応
- 段階的な機能追加

### 似た表現との違い

- **"Support old browsers"**: 後ろ向きな印象
- **"Graceful degradation"**: 逆のアプローチ

### NGパターン

❌ "Let's implement the progressive enhancement"
→ 一般的な手法なので冠詞不要

### 自然さUPのコツ

💡 どの機能をどの段階で追加するか例を示す

---

## 27. This follows the open-closed principle

### 例文

- **Context**: 拡張に開かれ修正に閉じた設計を説明する場面
- **A**: "Why use inheritance here instead of modifying the base class?"
- **B**: "This follows the open-closed principle. We can extend functionality without changing existing code."

### 和訳

「これは開放閉鎖原則に従っています」というSOLID原則の一つの適用。既存コードを変更せずに機能拡張。

### 文法解説

- **基本構造**: This + follows + the + 原則名
- **なぜこの形?**: 確立された設計原則への準拠
- **省略・変形**:
  - よりカジュアル: "Extend, don't modify"
  - よりフォーマル: "This adheres to the open-closed principle"

### 使用場面

- オブジェクト指向設計
- コードレビュー
- アーキテクチャ説明

### 似た表現との違い

- **"Don't change the base"**: 理由が不明
- **"Use inheritance"**: 手段のみ

### NGパターン

❌ "This follows open-closed principle"
→ 特定の原則なので定冠詞必要

### 自然さUPのコツ

💡 具体的にどう拡張可能か例を示すと理解しやすい

---

## 28. Let's establish clear boundaries

### 例文

- **Context**: モジュール間の責任範囲を明確にする提案
- **A**: "The modules are tightly coupled and hard to test independently."
- **B**: "Let's establish clear boundaries. Each module should have a well-defined interface."

### 和訳

「明確な境界を確立しましょう」という設計の明確化。モジュール間の依存を最小限に抑える。

### 文法解説

- **基本構造**: Let's + establish + 形容詞 + 複数名詞
- **なぜこの形?**: clearで質を強調、複数形で複数の境界
- **省略・変形**:
  - よりカジュアル: "Let's separate things clearly"
  - よりフォーマル: "We should define explicit module interfaces"

### 使用場面

- システム設計
- マイクロサービス分割
- レイヤー設計

### 似た表現との違い

- **"Separate modules"**: 境界の明確さが不明
- **"Decouple everything"**: 極端すぎる

### NGパターン

❌ "Let's establish clear boundary"
→ 通常複数の境界があるので複数形

### 自然さUPのコツ

💡 どのような基準で境界を設けるか原則を示す

---

## 29. We're applying YAGNI here

### 例文

- **Context**: 将来の要件を想定した過剰な実装を避ける場面
- **A**: "Should I add support for multiple databases even though we only use PostgreSQL?"
- **B**: "We're applying YAGNI here. You Aren't Gonna Need It - implement only what's required now."

### 和訳

「ここではYAGNIを適用しています」という実践的な開発原則。必要になるまで実装しない賢明な判断。

### 文法解説

- **基本構造**: We're + applying + 頭字語 + here
- **なぜこの形?**: 現在進行形で実践中を表現
- **省略・変形**:
  - よりカジュアル: "Don't build it yet"
  - よりフォーマル: "We adhere to the principle of deferred implementation"

### 使用場面

- 機能追加の判断
- 設計の簡素化
- アジャイル開発

### 似た表現との違い

- **"Keep it simple"**: より一般的
- **"Don't over-engineer"**: 否定的

### NGパターン

❌ "We apply YAGNI here"
→ 現在進行形で実践を強調

### 自然さUPのコツ

💡 YAGNIの意味を展開して説明すると親切

---

## 30. Let's make this discoverable

### 例文

- **Context**: APIや機能を見つけやすくする改善を提案する場面
- **A**: "Users can't find the advanced settings."
- **B**: "Let's make this discoverable. Clear naming and logical grouping will help users explore features."

### 和訳

「これを発見しやすくしましょう」という使いやすさの改善提案。ユーザーが直感的に機能を見つけられる設計。

### 文法解説

- **基本構造**: Let's + make + this + 形容詞
- **なぜこの形?**: make + 目的語 + 形容詞で状態変化
- **省略・変形**:
  - よりカジュアル: "Make it easier to find"
  - よりフォーマル: "We should enhance feature discoverability"

### 使用場面

- UI/UX設計
- API設計
- ドキュメント構成

### 似た表現との違い

- **"Make it visible"**: 視覚的側面のみ
- **"Document it"**: 受動的な発見

### NGパターン

❌ "Let's make this discoverable"
→ 文法的には正しいが、冗長さ回避のため言い換え推奨

### 自然さUPのコツ

💡 どのような方法で発見しやすくするか具体策を示す

---