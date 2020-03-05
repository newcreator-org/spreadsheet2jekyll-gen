# spreadsheet2jekyll-gen
Google Spreadsheetで作成した図表をJekyllの記事形式でジェネレートするスクリプト

---

## 必要なツール

- Python3

## 起動方法

`./services.csv` を用意してください。

今回の場合は

```
追加日,追加時間,カテゴリ,コンテンツ形式,タイトル（事業名）,運営元団体名,URL,無料期限（あれば）,概要
2020-03-05,13:39:00,science,動画,科学技術広報研究会 臨時休校対応特別企画,科学技術広報研究会,https://sites.google.com/view/jacst-for-kids/home,,様々な研究機関に所属する広報担当者が、科学技術に関連する様々なムービーをピックアップ。
2020-03-05,13:39:00,programming,オンライン授業,LOGY,株式会社Yoki,https://logy.app/202003-covid-19?fbclid=IwAR0Lvv4hry_dcC5zQFXQEA8yPXrb1vaWLlR3BD1Rv7iF0kcyDvuSGYhvxo0,4月上旬まで割引,
2020-03-05,13:39:00,daily_studying,書籍,進研ゼミ,ベネッセ,https://www.benesse.co.jp/zemi/homestudy/,3月末？,自宅学習教材等の一部無償提供
2020-03-05,13:39:00,programming,アプリ,N予備校,株式会社ドワンゴ,,,
.
.
.

```

といった形のファイルを想定しています。

```
$ python3 main.py
```

を実行すると `./markdown/` 以下にファイルが生成されます
