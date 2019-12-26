# Airtest導入ガイド 応用編
- [事前準備](https://github.com/saisai-dan-shift/Airtest/tree/master/docs#%E4%BA%8B%E5%89%8D%E6%BA%96%E5%82%99)
- [基礎編：クイックスタート](https://github.com/saisai-dan-shift/Airtest/tree/master/docs#%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%B9%E3%82%BF%E3%83%BC%E3%83%88)
- [上級編]()　未作成
---  
* [IDE設定](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#ide%E8%A8%AD%E5%AE%9A)
* [環境構築](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89)
* [スクリプト作成](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88%E4%BD%9C%E6%88%90)
* [レポーティング](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0)
* [カスタマイズ](https://github.com/saisai-dan-shift/Airtest/blob/master/docs/Advanced.md#%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%82%A4%E3%82%BA)

  複雑な自動化テストを実現するには`Airtest`、`Poco`と`Pythonライブラリ`の連携が必要。また、オリジナルPythonライブラリを導入することによって高機能なテストケースを作ることができる。  

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
### 環境構築
---

- 最新の[ADB(Android Debug Bridge)](https://developer.android.com/studio/releases/platform-tools.html)をダウンロードして解凍する。  
  *`AirtestIDEのインストール場所`*`/airtest/core/android/static/adb/` にある`adb`ファイルを全て置き換える  
  例：Windowsの場合  
  <img src="https://github.com/saisai-dan-shift/Airtest/blob/master/docs/img/Q_ADB.JPG"/>

---
### スクリプト作成
---

---
### レポーティング
---

---
### スクリプト作成
---

---
### カスタマイズ
---