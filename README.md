# Browser Use Playground

Browser Useは、AIエージェントがウェブブラウザを自動で操作するためのPythonライブラリです。

公式サイト：https://browser-use.com/
リポジトリ：https://github.com/browser-use/browser-use

## Getting Started

packageをインストールします。

```sh
pip install -r requirements.txt
```

.envを作成します。

```sh
cp .env.example .env
```

スクリプトを実行すると、ブラウザ上でAgentが与えられたタスクを行います。

```sh
python agent.py
```

![](./agent_history.gif)
