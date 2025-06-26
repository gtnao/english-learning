# 設計パターン説明 / Design Patterns

ソフトウェアアーキテクチャの議論で使われる設計パターンに関する表現を集めました。チーム内での技術的な議論をより効果的に行うための表現です。

---

## 1. We should implement a singleton pattern here

### 例文
- **Context**: 設計パターンの提案
- **Architect**: "We should implement a singleton pattern here to ensure only one instance of the configuration manager."

### 和訳
「ここにシングルトンパターンを実装すべきです」
特定の設計パターンの採用を提案する表現。

### 文法解説
- **基本構造**: We should + implement + パターン名
- **なぜこの形?**: shouldで推奨、implementで「実装する」
- **省略・変形**:
  - よりカジュアル: "Let's use a singleton..."
  - よりフォーマル: "I recommend implementing a singleton..."

### 使用場面
- アーキテクチャ設計会議
- コードレビュー
- 技術的な提案

### 似た表現との違い
- **We could use**: より選択的
- **We need to implement**: より必須的

### NGパターン
❌ "We should implement singleton pattern..." (冠詞a必要)
→ a singleton patternが正しい

### 自然さUPのコツ
💡 patternを技術用語として明確に発音

---

## 2. This follows the dependency injection principle

### 例文
- **Context**: 設計原則の説明
- **Developer**: "This follows the dependency injection principle, making our code more testable."

### 和訳
「これは依存性注入の原則に従っています」
コードが特定の設計原則に従っていることを説明する表現。

### 文法解説
- **基本構造**: This follows + the + 原則名
- **なぜこの形?**: followで「従う」、原則は特定なのでthe
- **省略・変形**:
  - よりカジュアル: "This uses DI..."
  - よりフォーマル: "This adheres to the principle of dependency injection..."

### 使用場面
- コードレビュー
- 設計説明
- ベストプラクティスの共有

### 似た表現との違い
- **This implements**: より実装的
- **This conforms to**: より適合的

### NGパターン
❌ "This follow the..." (三単現のs必要)
→ This followsが正しい

### 自然さUPのコツ
💡 principleを原則として重要性を込めて発音

---

## 3. We're violating the single responsibility principle

### 例文
- **Context**: 設計上の問題指摘
- **Code reviewer**: "We're violating the single responsibility principle by having this class handle both data access and business logic."

### 和訳
「単一責任の原則に違反しています」
設計原則に反していることを指摘する表現。

### 文法解説
- **基本構造**: We're violating + the + 原則名
- **なぜこの形?**: violateで「違反する」、進行形で現状
- **省略・変形**:
  - よりカジュアル: "This breaks SRP..."
  - よりフォーマル: "This contravenes the single responsibility principle..."

### 使用場面
- コードレビューでの指摘
- リファクタリングの必要性
- 設計の改善提案

### 似た表現との違い
- **We're breaking**: より直接的
- **This goes against**: より対立的

### NGパターン
❌ "We violate..." (進行形で現在の状態)
→ We're violatingが自然

### 自然さUPのコツ
💡 violatingを問題の深刻さを示して発音

---

## 4. Let's abstract this into an interface

### 例文
- **Context**: 抽象化の提案
- **Senior developer**: "Let's abstract this into an interface so we can swap implementations easily."

### 和訳
「これをインターフェースに抽象化しましょう」
具体的な実装を抽象化することを提案する表現。

### 文法解説
- **基本構造**: Let's abstract + this + into + 抽象化先
- **なぜこの形?**: abstract動詞で「抽象化する」、intoで変換先
- **省略・変形**:
  - よりカジュアル: "Make this an interface..."
  - よりフォーマル: "We should create an abstraction layer..."

### 使用場面
- リファクタリング議論
- 設計改善
- 柔軟性の向上

### 似た表現との違い
- **Let's extract**: より分離的
- **Let's generalize**: より一般化

### NGパターン
❌ "Abstract this to interface..." (前置詞into)
→ abstract into an interfaceが正しい

