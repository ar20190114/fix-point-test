# No.1
監視ログファイルを読み込み、故障状態のサーバアドレスとそのサーバの故障期間を出力するプログラムを作成せよ。
出力フォーマットは任意でよい。
なお、pingがタイムアウトした場合を故障とみなし、最初にタイムアウトしたときから、次にpingの応答が返るまでを故障期間とする。

# No.2
ネットワークの状態によっては、一時的にpingがタイムアウトしても、一定期間するとpingの応答が復活することがあり、
そのような場合はサーバの故障とみなさないようにしたい。
N回以上連続してタイムアウトした場合にのみ故障とみなすように、設問1のプログラムを拡張せよ。
Nはプログラムのパラメータとして与えられるようにすること。

# No.3
サーバが返すpingの応答時間が長くなる場合、サーバが過負荷状態になっていると考えられる。
そこで、直近m回の平均応答時間がtミリ秒を超えた場合は、サーバが過負荷状態になっているとみなそう。
設問2のプログラムを拡張して、各サーバの過負荷状態となっている期間を出力できるようにせよ。mとtはプログラムのパラメータとして与えられるようにすること。

# No.4
ネットワーク経路にあるスイッチに障害が発生した場合、そのスイッチの配下にあるサーバの応答がすべてタイムアウトすると想定される。
そこで、あるサブネット内のサーバが全て故障（ping応答がすべてN回以上連続でタイムアウト）している場合は、
そのサブネット（のスイッチ）の故障とみなそう。
設問2または3のプログラムを拡張して、各サブネット毎にネットワークの故障期間を出力できるようにせよ。


# Usage
 
Please create python code named "index.py".
 
Run "index.py"
 
```bash
python index.py
```

# Text Case
 ```bash
20201019133124,10.20.30.1/16,2
20201019133125,10.20.30.2/16,1
20201019133134,192.168.1.1/24,10
20201019133135,192.168.1.2/24,5
20201019133224,10.20.30.1/16,522
20201019133225,10.20.30.2/16,1
20201019133234,192.168.1.1/24,8
20201019133235,192.168.1.2/24,15
20201019133324,10.20.30.1/16,-
20201019133325,10.20.30.2/16,2
20201019133424,10.20.30.1/16,10
20201019133524,10.20.30.1/16,500
20201019133624,10.20.30.1/16,-
20201019133724,10.20.30.1/16,-
20201019133824,10.20.30.1/16,20
20201019133924,10.20.30.1/16,20
20201019134024,10.20.30.1/16,20
20201019134124,10.20.30.1/16,20
```
