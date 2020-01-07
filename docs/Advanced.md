# Airtest導入ガイド 応用編
- [事前準備](https://github.com/saisai-dan-shift/Airtest/tree/master/docs#%E4%BA%8B%E5%89%8D%E6%BA%96%E5%82%99)
- [基礎編：クイックスタート](https://github.com/saisai-dan-shift/Airtest/tree/master/docs#%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88)

---
複雑な自動化テストを実現するには`Airtest`、`Poco`と`Pythonライブラリ`の連携が必要。また、オリジナルPythonライブラリを導入することによって高機能なテストケースを作ることができる。
* [IDE設定](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#ide%E8%A8%AD%E5%AE%9A)
* [環境構築](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89)
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
  
  プラットフォーム別[Pocoの導入方法](https://poco.readthedocs.io/zh_CN/latest/source/doc/poco_drivers.html)  
  AirtestIDEのPocoアシスタントから対象のプラットフォームを選択すれば要素を検索できる。また 
  <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/"/> 










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
### レポーティング
---

---
### スクリプト作成
---

---
### カスタマイズ
---