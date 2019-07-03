sudo apt install puredata
 -> 0.47.1 pd vanilla

このバージョンにはcounterなど使えないオブジェクトがある
dekenを使って使えるようにする

Help -> Find externals
cycloneを入れる
/home/pi/pd/externalsを指定
 -> Successfully upzipped ~ を確認
Preferences -> Path..を開きNew..をクリックし追加したパッケージを指定
 -> これでCycloneに入っているcountオブジェクトが使える
   参考）http://nakagaw.hateblo.jp/entry/2016/12/31/030951

OSCで外部プロセスからBangを受け取る
　受け側は netreceiveを使う
　送信側は、sudo python -m pip install pyOSC 
　以下のようなコードで送信する
------------------
import OSC
c = OSC.OSCClient()
c.connect(('127.0.0.1', 9002))
oscmsg = OSC.OSCMessage()
oscmsg.setAddress("/effect")
oscmsg.append('HELLO')
c.send(oscmsg)
------------------

