# Airtest導入ガイド 応用編
- [事前準備](https://github.com/saisai-dan-shift/Airtest/tree/master/docs#%E4%BA%8B%E5%89%8D%E6%BA%96%E5%82%99)
- [基礎編：クイックスタート](https://github.com/saisai-dan-shift/Airtest/tree/master/docs#%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88)
<br/>  
  複雑な自動化テストを実現するには`Airtest`、`Poco`と`Pythonライブラリ`の連携が必要となる。また、オリジナルPythonライブラリを導入することによって高機能なテストケースを作ることができる。
---
### IDE設定
---

- `Show Real-time Cursor Coordinate` -> `デバイス上の座標を表示`
- `Relative Coordinate` -> `デバイス上の（相対）座標を表示`
- `Auto Complete` -> `自動補完` ※IDEの性能が落ちるので、チェックを外すほうがいい
- `Default Log Path` -> `テスト結果の格納場所`
- **`Custom Python Path` -> `事前にインストールしたPython 3.6.xの場所`**
- `Chrome Path` -> `Chromeのインストール場所`
  <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/A_Settings.JPG"/>
---
### 環境設定
---

- 最新の[ADB(Android Debug Bridge)](https://developer.android.com/studio/releases/platform-tools.html)をダウンロードして解凍する。  
  *`インストール場所`*`/airtest/core/android/static/adb/` にある`adb`ファイルを置き換える  
  例：Windowsの場合  
  <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_ADB.JPG"/>