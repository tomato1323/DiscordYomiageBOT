バッチファイルに関する質問は受けても返しません。
バッチファイルを使う事で起こる問題や事象について関知しません。対応も約束しません。

必ずご自身で内容を見て、ご自身で問題がない事を確認してください。

  - SeikaSay2.exe
    AssistantSeikaを操作するコマンドです。
     https://wiki.hgotoh.jp/documents/tools/assistantseika/interface/cli/

  - おまけ\seikaClock.cmd
    SeikaSay2.exeを使って現在の時刻を読み上げるためのバッチファイルです。
    CID=1700 が話者の指定部分です。自分の環境に合わせて変更してください。

  - おまけ\seikaClock.xml
    seikaClock.cmdをタスクスケジューラに登録する際のパラメタです。
    <Command>～</Command>、<WorkingDirectory>～</WorkingDirectory>を自分の環境に合わせてください。

  - おまけ\taskadd.cmd
    seikaClock.cmdをタスクスケジューラに登録するためのバッチファイルです。
    1分おきに時刻読み上げが行われます。

  - おまけ\taskremove.cmd
    seikaClock.cmdをタスクスケジューラから解除するためのバッチファイルです。
