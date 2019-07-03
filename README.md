# raspi-guitar
ラズパイ＋加速度センサー＋puredataで作ったエフェクター

[ハッカーズチャンプルー2019](https://hackers-champloo.org/2019/)で話した  
[LT(ラズパイは〇〇)](https://www.slideshare.net/ShinjiMiyazato/ss-152583546)で紹介したやつの  
ファイルを雑に残しておくリポジトリ  
[Qiita](https://qiita.com/miyaz/items/573af16007ca47c53762)にも概要や解説載せています

## ファイル説明

* ./home/pi/pd-ctlr.py
  * 3つのタクトスイッチを入力としてPureDataを制御するデーモン
  * rc.localからOS起動時にバックグラウンドで実行される
  * スイッチ1制御
    * 3秒以上押し続けるとラズパイ停止
    * 1.5~3秒押し続けるとラズパイ再起動
    * 0.5~1.5秒押し続けるとPureData起動／停止
    * 起動と同時に./home/pi/pd/hcmpl_lt1.pdを読み込み、リズムサンプラー（ドラム）を再生する
  * スイッチ2制御
    * PureDataにrecordシグナルを送信する
    * PureData側ではスイッチを押すごとに３トラックを順番に切り替えて録音する
    * 小説の途中に押した場合は次の小説の頭から録音開始する
    * 録音された音声を自動的にループ再生する
  * スイッチ3制御
    * PureDataにeffectシグナルを送信する
    * PureData側ではエフェクトの切り替えを行う
* ./home/pi/effect-ctlr.py
  * 0.1秒間隔で加速度センサーから取得した値に応じた信号をPureDataに送るデーモン
* ./home/pi/pd/hcmpl_lt1.pd
  * PureDataのパッチ
* ./etc/rc.local
  * OS起動時に必要なスクリプトをバックグラウンド起動している