### 自然さUPのコツ
💡 abstractを設計改善の意図で発音

---

## 5. This creates a circular dependency

### 例文
- **Context**: 依存関係の問題指摘
- **Architect**: "This creates a circular dependency between the modules, which we need to avoid."

### 和訳
「これは循環依存を作り出してしまいます」
モジュール間の問題のある依存関係を指摘する表現。

### 文法解説
- **基本構造**: This creates + a + 問題の種類
- **なぜこの形?**: createで「作り出す」、不定冠詞aで一つの問題
- **省略・変形**:
  - よりカジュアル: "This causes a loop..."
  - よりフォーマル: "This introduces a cyclic dependency..."

### 使用場面
- アーキテクチャレビュー
- 依存関係の分析
- 設計上の問題指摘

### 似た表現との違い
- **This leads to**: より結果的
- **This results in**: より因果的

### NGパターン
❌ "This create..." (三単現のs必要)
→ This createsが正しい

### 自然さUPのコツ
💡 circularを問題の深刻さを示して発音

---

## 6. We can leverage the factory pattern

### 例文
- **Context**: パターンの活用提案
- **Tech lead**: "We can leverage the factory pattern to handle different types of parsers."

### 和訳
「ファクトリーパターンを活用できます」
既存のパターンを利用することを提案する表現。

### 文法解説
- **基本構造**: We can leverage + the + パターン名
- **なぜこの形?**: leverageで「活用する」、特定のパターンなのでthe
- **省略・変形**:
  - よりカジュアル: "Use a factory..."
  - よりフォーマル: "We could utilize the factory pattern..."

### 使用場面
- 設計提案
- 問題解決
- パターンの適用

### 似た表現との違い
- **We can use**: より単純
- **We can apply**: より適用的

### NGパターン
❌ "Leverage factory pattern..." (冠詞the必要)
→ leverage the factory patternが正しい

### 自然さUPのコツ
💡 leverageをビジネス用語として発音

---

## 7. This introduces tight coupling

### 例文
- **Context**: 結合度の問題指摘
- **Reviewer**: "This introduces tight coupling between the view and the controller."

### 和訳
「これは密結合を導入してしまいます」
コンポーネント間の結合度が高くなることを指摘する表現。

### 文法解説
- **基本構造**: This introduces + 問題の種類
- **なぜこの形?**: introduceで「導入する」、tight couplingは技術用語
- **省略・変形**:
  - よりカジュアル: "This makes things too connected..."
  - よりフォーマル: "This creates excessive interdependency..."

### 使用場面
- コードレビュー
- 設計の問題指摘
- リファクタリングの必要性

### 似た表現との違い
- **This causes**: より原因的
- **This results in**: より結果的

### NGパターン
❌ "This introduce..." (三単現のs必要)
→ This introducesが正しい

### 自然さUPのコツ
💡 couplingを技術的な問題として発音

---

## 8. We should favor composition over inheritance

### 例文
- **Context**: 設計原則の推奨
- **Architect**: "We should favor composition over inheritance for this use case."

### 和訳
「継承よりもコンポジションを優先すべきです」
設計上の選択肢を比較し、推奨する表現。

### 文法解説
- **基本構造**: We should favor + A + over + B
- **なぜこの形?**: favorで「優先する」、overで比較
- **省略・変形**:
  - よりカジュアル: "Use composition instead..."
  - よりフォーマル: "We ought to prioritize composition..."

### 使用場面
- 設計方針の決定
- ベストプラクティスの適用
- アーキテクチャ議論

### 似た表現との違い
- **We should prefer**: より選好的
- **We should choose**: より選択的

### NGパターン
❌ "Favor composition than inheritance..." (比較はover)
→ favor composition over inheritanceが正しい

### 自然さUPのコツ
💡 favorを設計原則として発音

---

## 9. This pattern provides loose coupling

### 例文
- **Context**: パターンの利点説明
- **Developer**: "This pattern provides loose coupling, making it easier to test and maintain."

### 和訳
「このパターンは疎結合を提供します」
設計パターンの利点を説明する表現。

