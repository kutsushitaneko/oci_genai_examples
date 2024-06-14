# %% [markdown]
# # Oracle Generative AI Service チャットサンプルノートブック（Cohere Command R）
# 関連ドキュメント： Accessing The Code (https://docs.oracle.com/en-us/iaas/Content/generative-ai/get-code.htm#get-code)

# %% [markdown]
# ## ライブラリインポート
# - oci : OCI SDK（ソフトウェア開発キット : https://docs.oracle.com/ja-jp/iaas/Content/API/Concepts/sdks.htm ）
# - os ：オペレーティングシステムへのアクセスを提供するライブラリ（標準ライブラリ : https://docs.python.org/ja/3/library/os.html ）
# - time : 時刻データへのアクセスと変換（標準ライブラリ : https://docs.python.org/ja/3/library/time.html ）
# - dotenv : 環境変数を管理するためのライブラリ（python-dotenv : https://pypi.org/project/python-dotenv/ ）

# %%
import oci
import os
import time
from dotenv import load_dotenv, find_dotenv

# %% [markdown]
# ## 環境変数設定
# OCI のコンパートメントIDを環境変数に設定します。事前準備として ".env" ファイルに OCI_COMPARTMENT_ID=XXXXXXXXXX の書式でコンパートメントIDを記載しておく必要があります
# 

# %%
_= load_dotenv(find_dotenv())

# %% [markdown]
# ## OCI 認証設定
# - CONFIG_PROFILE：構成ファイルに定義されたプロファイル名
# - config : SDK and Tool Configuration（認証に関する構成情報を定義するディクショナリー）[リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/configuration.html)
# 
# 参考ドキュメント
# - [SDKおよびCLIの構成ファイル](https://docs.oracle.com/ja-jp/iaas/Content/API/Concepts/sdkconfig.htm)
# - [Configuration](https://docs.oracle.com/en-us/iaas/tools/python/latest/configuration.html)
# 
# 

# %%
CONFIG_PROFILE = "DEFAULT" # 構成ファイルに合わせて変更してください。
config = oci.config.from_file(file_location='~/.oci/config', profile_name=CONFIG_PROFILE)

# %% [markdown]
# ## Oracle Generative AI Service （生成AIサービス）設定
# - compartment_id ： OCIコンパートメントID
# - （オプション）endpoint ： Generative AI Service （生成AIサービス）のサービスエンドポイントURL（カスタム・モデル、もしくは、ホスティング専用AIクラスタを使用する際に指定します。 このノートブックでは使用しません）
# - model_id ： 推論に使用する基盤モデルのID

# %%
compartment_id = os.getenv("OCI_COMPARTMENT_ID") 
#endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com" # カスタム・モデル、もしくは、ホスティング専用AIクラスタを使用する際に指定します。生成AIコンソールのエンドポイントで確認できます。
model_id = "cohere.command-r-16k"

# %% [markdown]
# ## Generative AI Service （生成AIサービス）の推論クライアントの生成
# - GenerativeAiInferenceClient：Generative AI Service （生成AIサービス）の推論クライアントクラス[リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/api/generative_ai_inference/client/oci.generative_ai_inference.GenerativeAiInferenceClient.html#oci.generative_ai_inference.GenerativeAiInferenceClient)
#   - コンストラクタ：生成AIサービスの基盤モデルで推論を行うためのサービスクライアントを生成
#       - config : SDK and Tool Configuration（ディクショナリー）[リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/configuration.html)
#       - service_endpoint : （オプション）サービスエンドポイント（カスタム・モデル、もしくは、ホスティング専用AIクラスタを使用する際に指定）
#   - メソッド
#       - chat ：チャット応答を生成するメソッド（チャット応答の生成で呼び出す）
#       - embed_text ：入力データの埋め込み（エンベディング、ベクトルデータ）を生成するメソッド（このノートブックでは使用しない）
#       - generate_text ：ユーザープロンプトに基づいてテキスト応答を生成するメソッド（このノートブックでは使用しない）
#       - summarize_text ：入力テキストを要約するメソッド（このノートブックでは使用しない）

