# OCI Generative AI Cohere Command R/R+/A チャットサンプルコード

[English version](https://github.com/kutsushitaneko/oci_genai_examples/blob/main/README.md)

このリポジトリには、Oracle Cloud Infrastructure (OCI) Generative AI で提供されている Cohere Command R/R+ をチャットアプリケーションで使用する方法を示すサンプルスクリプトとノートブックが含まれています。

## 解説記事
- [OCI Generative AI で Cohere Command R/R+ の Chat API を試してみる（Update: ストリームチャット対応）](https://qiita.com/yuji-arakawa/items/597c4bd9f3d5b4212b51)
- [地球爆破計画が未遂に終わった件、あるいは Safety Modes - OCI Generative AI サービス](https://qiita.com/yuji-arakawa/items/a8514999463363d13ec6)

## 内容

- `oci_genai_cohere_chat_example.ipynb`: OCI Generative AI Cohere Command R/R+/A によるチャットのためのJupyterノートブック例
- `oci_genai_cohere_chat_example.py`: チャット例のPythonスクリプト版
- `oci_genai_cohere_chat_streaming_example.ipynb`: ストリーミングを使用したOCI Generative AI Cohere Command R/R+/A によるチャットのためのノートブック例
- `oci_genai_cohere_chat_streaming_example.py`: ストリーミングチャット例のPythonスクリプト版
- `oci_genai_cohere_chat_streaming_safety_modes_example.ipynb`: セーフティモードのノートブック例
   - [関連記事：地球爆破計画が未遂に終わった件、あるいは Safety Modes - OCI Generative AI サービス](https://qiita.com/yuji-arakawa/items/a8514999463363d13ec6)
- `oci_genai_cohere_chat_streaming_ai_guardrails_api_example.ipynb`: AI Guardrails API を使用した個人識別情報のマスキング処理のためのノートブック例

## 要件

サンプルプログラムの前提条件：

- Python 3.11.9 で動作確認しています
- 必要なPythonパッケージ（`requirements.txt`に記載）

## セットアップ

1. このリポジトリをクローンします：
   ```
   git clone https://github.com/kutsushitaneko/oci_genai_examples
   cd oci_genai_examples
   ```

2. 必要なパッケージをインストールします：
   ```
   pip install -r requirements.txt
   ```

3. 環境変数を設定します：
   - `.env_sample`を`.env`にコピーします
   - `.env`ファイルにOCIの認証情報とモデルIDを入力します

## 使用方法

### Jupyterノートブック

1. Jupyter Notebookを起動します：
   ```
   jupyter notebook
   ```

2. `oci_genai_cohere_chat_example.ipynb`、`oci_genai_cohere_chat_streaming_example.ipynb`などのノートブックを開きます

3. ノートブック内のセルを実行して、チャット例の動作を確認します

### Pythonスクリプト

以下のいずれかのPythonスクリプトを直接実行します：

```
python oci_genai_cohere_chat_example.py
```

または

```
python oci_genai_cohere_chat_streaming_example.py
```

## ライセンス

このプロジェクトはMIT No Attribution License (MIT-0)の下でライセンスされています。このライセンスでは、ソフトウェアの使用、コピー、変更、配布を制限なく行うことができます。これには、ソフトウェアの使用、コピー、変更、マージ、公開、配布、サブライセンス、販売の権利が含まれますが、これらに限定されません。

ライセンスの全文は以下で確認できます：https://opensource.org/licenses/MIT-0

## 連絡先

質問や問題がある場合は、このリポジトリでIssueを開いてください。
