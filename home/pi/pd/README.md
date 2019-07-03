## 手順メモ


### puredataインストール

```
sudo apt install puredata
 -> 0.47.1 pd vanilla
```

### deken＆Gemを導入

使いたいオブジェクトをプラグイン的に追加できるdekenを導入する  
今回はcounterオブジェクトを使うためにcycloneというGemを入れる  

1. Help -> Find externals  
   cycloneを検索してインストールする
1. /home/pi/pd/externalsを指定  
   -> Successfully upzipped ~ を確認
1. Preferences -> Path..を開きNew..をクリックし追加したパッケージを指定  
   -> これでCycloneに入っているcounterオブジェクトが使える  
   参考）http://nakagaw.hateblo.jp/entry/2016/12/31/030951

## OSCで外部プロセスからBangを受け取るTips

受け側は netreceiveを使う  
送信側は、OSCプロトコルでメッセージを送信する

以下Pythonでの例  

sudo python -m pip install pyOSC  
以下のようなコードで送信する  
```
import OSC
c = OSC.OSCClient()
c.connect(('127.0.0.1', 9002))
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/effect")
oscmsg.append('HELLO')
c.send(oscmsg)
```
