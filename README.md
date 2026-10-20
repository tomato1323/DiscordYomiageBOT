# Discord読み上げBOT

ゴールデンタイムだとDiscordのBotが読み上げられないので作ります

## やりたいこと

- Botからテキストをローカルに流す
- assistantseikaとかでAIVOICEとかに流す
- フレンドのテキストが聞こえる

## 環境ファイルに必要なもの

`.env`ファイルに下記を追加してください

1. `BOT_TOKEN`聞きたいサーバーに追加したボットのトークン
1. `CHANNEL_ID`聞きたいサーバーにある聞きたいチャンネルのID、右クリで出るやつ
1. `VOICE_ID`AssistantSeikaの話者一覧にある話者CID
1. `SOUND_LEVEL`音が小さかったら2.0とかにしとくと良き

## BOTに必要なもの

- Privileged Gateway Intents: Message Content Intent(多分いらんとおもうけどPresence Intentも私は入れてある)
- 権限:bot(サーバーに追加するときの権限はこれだけでよろし)
- メッセージ履歴を読む(これも本当は多分なくてもよい？)
ちゃんとテストせずとりあえず動いてるからいいかのノリで開発したソフトなのであやふや条件定義
