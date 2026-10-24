# Discord読み上げBOT

ゴールデンタイムだとDiscordのBotが読み上げられないので作ります

## やりたいこと

- Botからテキストをローカルに流す
- assistantseikaとかでAIVOICEとかに流す
- フレンドのテキストが聞こえる

## 必須ソフト
- Python 3.14
- [AssistantSeika](https://wiki.hgotoh.jp/documents/tools/assistantseika/introduction/assistantseika-000)

ライブラリ関連はCloneしてdependenciesから引っ張ってください

## 使い方
BOTの設定とか追加とかもろもろやっといてください
作成したBOTのトークンをメモしておいてください。
BOTを追加したサーバーでListenしたいチャンネルIDをコピーしといてください。

1. AssistantSeikaと対応するTTS(AIVOICEとか)を起動
1. `.env`ファイルに下記情報を入力
1. BATファイルを起動

### 環境ファイルに必要なもの

`.env`ファイルに下記を追加してください

2. `BOT_TOKEN`聞きたいサーバーに追加したボットのトークン
2. `CHANNEL_ID`聞きたいサーバーにある聞きたいチャンネルのID、右クリで出るやつ
2. `VOICE_ID`AssistantSeikaの話者一覧にある話者CID
2. `SOUND_LEVEL`音が小さかったら1.5とかにしとくと良き

### BOTに必要なもの

- Privileged Gateway Intents: Message Content Intent(多分いらんとおもうけどPresence Intentも私は入れてある)
- 権限:bot(サーバーに追加するときの権限はこれだけでよろし)
- メッセージ履歴を読む(これも本当は多分なくてもよい？)
ちゃんとテストせずとりあえず動いてるからいいかのノリで開発したソフトなのであやふや条件定義
