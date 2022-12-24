# mp3-splitter
MP3形式のファイルを無音部分で分割しポーズを入れるClIツール。ポーズを挿入した音声をMP3形式で出力する。

ポーズの長さは直前の音声部分と同じ（調節機能は今後導入するか検討中）。

## Requirements
* Python>=3.5
* ffmpeg

## How to Use
### セットアップ

リポジトリをクローン

```
git clone git@github.com:iced-penguin/mp3-splitter.git
```

必要なパッケージをインストール

```
pip install -r requirements.txt
```

入っていなければffmpegをインストール

```sh
# For mac OS
brew install ffmpeg
```

### 基本的な使い方

```
python main.py [optionis] [src] [dst]
```

* src: 元ファイルのパス
* dst: ポーズ挿入後のファイルパス

e.g.

```
python main.py src.mp3 dst.mp3
```

### オプション

`-t`, `--threshold`: 分割に使用する無音部分の長さの閾値を設定する（ミリ秒）

```sh
python main.py -t 300 src.mp3 dst.mp3
```

`--ignore-first`: 最初の空白にはポーズを挿入しない

タイトル読み上げ直後はポーズを入れたくない時などに

```sh
python main.py --ignore-first src.mp3 dst.mp3
```

ヘルプ

```
python main.py -h
```