### 文法解説
- **基本構造**: This pattern provides + 利点
- **なぜこの形?**: provideで「提供する」、loose couplingは利点
- **省略・変形**:
  - よりカジュアル: "This keeps things loosely connected..."
  - よりフォーマル: "This pattern ensures minimal interdependency..."

### 使用場面
- パターンの利点説明
- 設計決定の根拠
- 技術的な議論

### 似た表現との違い
- **This pattern offers**: より提供的
- **This pattern enables**: より可能的

### NGパターン
❌ "This pattern provide..." (三単現のs必要)
→ This pattern providesが正しい

### 自然さUPのコツ
💡 couplingを技術用語として明確に発音

---

## 10. We're implementing a facade here

### 例文
- **Context**: パターンの実装説明
- **Developer**: "We're implementing a facade here to simplify the complex subsystem interactions."

### 和訳
「ここにファサードを実装しています」
特定のパターンを実装していることを説明する表現。

### 文法解説
- **基本構造**: We're implementing + a + パターン名
- **なぜこの形?**: 進行形で現在の作業、不定冠詞aで一つのパターン
- **省略・変形**:
  - よりカジュアル: "We're using a facade..."
  - よりフォーマル: "We are creating a facade pattern..."

### 使用場面
- 実装の説明
- 進行中の作業報告
- 設計の共有

### 似た表現との違い
- **We're creating**: より作成的
- **We're applying**: より適用的

### NGパターン
❌ "We implementing..." (be動詞必要)
→ We're implementingが正しい

### 自然さUPのコツ
💡 facadeをフランス語風に軽く発音

---

## 11. This violates the open-closed principle

### 例文
- **Context**: SOLID原則違反の指摘
- **Senior developer**: "This violates the open-closed principle - we're modifying existing code instead of extending it."

### 和訳
「これは開放閉鎖の原則に違反しています」
SOLID原則の一つに違反していることを指摘する表現。

### 文法解説
- **基本構造**: This violates + the + 原則名
- **なぜこの形?**: violateで「違反する」、特定の原則なのでthe
- **省略・変形**:
  - よりカジュアル: "This breaks OCP..."
  - よりフォーマル: "This contravenes the open-closed principle..."

### 使用場面
- コードレビュー
- 設計上の問題指摘
- リファクタリングの必要性

### 似た表現との違い
- **This goes against**: より対立的
- **This doesn't follow**: より非遵守的

### NGパターン
❌ "This violate..." (三単現のs必要)
→ This violatesが正しい

### 自然さUPのコツ
💡 principleを原則として重要性を込めて発音

---

## 12. Let's apply the adapter pattern

### 例文
- **Context**: 互換性問題の解決
- **Architect**: "Let's apply the adapter pattern to make these incompatible interfaces work together."

### 和訳
「アダプターパターンを適用しましょう」
特定のパターンを適用することを提案する表現。

### 文法解説
- **基本構造**: Let's apply + the + パターン名
- **なぜこの形?**: applyで「適用する」、特定のパターンなのでthe
- **省略・変形**:
  - よりカジュアル: "Use an adapter..."
  - よりフォーマル: "We should implement the adapter pattern..."

### 使用場面
- 互換性問題の解決
- レガシーコードの統合
- インターフェースの調整

### 似た表現との違い
- **Let's use**: より単純
- **Let's implement**: より実装的

### NGパターン
❌ "Apply adapter pattern..." (冠詞the必要)
→ apply the adapter patternが正しい

### 自然さUPのコツ
💡 adapterを解決策として発音

---

## 13. This follows the MVC architecture

### 例文
- **Context**: アーキテクチャパターンの説明
- **Developer**: "This follows the MVC architecture, separating concerns effectively."

### 和訳
「これはMVCアーキテクチャに従っています」
システムが特定のアーキテクチャパターンに従っていることを説明する表現。

