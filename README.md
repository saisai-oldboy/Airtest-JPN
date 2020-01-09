<img src="https://avatars3.githubusercontent.com/u/34292813?s=200&v=4" width = "100" height = "100"/>

# Airtest プロジェクト

AirtestはNetEaseが開発した画像認識によるUI自動テストIDE

- [AritestIDE 公式サイト](http://airtest.netease.com/)

- [Github - AirtestProject](https://github.com/AirtestProject)

- オフィシャル資料（英語）
  >[AritestIDE](http://airtest.netease.com/docs/en/index.html)  
  >[Aritest](https://airtest.readthedocs.io/en/latest/)  
  >[Poco](https://poco.readthedocs.io/en/latest/)

- [導入ガイド（日本語）](https://github.com/saisai-oldboy/Airtest/tree/master/docs)

## 概要

#### 全体像

![](https://github.com/saisai-oldboy/Airtest/blob/master/docs/img/airtest_jp.png)
#### 特徴
- 自動化テストコード作成、メンテナンスのコストダウン
  >スクリプト記録機能が内蔵されており、プログラミング出来ない人でも手軽にテストスクリプトを作成することができる  
  >IDEの導入、テスト実行とレポーティングは容易に行える
- ゲーム自動化テスト
  >主流ゲームエンジンをサポートするクロスプラットフォームである。モバイルゲームの自動化テストをより簡単にできる
---
## 自動化フレームワーク
- [Airtest](https://airtest.readthedocs.io/en/latest/README_MORE.html)
  >Pythonで開発されたUIクロステストフレームワーク。画像認識技術が内蔵されており、ゲームやAPPの自動化テストに適応している
- [Poco](https://poco-chinese.readthedocs.io/en/latest/source/README.html)
  >UI要素検索用テストフレームワーク。Android、iOS以外、ゲームとHTML5アプリもサポートしている

#### WEB自動化テスト
- Seleniumサポート  
  [Airtest-Selenium](http://airtest.netease.com/docs/en/1_quick_start/5_get_started_with_web_test.html?highlight=selenium)がIDEに内蔵されており、現在(2020/01)Chromeのみサポートしている

#### 対応環境

| プラットフォーム                 | Airtest                        | Poco                                                                                                    |
|---------------------------|--------------------------------|---------------------------------------------------------------------------------------------------------|
| [Android](http://airtest.netease.com/docs/en/1_quick_start/2_test_with_Android_device.html)                 | √ [model list](#%E5%AF%BE%E5%BF%9C%E3%83%87%E3%83%90%E3%82%A4%E3%82%B9%E4%B8%80%E8%A6%A7201912%E6%99%82%E7%82%B9)             | √                                                                                                       |
| [Emulator](#対応エミュレーター)                  | √ [model list](#%E5%AF%BE%E5%BF%9C%E3%82%A8%E3%83%9F%E3%83%A5%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC201912%E6%99%82%E7%82%B9)    | √                                                                                                       |
| [iOS](https://github.com/AirtestProject/iOS-Tagent)                       | √ [model list](https://github.com/AirtestProject/iOS-Tagent) | [ios-tagent](https://github.com/AirtestProject/iOS-Tagent)                            |
| [Windows](http://airtest.netease.com/docs/en/1_quick_start/4_get_started_with_Windows_test.html)                  | √                              | 未対応                                                                                                 | 
| Cocos2dx-js & Cocos2dx-lua| √                              | √ [integration doc](https://poco.readthedocs.io/en/latest/source/doc/integration.html#cocos2dx-lua)            |
| Unity3D                   | √                              | √ [integration doc](https://poco-chinese.readthedocs.io/en/latest/source/doc/integration.html#unity3d)         |
| Other engines             | √                              | √ [implementation doc](https://poco-chinese.readthedocs.io/en/latest/source/doc/implementation_guide.html)        |

#### 対応デバイス一覧（2020/01時点）
| No. | デバイス                          | 備考 |
|------|----------------------------------|------|
| 1    | Huawei Honor 3C（H30-L01）           |      |
| 2    | Huawei Honor 4A（SCL-AL00）          |      |
| 3    | Huawei Honor 4C（CHM-TL00）          |      |
| 4    | Huawei Honor 6（H60-L01）            |      |
| 5    | Huawei Honor 6 Plus（PE-TL10）       |      |
| 6    | Huawei Honor 7（PLK-AL10）           |      |
| 7    | Huawei Honor 7i（ATH-AL00）          |      |
| 8    | Huawei Honor（G750-T01） |      |
| 9    | Huawei Honor 4（G621-TL00）      |      |
| 10   | Huawei Honor 4X（CHE-TL00H）    |      |
| 11   | Huawei Honor 4X（CHE1-CL20）     |      |
| 12   | Huawei Honor 5A（CAM-AL00）      |      |
| 13   | Huawei Honor 5X（KIW-AL10）      |      |
| 14   | Huawei Honor 5C（NEM-TL00H）     |      |
| 15   | Huawei Honor 6X（BLN-AL30）      |      |
| 16   | Huawei Enjoy 5（TIT-AL00）           |      |
| 17   | Huawei Enjoy 5S（TAG-AL00）          |      |
| 18   | Huawei Enjoy 6S（DIG-AL00）          |      |
| 19   | Huawei Mate 7（MT7-CL00）           |      |
| 20   | Huawei nova（CAZ-TL10）             |      |
| 21   | Huawei Mate S（CRR-UL00）           |      |
| 22   | Huawei Maimang 6（RNE-AL00）           |      |
| 23   | Huawei P7（P7-L07）                 |      |
| 24   | Huawei P8 （GRA-UL10）        |      |
| 25   | Huawei P8（GRA-TL00）        |      |
| 26   | Huawei G7 Plus（RIO-TL00）          |      |
| 27   | Huawei G9 （VNS-AL00）        |      |
| 28   | Huawei P9（EVA-AL10）               |      |
| 29   | Huawei P9 Plus（VIE-AL10）          |      |
| 30   | Huawei P10（VTR-AL00）              |      |
| 31   | Huawei Mate8（NXT-AL10）            |      |
| 32   | Huawei Mate9（MHA-AL00）            |      |
| 33   | Huawei Mate9 Pro（LON-AL00）        |      |
| 34   | Huawei Mate10（ALP-AL00）           |      |
| 35   | Huawei Mate10 Pro（BLA-AL00）       |      |
| 36   | Huawei Honor8（FRD-AL00）            |      |
| 37   | Huawei Honor9（STF-AL10）            |      |
| 38   | Huawei HonorV8（KNT-AL10）           |      |
| 39   | Huawei HonorV9（DUK-AL20）           |      |
| 40   | Huawei HonorV10（BKL-AL20）          |      |
| 41   | Huawei nova2S（HWI-AL00）           |      |
| 42   | Xiaomi 2        |      |
| 43   | Xiaomi 2A       |      |
| 44   | Xiaomi 2S                 |      |
| 45   | Xiaomi 3                  |      |
| 46   | Xiaomi 3 |      |
| 47   | Xiaomi 4           |      |
| 48   | Xiaomi 4C                 |      |
| 49   | Redmi 1S |      |
| 50   | Redmi 1S                 |      |
| 51   | Redmi 2                  |      |
| 52   | Redmi 2A       |      |
| 53   | Redmi 3        |      |
| 54   | Redmi 3X       | HOMEキーなど非対応       |
| 55   | Redmi 3S                 |      |
| 56   | Redmi 4        |      |
| 57   | Redmi 4A       |      |
| 58   | Redmi Note         |      |
| 59   | Redmi Note         |      |
| 60   | Redmi Note        |      |
| 61   | Redmi Note 3       |      |
| 62   | Redmi Note 2       |      |
| 63   | Xiaomi Note               |      |
| 64   | Redmi Note 4X  |      |
| 65   | Xiaomi Max      |      |
| 66   | Xiaomi Note2    |      |
| 67   | Redmi Note 2             |      |
| 68   | Redmi Note 4             |      |
| 69   | Xiaomi 5C       | HOMEキーなど非対応       |
| 70   | Redmi Note 3      |      |
| 71   | Xiaomi 5                  |      |
| 72   | Xiaomi Note                   |      |
| 73   | Xiaomi Note 3             |      |
| 74   | Xiaomi 5S                 |      |
| 75   | Xiaomi 6        |      |
| 76   | Xiaomi MIX      |      |
| 77   | Xiaomi MIX 2    |      |
| 78   | OPPO A31                |      |
| 79   | OPPO A33      |      |
| 80   | OPPO A37      |      |
| 81   | OPPO A53                |      |
| 82   | OPPO A57      |      |
| 83   | OPPO A59      |      |
| 84   | OPPO A59s     |      |
| 85   | OPPO R7                 |      |
| 86   | OPPO R7s                   |      |
| 87   | OPPO R1C（R8207）          |      |
| 88   | OPPO 1107               |      |
| 89   | OPPO R9s Plus |      |
| 90   | OPPO R9 Plus            |      |
| 91   | OPPO R9s（R9s）            |      |
| 92   | OPPO R9（R9m）             |      |
| 93   | OPPO R11      |      |
| 94   | OPPO R11 Plus |      |
| 95   | OPPO R11s     |      |
| 96   | OPPO R11s Plus|      |
| 97   | vivo Y23L     |      |
| 98   | vivo Y27      |      |
| 99   | vivo Y31A     |      |
| 100  | vivo Y33      |      |
| 101  | vivo Y37      |      |
| 102  | vivo V3       |      |
| 103  | vivo Y51A     |      |
| 104  | vivo Y55A     | キーイベント非対応、textエラー   |
| 105  | vivo Y66      |      |
| 106  | vivo Y67      | HOMEキーなど非対応       |
| 107  | vivo Xplay5             |      |
| 108  | vivo X6S                |      |
| 109  | vivo X7       |      |
| 110  | vivo X7 Plus  |      |
| 111  | vivo X9（X9i）| HOMEキーなど非対応       |
| 112  | vivo X9 Plus  |      |
| 113  | vivo X9s      |      |
| 114  | vivo X9s Plus |      |
| 115  | vivo Xplay5                |      |
| 116  | vivo X20      |      |
| 117  | vivo X20 Plus       | HOMEキーなど非対応       |
| 118  | Samsung Galaxy S3（GT-I9300）        |      |
| 119  | Samsung Galaxy S4（GT-I9507V）       |      |
| 120  | Samsung GalaxyS4（GT-I9508V）        |      |
| 121  | Samsung Galaxy A5 2016（SM-A5108）   |      |
| 122  | Samsung Galaxy J7 2016（SM-J7108）   |      |
| 123  | Samsung Galaxy A8（SM-A8000）        |      |
| 124  | Samsung Galaxy Note 3（SM-N9002）    |      |
| 125  | Samsung Galaxy A9（SM-A9000）        |      |
| 126  | Samsung Galaxy Note 4（SM-N9109W）   |      |
| 127  | Samsung Galaxy S5（SM-G9008W）       | use ADB orientation必須  |
| 128  | Samsung Galaxy Note 5（SM-N9200）    |      |
| 129  | Samsung Galaxy Note 8（SM-N9500）    |      |
| 130  | Samsung Galaxy S6（SM-G9209）        |      |
| 131  | Samsung Galaxy S6 Edge（SM-G9250）   |      |
| 132  | Samsung Galaxy S7（SM-G9308）        |      |
| 133  | Samsung Galaxy S7 Edge（SM-G9350）   |      |
| 134  | Samsung Galaxy S8（SM-G9500）        |      |
| 135  | Google Pixel 3       |      |
| 136  | Google Pixel 3 xl      |      |
| 137  | Google Pixel 3a        |      |
| 138  | Google Pixel 3a xl       |      |
| 139  | Google Pixel 4       |      |

#### 対応エミュレーター（2020/01時点）
| No. | エミュレーター                          |
|------|----------------------------------|
| 1    | iTools           |
| 2    | BlueStacks          |
| 3    | AVD          |