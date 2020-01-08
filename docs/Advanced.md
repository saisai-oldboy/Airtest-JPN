# Airtest導入ガイド 応用編
- [事前準備](https://github.com/saisai-dan-shift/Airtest/tree/master/docs#%E4%BA%8B%E5%89%8D%E6%BA%96%E5%82%99)
- [クイックスタート](https://github.com/saisai-dan-shift/Airtest/tree/master/docs#%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88)

---
高度な自動化テストを実現するには`Airtest`、`Poco`と`Pythonライブラリ`の連携が必要。また、オリジナルPythonライブラリを導入することによって高機能なテストケースを作ることができる。
* [IDE設定](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#ide%E8%A8%AD%E5%AE%9A)
* [環境構築](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89)
* [Pythonコマンドで実行]()
* [スクリプト作成](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88%E4%BD%9C%E6%88%90)
* [レポーティング](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0)
* [カスタマイズ](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%82%A4%E3%82%BA)

---
### IDE設定
---

- `Show Real-time Cursor Coordinate` -> `デバイス上の座標を表示`
- `Relative Coordinate` -> `デバイス上の（相対）座標を表示`
- `Auto Complete` -> `自動補完` ※IDEの性能が落ちるので、チェックを外したほうがいい
- `Default Log Path` -> `テスト結果の格納場所`
- **`Custom Python Path` -> `Python 3.6.x実行ファイルの場所`**
- `Chrome Path` -> `Chrome実行ファイルの場所`
  <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/A_Settings.JPG"/>
---
### スクリプト作成
---
- 新規作成

IDEの「File」また「＋」から`.air`また`.py`を選択して新規スクリプトを作る  
<img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/A_new.gif"/>

- Airtestアシスタント  

| 操作系 | 補助      | アサーション |
|--------|---------|--------|
|touch	 |text	    |assert_exists    |
|swipe	 |keyevent	|assert_not_exists|
|wait	 |sleep	    |assert_equal     |
|exist	 |	        |assert_not_equal |
|snapshot |	        |                 |

- キャプチャの挿入  
  <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/A_insertimg.JPG"/>  
  対象オブジェクトを繰り返し検出する際に役立つ  

- 画像認識の設定  
  画像をダブルクリックしてImage Editorを開き、`Snapshot Recognition`を押すと現在の表示画面で対象オブジェクトの画像認識を確認できる。 
  - threshold(浮動小数点型)  
　  画像認識の閾値を設定する。範囲：`[0.0, 1.0]`　デフォルト：`[0.6]`  
  - target_pos(整数型)  
　  対象画像の操作範囲を指定する。範囲：`[1, 9]`　デフォルト：`[5]`  
    <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/A_target_pos.png"/>
  - rgb(bool型)  
    画像認識でRGBレイヤーを使用する。デフォルト：`Flase`（輝度レイヤーのみ使用）  
  <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/A_ocr_setting.gif"/>  

- Poco UIツリー  
  プラットフォーム別の[Pocoの導入方法](https://poco.readthedocs.io/zh_CN/latest/source/doc/poco_drivers.html)  
  AirtestIDEのPocoアシスタントから対象のプラットフォームを選択すれば要素を一覧表示・検索できる。さらに`poco Inspector`を使えば対象オブジェクトを簡単に見けられる。ツリーから対象オブジェクトをダブルクリックすればソースに追加できる。
  <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/A_pocotree.gif"/> 

---
### 環境構築
---
- Airtestフレームワークをインストールする。
  >pip install -U airtest

  Mac/Linuxの場合、手動での権限付与が必要
  >#Mac  
  >cd {your_python_path}/site-packages/airtest/core/android/static/adb/mac  
  >#Linux  
  >cd {your_python_path}/site-packages/airtest/core/android/static/adb/linux

  >chmod +x adb
  
  エラー対策：  
    - `cv2`モジュール`ImportError: DLL load failed`エラー 
      [最新版AirtestIDE](http://airtest.netease.com/changelog.html)をダウンロードして解凍する。`api-ms-win-downlevel-shlwapi-l1-1-0.dll`と`IEShims.dll`2つのファイルを`C:\Windows\System32`にコピーする。
    - win.py実行時`import win32api`の`DLL load failed`エラー  
      pywin32を再インストールする。  
      >pip uninstall pywin32
      >pip install pywin32==223


- Pocoフレームワークをインストールする。
  >pip install -U pocoui

- ADBを更新しておいたほうがいい  
  最新の[ADB(Android Debug Bridge)](https://developer.android.com/studio/releases/platform-tools.html)をダウンロードして解凍する。  
  *`AirtestIDEのインストール場所`*`/airtest/core/android/static/adb/` にある`adb`ファイルを全て置き換える  
  例：Windows SDKの場合  
  <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_ADB.JPG"/>

---
### Pythonコマンドで実行
---

#### コマンド例：
>airtest run untitled.air --device Android:///デバイス番号 --log log/
>python -m airtest run untitled.air --device Android:///デバイス番号 --log log/

- `airtest run` 実行スクリプト 
- --device デバイス番号
- --log指定 ログファイル保存場所
  
#### デバイス番号の定義：
>Android://<adbhost[localhost]>:<adbport[5037]>/<serialno>

- adbhost：adb serverのIPアドレス。デフォルトは127.0.0.1
- adb port：デフォルトは5037
- serialno：androidのシリアルナンバー  

#### デバイス番号指定の例：
>#指定なしの場合は最初のデバイスに接続  
>Android:///  

>#シリアルナンバーが79d03faのデバイスをデフォルトIP:Portで接続する  
>Android://127.0.0.1:5037/79d03fa  

>#adb connectでリモート接続する。※シリアルナンバーの代わりに10.254.60.1:5555を使用  
>Android://127.0.0.1:5037/10.254.60.1:5555  

>#window handleが123456のWindowsフォームに接続する  
>Windows:///123456  

>#windowタイトルを正規表現で指定し、Windowsフォームに接続する  
>Windows:///?title_re=Unity.*  

>#windowsのdesktopに接続  
>Windows:///  

>#iOSデバイスに接続する  
>iOS:///127.0.0.1:8100  

##### 接続オプション 
デバイスによってIDEで接続する際に`use ADB orientation`また`use javacap`のチェックが必須となる。コマンド実行時も同様。  
>#例：`Use javacap`の場合  
>Android://127.0.0.1:5037/127.0.0.1:7555?cap_method=JAVACAP  

>#複数項目を使う場合は`&&`を使う  
>Android://127.0.0.1:5037/79d03fa?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=ADBTOUCH  

##### 実行画面の録画
オプション`--recording`で実行すれば、`recording_0.mp4`のようなmp4ファイルが自動的に生成され、レポーティングの時はデフォルトのHTMLに取り込まれる  

#### 複数デバイスの実行（Androidのみ）
**複数デバイスで1つのスクリプト**を同時実行するでなく、**1つのスクリプトで複数のデバイス**を使う場合である。例えば、SNSアプリでお互いに友たち承認する場合など、デバイス間の連携が必要なときには有効な手段となる。  
  
方法：`set_current `で簡単にデバイスの切り替えられる。  
コマンド実行時：`--device`オプションでデバイス追加する
>airtest run untitled.air --device Android:///serialno1 --device Android:///serialno2 --device Android:///serialno1

スクリプトの例：
```
from airtest.core.api import connect_device

# 1台目のデバイス
dev1 = connect_device("Android://127.0.0.1:5037/serialno1")
# 2台目のデバイス
dev2 = connect_device("Android://127.0.0.1:5037/serialno2")

# グローバル変数G.DEVICE_LISTが[dev1, dev2]になっていることを確認できる
print(G.DEVICE_LIST)

# 1番目のデバイスに切り替え
set_current(0) 
#シリアル番号serialno2のデバイスに切り替え
set_current("serialno2")

#オブジェクトを取得
current_dev = device()
```

#### Android専用インターフェース

[airtest.core.android.android](https://airtest.readthedocs.io/en/latest/all_module/airtest.core.android.android.html)の呼出例：
```
# デバイスオブジェクト取得
dev = device()

# デバイス情報
print(dev.get_display_info())

# インストール済のアプリリスト
print(dev.list_app())
```
ADBコマンドの呼出例：
```
# adb shell ls
print(shell("ls"))

# デバイス指定adb shell ls
dev = connect_device("Android:///device1")
dev.shell("ls")

# 任意のデバイスに切り替えてaadb shell ls
set_current(0)
shell("ls")
```

---
### スクリプト作成
---


---
### レポーティング
---

---
### カスタマイズ
---