# %%
generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(config=config, retry_strategy=oci.retry.NoneRetryStrategy(), timeout=(10,240))
#generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(config=config, service_endpoint=endpoint, retry_strategy=oci.retry.NoneRetryStrategy(), timeout=(10,240))

# %% [markdown]
# ## チャットリクエストを定義
# CohereChatRequest : Cohere の基盤モデルへのチャットリクエストを定義したクラス。 BaseChatRequest クラスの派生クラス。[リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/api/generative_ai_inference/models/oci.generative_ai_inference.models.CohereChatRequest.html#oci.generative_ai_inference.models.CohereChatRequest)
# - prompt : プロンプト
# - is_stream : 部分的な進行状況をストリームバックするかどうか。True に設定されている場合、利用可能となったトークンから順次 server-sent イベントとして送信される。
# - max_tokens : 出力トークンの最大数
# - temperature : 生成される出力のランダム性を設定する数値。値が低いほどランダム性が小さい。
# - frequency_penalty : 生成されたトークンの反復を減らすために、生成されたテキスト内の頻度に基づいて新しいトークンにペナルティを与えます。大きな数値は、モデルに新しいトークンを使用するように促し、小さな数値はトークンを繰り返すように促す。無効にするには、0に設定する。
# - top_p : トークン群のうちその生成確率を確率の高いものから順に累計した合計が top_p となるまでのトークン群のみを候補として生成を行う。出現頻度の低いトークンを生成させたくない場合は小さな値を設定する。
# - top_k ：トークン群のついその生成確率が高いものから k 個のトークン群のみを候補して生成を行う。
# - is_echo ：Trueの場合にモデルに送信された完全なプロンプトを返します。
# - chat_history ： ユーザーとモデル間の過去のメッセージのリスト。以下の3種類のメッセージを含むリストを設定します。
#   - CohereSystemMessage ： システムロールのメッセージを定義したクラス。 CohereMessage クラスの派生クラス。[リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/api/generative_ai_inference/models/oci.generative_ai_inference.models.CohereSystemMessage.html)
#   - CohereUserMessage ： ユーザーロールのメッセージを定義したクラス。 CohereMessage クラスの派生クラス。[リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/api/generative_ai_inference/models/oci.generative_ai_inference.models.CohereUserMessage.html)
#   - CohereChatBotMessage ： チャットボットロールのメッセージを定義したクラス。 CohereMessage クラスの派生クラス。[リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/api/generative_ai_inference/models/oci.generative_ai_inference.models.CohereChatBotMessage.html)
# - documents ： ユーザーのリクエストに対して根拠のある応答を生成するためにモデルが参照できる関連文書のリスト。

# %%
chat_request = oci.generative_ai_inference.models.CohereChatRequest()
chat_request.message = "オラクルのリレーショナルデータベースについて教えてください。"
chat_request.max_tokens = 500
chat_request.is_stream = False
chat_request.temperature = 0.75
chat_request.top_p = 0.7
chat_request.top_k = 0 # Only support topK within [0, 500]
chat_request.frequency_penalty = 1.0
chat_request.is_echo = True

previous_chat_system_message = oci.generative_ai_inference.models.CohereSystemMessage(role="SYSTEM", message="あなたはIT業界に精通した優秀なテクニカルライターです。")
previous_chat_user_message = oci.generative_ai_inference.models.CohereUserMessage(role="USER", message="オラクルとはどんな会社ですか？")
previous_chat_chatbot_message = oci.generative_ai_inference.models.CohereChatBotMessage(role="CHATBOT", message="Oracleは、エンタープライズIT市場における最大手のベンダーの一つであり、その主力製品の略称でもあります。このデータベースソフトウェアは、多くの企業のITシステムで利用されています。")
chat_request.chat_history = [previous_chat_system_message, previous_chat_user_message, previous_chat_chatbot_message]
chat_request.documents = [
    {
        "title": "Oracle",
        "snippet": "オラクルのデータベース・サービスおよび製品は、世界をリードするコンバージド・マルチモデル・データベース管理システムであるOracle Databaseをはじめ、インメモリ、NoSQLMySQLデータベースなど、お客様に最適なコストとパフォーマンスを提供しています。Oracle Autonomous Databaseは、Oracle Cloud@CustomerまたはOracle Cloud Infrastructureによって、提供されており、お客様は、リレーショナル・データベース環境を簡素化し、管理ワークロードを削減できます。",
        "website": "https://www.oracle.com/jp/database/"
    }
]

