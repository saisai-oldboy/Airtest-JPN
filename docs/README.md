# Airtest導入ガイド

- 対象：AirtestIDE V1.2.2 (2019/12)
- AirtestスクリプトはPythonを使用する前提で開発されているため、使用前に[Pythonの基礎知識](https://docs.python.org/ja/3.6/tutorial/index.html)を習得しておくことがおすすめ
- [クイックスタート](https://github.com/saisai-dan-shift/Airtest/tree/master/docs#%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88)
- [応用編](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md)

### 事前準備
  
- [Python 3.6.8](https://www.python.org/downloads/release/python-368/) をインストールしておく。Windowsの場合PATHを通す。  
  他のバージョンでの動きが不安定なので、できるだけPython 3.6.Xを使用してください（2019/12時点）
- [Java(JDK)](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)をダウンロードしてインストールする
- [Git](https://git-scm.com/)をインストールしておく
- [Homebrew](https://brew.sh/index_ja)をインストールしておく。**※ MacOSのみ**

---
### クイックスタート
---

#### 1.インストール

<img src="http://airtest.netease.com/static/img/icon/48x48.png" width = "20" height = "20"/> **AirtestIDE**
  
AirtestIDEを[ダウンロード](http://airtest.netease.com/changelog.html)してインストールする。
  
途中でAirLabのログインモーダルが表示されるが、そのまま無視して問題ない。起動する度にモーダルが表示されるので、表示をなくしたい場合は[AirLab](https://airlab.163.com/)に登録する。  
※Githubアカウントで登録可能

- 起動画面  
<img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_start.JPG"/>
  
#### 2.デバイス接続

- **Android**
  - モバイルデバイスをUSBケーブルでPCと接続し、`設定`>`USBの設定` でモバイル側のUSB通信制限を解除する
  - モバイル側の開発オプションで **「USB デバッグ」** を有効にする（[Androidガイド](https://developer.android.com/studio/debug/dev-options.html#debugging)）
  - `Device Screen` -> `Mobile Phone Connection` -> `接続済のデバイス`  
    - Android 9 の場合 `use javacap` を外しても問題ない
    - Android 10 の場合 `use javacap` に **`必ずチェック`** を入れてください  
    ※v1.2.2の場合、ADBのみで接続するとエラーになる
    <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_android_connect.gif"/>
    <br/>
- **Windowsアプリ**
   - 「Select Window」また「Search Window」でWindowsアプリを選択する  
  
- **iOS　β版**
  - Xcodeインストール済のMAC PCを用意する
  - iOS-Tagentをインストール
    - 1.iOS-TagentをPCにダウンロード
      > git clone git@github.com:AirtestProject/iOS-Tagent.git
    - 2.XcodeでiOS-Tagentを開き、iPhoneのDeveloperモードが有効になっていることを確認する。
      <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_iPhoneDev.png" width="30%"/>   
      > Xcodeメニューから`product` -> `Scheme` -> `WebDriverAgentRunner` を選択する。
      <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_iOSTagent.png"/>  

      > Xcodeメニューから`product` -> `Destination` -> *`接続したiPhone`* を選択する。  
         
      > Xcodeメニューから`product` -> `Test` を選択し、正常に起動していることを確認する。  
      <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_Xcode.png"  width = "400" />
        
      ```
      2019-12-26 16:16:39.047184+0900 WebDriverAgentRunner-Runner[380:60778] Running tests...
      Test Suite 'All tests' started at 2019-12-26 16:16:41.095
      Test Suite 'WebDriverAgentRunner.xctest' started at 2019-12-26 16:16:41.095
      Test Suite 'UITestingUITests' started at 2019-12-26 16:16:41.095
      Test Case '-[UITestingUITests testRunner]' started.
      t =     0.00s Start Test at 2019-12-26 16:16:41.096
      t =     0.00s Set Up
      ```
  - iPhone側で`設定` -> `一般` -> `プロフィルとデバイス管理` -> `iOS-Tagent` を有効にする。  
    <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_iPhoneprofile.png" width="50%"/>  

  - iproxyをインストールする。  
    `$ brew install libimobiledevice`

  - iproxyを起動する。  
    `$ iproxy 8100 8100`

  - ブラウザを起動して http://127.0.0.1:8100/inspector にアクセスする。iPhoneの画面が映し出されていることを確認する。  

  - AirtestIDEで接続  
    <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_Airtest_iOS.gif"/>  
   
#### 3.最初のテストを作る

- レコーディング機能を使って記録する方法：  
  [AirtestIDE公式ドキュメント](http://airtest.netease.com/docs/docs_AirtestIDE-en_US/1_online_help/airtest_intro.html#recording-airtest-script-in-airtestide)  
  レコーディング例（from 公式サイト）：
  - 自動レコーディング  
    <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/airtest_auto_record.gif"/> 
  - マニュアルレコーディング  
    <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/airtest_manual_record.gif"/>