# Airtest導入ガイド

- AirtestIDE V1.2.2 (2019/12)
  
**AirtestスクリプトはPythonを使用する前提で開発されているため、使用前に[Pythonの基礎知識](https://docs.python.org/ja/3.6/tutorial/index.html)を習得しておいてください**  

------
### クイックスタート
  
AirtestスクリプトはPythonを使用する前提で開発されているため、使用前にPythonの基礎知識を習得しておいてください。

#### 1.インストール

<img src="http://airtest.netease.com/static/img/icon/48x48.png" width = "20" height = "20"/> **AirtestIDE**
  
[ダウンロード](http://airtest.netease.com/changelog.html)してインストールする。
  
途中でAirLabのログインモーダルが表示されるが、そのまま無視して問題ない。起動する度にモーダルが表示されが、表示をなくしたい場合は[AirLab](https://airlab.163.com/)に登録する。  
※Githubアカウントで登録可能

- 起動画面  
<img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_start.JPG"/>
  
#### 2.デバイス接続

- **Android**
  - モバイルデバイスをUSBケーブルでPCと接続し、`設定`>`USBの設定` でモバイル側のUSB通信制限を解除してください
  - モバイル側の開発オプションで **「USB デバッグ」** を有効にしてください（[Androidガイド](https://developer.android.com/studio/debug/dev-options.html#debugging)）
  - `Device Screen` -> `Mobile Phone Connection` -> `接続済のデバイス`  
    - Android 9 の場合 `use javacap` を外しても問題ない
    - Android 10 の場合 `use javacap` に<span style="color:red;">必ずチェックを入れてください</span>  
    ※v1.2.2はADBのみで接続エラーとなる
    <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_android_connect.gif"/>
    <br/>
- **Windowsアプリ**
   - 「Select Window」また「Search Window」でWindowsアプリを選択する  
  
- **iOS　β版**
  - Xcodeインストール済のMAC PCを予め用意する
  - iOS-Tagentをインストール
    - 1.iOS-TagentをPCにダウンロード
      > git clone git@github.com:AirtestProject/iOS-Tagent.git
    - 2.XcodeでiOS-Tagentを開き、iPhoneをPCと接続してください
      > メニューから`product` -> `Scheme` -> `WebDriverAgentRunner` を選択  
      > メニューから`product` -> `Destination` -> `*接続したiPhone*` を選択
    <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_iOSTagent.png"/>