# %% [markdown]
# ## チャット応答生成リクエストの詳細を定義
# ChatDetails ：チャット応答生成リクエストの詳細を定義したクラス（HTTP リクエストの body となる） [リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/api/generative_ai_inference/models/oci.generative_ai_inference.models.ChatDetails.html)
#   - generative_ai_inference_client の chat メソッドの引数となる
#   - compartment_id : OCIコンパートメントID
#   - chat_request : チャットリクエストを定義した CohereChatRequest クラスのインスタンス
#   - serving_mode : モデルのサービングモード
#     - OnDemandServingMode : カスタム・モデル、ホスティング専用AIクラスタを使用しない場合
#     - DedicatedServingMode : カスタム・モデル、もしくは、ホスティング専用AIクラスタを使用する場合
# 
# 

# %%
chat_detail = oci.generative_ai_inference.models.ChatDetails()

chat_detail.serving_mode = oci.generative_ai_inference.models.OnDemandServingMode(model_id=model_id)
chat_detail.compartment_id = compartment_id
chat_detail.chat_request = chat_request

# %% [markdown]
# ## チャット応答の生成
# chat : ユーザープロンプトに基づいてチャット応答を生成するメソッド  [リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/api/generative_ai_inference/client/oci.generative_ai_inference.GenerativeAiInferenceClient.html#oci.generative_ai_inference.GenerativeAiInferenceClient.chat)
# - oci.generative_ai_inference.GenerativeAiInferenceClient クラスのメソッド  [リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/api/generative_ai_inference/client/oci.generative_ai_inference.GenerativeAiInferenceClient.html#oci.generative_ai_inference.GenerativeAiInferenceClient)
# - 引数 : チャット応答生成リクエストの詳細クラス ChatDetails のインスタンス  [リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/api/generative_ai_inference/models/oci.generative_ai_inference.models.ChatDetails.html#oci.generative_ai_inference.models.ChatDetails)
# （前のセルで生成・設定した chat_detail）
# 
# - 戻り値：チャット応答を含む Response クラスのインスタンス  [リファレンス](https://docs.oracle.com/en-us/iaas/tools/python/latest/api/request_and_response.html#oci.response.Response)
# 
# 
# 

# %%
start_time = time.perf_counter()
chat_response = generative_ai_inference_client.chat(chat_detail)
end_time = time.perf_counter() 
elapsed_time = end_time - start_time

# %% [markdown]
# ## チャット応答を表示

# %%
#print("**************************Chat Response*********************************")
#print(f"chat_response.data:\n{chat_response.data}")

print("**************************Chat History*************************************")
for history in chat_response.data.chat_response.chat_history:
    print(f"Role: {history.role}, Message: {history.message}\n")
print("**************************Chatbot Message**********************************")
print(f"text:\n{chat_response.data.chat_response.text}\n")
print("**************************Citations****************************************")
citations = chat_response.data.chat_response.citations
for i, citation in enumerate(citations, start=1):
    print(f"Citation {i}:")
    print(f"  Document IDs: {citation.document_ids}")
    print(f"  Start: {citation.start}")
    print(f"  End: {citation.end}")
    print(f"  Text: {citation.text}")
    print()
print("**************************Finish Reason************************************")
print(f"finish_reason:{chat_response.data.chat_response.finish_reason}\n")
print("**************************Prompt*******************************************")
print(f"prompt:{chat_response.data.chat_response.prompt}\n")
print("**************************Inference Time***********************************")
print(f"total inference time: {elapsed_time:.2f} sec")

# %%