### 文法解説
- **基本構造**: This follows + the + アーキテクチャ名
- **なぜこの形?**: followで「従う」、特定のアーキテクチャなのでthe
- **省略・変形**:
  - よりカジュアル: "This uses MVC..."
  - よりフォーマル: "This adheres to the Model-View-Controller pattern..."

### 使用場面
- システム設計の説明
- アーキテクチャの共有
- 技術文書

### 似た表現との違い
- **This implements**: より実装的
- **This is based on**: より基盤的

### NGパターン
❌ "This follow..." (三単現のs必要)
→ This followsが正しい

### 自然さUPのコツ
💡 MVCを略語として明確に発音

---

## 14. We need to decouple these components

### 例文
- **Context**: 結合度を下げる必要性
- **Tech lead**: "We need to decouple these components to improve maintainability."

### 和訳
「これらのコンポーネントを分離する必要があります」
コンポーネント間の結合度を下げることを提案する表現。

### 文法解説
- **基本構造**: We need to decouple + 対象
- **なぜこの形?**: decoupleで「分離する」、need toで必要性
- **省略・変形**:
  - よりカジュアル: "Let's separate these..."
  - よりフォーマル: "It's necessary to reduce coupling between..."

### 使用場面
- リファクタリング計画
- 保守性の向上
- 設計改善

### 似た表現との違い
- **We should separate**: より分離的
- **We must isolate**: より隔離的

### NGパターン
❌ "We need decouple..." (to不定詞必要)
→ We need to decoupleが正しい

### 自然さUPのコツ
💡 decoupleを技術的改善として発音

---

## 15. This is a classic observer pattern

### 例文
- **Context**: パターンの識別
- **Developer**: "This is a classic observer pattern - the subject notifies all observers of state changes."

### 和訳
「これは典型的なオブザーバーパターンです」
コードが既知のパターンに該当することを指摘する表現。

### 文法解説
- **基本構造**: This is + a classic + パターン名
- **なぜこの形?**: classicで「典型的な」、不定冠詞aで一つの例
- **省略・変形**:
  - よりカジュアル: "That's observer pattern..."
  - よりフォーマル: "This exemplifies the observer pattern..."

### 使用場面
- パターンの識別
- コードレビュー
- 教育的な説明

### 似た表現との違い
- **This is a typical**: より典型的
- **This is a standard**: より標準的

### NGパターン
❌ "This is classic observer..." (冠詞a必要)
→ a classic observer patternが正しい

### 自然さUPのコツ
💡 classicを認識の確信を込めて発音

---

## 16. We're using dependency inversion here

### 例文
- **Context**: 設計原則の適用説明
- **Architect**: "We're using dependency inversion here - high-level modules don't depend on low-level ones."

### 和訳
「ここでは依存性逆転を使用しています」
特定の設計原則を適用していることを説明する表現。

### 文法解説
- **基本構造**: We're using + 原則/パターン名
- **なぜこの形?**: 進行形で現在の実装、usingで「使用」
- **省略・変形**:
  - よりカジュアル: "This uses DIP..."
  - よりフォーマル: "We are applying the dependency inversion principle..."

### 使用場面
- 設計説明
- 原則の適用例
- アーキテクチャ議論

### 似た表現との違い
- **We're applying**: より適用的
- **We're implementing**: より実装的

### NGパターン
❌ "We using..." (be動詞必要)
→ We're usingが正しい

### 自然さUPのコツ
💡 inversionを原則として明確に発音

---

## 17. This enables polymorphic behavior

### 例文
- **Context**: 設計の利点説明
- **Developer**: "This enables polymorphic behavior, allowing us to add new types without modifying existing code."

### 和訳
「これはポリモーフィックな振る舞いを可能にします」
設計が提供する柔軟性を説明する表現。

### 文法解説
- **基本構造**: This enables + 技術的特性
- **なぜこの形?**: enableで「可能にする」、polymorphicは形容詞
- **省略・変形**:
  - よりカジュアル: "This allows different behaviors..."
  - よりフォーマル: "This facilitates polymorphism..."

### 使用場面
- 設計の利点説明
- オブジェクト指向の議論
- 拡張性の説明

### 似た表現との違い
- **This allows**: より許可的
- **This supports**: よりサポート的

### NGパターン
❌ "This enable..." (三単現のs必要)
→ This enablesが正しい

### 自然さUPのコツ
💡 polymorphicを技術用語として発音

---

## 18. Let's extract this into a strategy pattern

### 例文
- **Context**: リファクタリング提案
- **Senior developer**: "Let's extract this into a strategy pattern to handle different algorithms."

### 和訳
「これをストラテジーパターンに抽出しましょう」
コードを特定のパターンにリファクタリングすることを提案する表現。

### 文法解説
- **基本構造**: Let's extract + this + into + パターン
- **なぜこの形?**: extractで「抽出する」、intoで変換先
- **省略・変形**:
  - よりカジュアル: "Pull this out as a strategy..."
  - よりフォーマル: "We should refactor this into a strategy pattern..."

### 使用場面
- リファクタリング提案
- コードの改善
- パターンの適用

### 似た表現との違い
- **Let's refactor**: より再構築的
- **Let's convert**: より変換的

### NGパターン
❌ "Extract into strategy pattern..." (冠詞a必要)
→ extract into a strategy patternが正しい

### 自然さUPのコツ
💡 extractをリファクタリングの意図で発音

---

## 19. This implements the repository pattern

### 例文
- **Context**: データアクセス層の説明
- **Developer**: "This implements the repository pattern, abstracting data access logic."

### 和訳
「これはリポジトリパターンを実装しています」
データアクセス層の設計パターンを説明する表現。

### 文法解説
- **基本構造**: This implements + the + パターン名
- **なぜこの形?**: implementで「実装する」、特定のパターンなのでthe
- **省略・変形**:
  - よりカジュアル: "This uses repository..."
  - よりフォーマル: "This employs the repository pattern..."

### 使用場面
- データ層の設計説明
- アーキテクチャレビュー
- パターンの適用例

### 似た表現との違い
- **This follows**: より従順的
- **This uses**: より使用的

### NGパターン
❌ "This implement..." (三単現のs必要)
→ This implementsが正しい

### 自然さUPのコツ
💡 repositoryをデータパターンとして発音

---

## 20. We should consider the builder pattern

### 例文
- **Context**: 複雑なオブジェクト生成
- **Architect**: "We should consider the builder pattern for constructing these complex objects."

### 和訳
「ビルダーパターンを検討すべきです」
特定のパターンの採用を検討することを提案する表現。

### 文法解説
- **基本構造**: We should consider + the + パターン名
- **なぜこの形?**: considerで「検討する」、shouldで推奨
- **省略・変形**:
  - よりカジュアル: "Think about using builder..."
  - よりフォーマル: "It would be advisable to evaluate the builder pattern..."

### 使用場面
- 設計オプションの検討
- 複雑なオブジェクト生成
- パターン選択

### 似た表現との違い
- **We should use**: より決定的
- **We might try**: より試験的

### NGパターン
❌ "Consider builder pattern..." (冠詞the必要)
→ consider the builder patternが正しい

### 自然さUPのコツ
💡 considerを検討の姿勢で発音

---

## 21. This follows SOLID principles

### 例文
- **Context**: 設計品質の評価
- **Code reviewer**: "This follows SOLID principles well, making the code maintainable and extensible."

### 和訳
「これはSOLID原則に従っています」
コードが設計原則に準拠していることを評価する表現。

### 文法解説
- **基本構造**: This follows + 原則名（複数形）
- **なぜこの形?**: followで「従う」、principlesは複数
- **省略・変形**:
  - よりカジュアル: "This is SOLID..."
  - よりフォーマル: "This adheres to SOLID design principles..."

### 使用場面
- コード品質の評価
- 設計レビュー
- ベストプラクティスの確認

### 似た表現との違い
- **This implements**: より実装的
- **This conforms to**: より適合的

### NGパターン
❌ "This follow SOLID..." (三単現のs必要)
→ This followsが正しい

### 自然さUPのコツ
💡 SOLIDを頭字語として明確に発音

---

## 22. We're dealing with a god object here

### 例文
- **Context**: アンチパターンの指摘
- **Senior developer**: "We're dealing with a god object here - this class has too many responsibilities."

### 和訳
「ここではゴッドオブジェクトを扱っています」
アンチパターンの存在を指摘する表現。

### 文法解説
- **基本構造**: We're dealing with + a + アンチパターン名
- **なぜこの形?**: deal withで「扱う」、進行形で現在の問題
- **省略・変形**:
  - よりカジュアル: "This is a god object..."
  - よりフォーマル: "We have encountered a god object anti-pattern..."

### 使用場面
- 問題のあるコードの指摘
- リファクタリングの必要性
- アンチパターンの識別

### 似た表現との違い
- **We have**: より所有的
- **We're facing**: より対面的

### NGパターン
❌ "Dealing with god object..." (冠詞a必要)
→ dealing with a god objectが正しい

### 自然さUPのコツ
💡 god objectを問題として懸念を込めて発音

---

## 23. This provides a clean separation of concerns

### 例文
- **Context**: 良い設計の評価
- **Architect**: "This provides a clean separation of concerns between business logic and presentation."

### 和訳
「これは関心事の明確な分離を提供します」
設計が責務を適切に分離していることを評価する表現。

### 文法解説
- **基本構造**: This provides + a clean + 技術的利点
- **なぜこの形?**: provideで「提供する」、cleanで「明確な」
- **省略・変形**:
  - よりカジュアル: "This separates things well..."
  - よりフォーマル: "This ensures proper isolation of responsibilities..."

### 使用場面
- 設計の評価
- アーキテクチャの利点
- 良い実装の例

### 似た表現との違い
- **This creates**: より作成的
- **This ensures**: より保証的

### NGパターン
❌ "Provide clean separation..." (三単現のs必要)
→ This providesが正しい

### 自然さUPのコツ
💡 separationを設計品質として発音

---

## 24. Let's implement an event-driven architecture

### 例文
- **Context**: アーキテクチャパターンの提案
- **Tech lead**: "Let's implement an event-driven architecture to handle asynchronous operations better."

### 和訳
「イベント駆動アーキテクチャを実装しましょう」
特定のアーキテクチャパターンの採用を提案する表現。

### 文法解説
- **基本構造**: Let's implement + an + アーキテクチャタイプ
- **なぜこの形?**: implementで「実装する」、不定冠詞anで一つのアーキテクチャ
- **省略・変形**:
  - よりカジュアル: "Go with event-driven..."
  - よりフォーマル: "We should adopt an event-driven architectural pattern..."

### 使用場面
- システム設計の大きな決定
- 非同期処理の改善
- アーキテクチャの選択

### 似た表現との違い
- **Let's use**: より単純
- **Let's adopt**: より採用的

### NGパターン
❌ "Implement event-driven architecture..." (冠詞an必要)
→ implement an event-driven architectureが正しい

### 自然さUPのコツ
💡 event-drivenをハイフンで繋げて発音

---

## 25. This exhibits high cohesion

### 例文
- **Context**: モジュール設計の評価
- **Code reviewer**: "This module exhibits high cohesion - all methods are closely related to the single purpose."

### 和訳
「これは高い凝集性を示しています」
モジュールやクラスの設計品質を評価する表現。

### 文法解説
- **基本構造**: This exhibits + 品質の特性
- **なぜこの形?**: exhibitで「示す」、high cohesionは技術用語
- **省略・変形**:
  - よりカジュアル: "This is well-focused..."
  - よりフォーマル: "This demonstrates excellent cohesion..."

### 使用場面
- コード品質の評価
- モジュール設計の議論
- 良い実装の例

### 似た表現との違い
- **This shows**: より表示的
- **This demonstrates**: より実証的

### NGパターン
❌ "This exhibit..." (三単現のs必要)
→ This exhibitsが正しい

### 自然さUPのコツ
💡 cohesionを設計品質として技術的に発音