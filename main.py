import pandas as pd
import datetime

services = pd.read_csv('./services.csv')
date = str(datetime.date.today())

for index,row in services.iterrows():
    f = open('./markdown/' + date + '-' + row['タイトル（事業名）'] + '.md', 'w', encoding='utf-8')
    f.write('---\n')
    f.write('layout: post\n')
    f.write('title: \'' + row['タイトル（事業名）'] + '\'\n')
    f.write('target: \'' + row['ターゲット'] + '\'\n')
    f.write('format: \'' + row['コンテンツ形式'] + '\'\n')
    f.write('description: \'' + row['概要'] + '\'\n')
    f.write('date: ' + row['追加日'] + ' ' +row['追加時間'] + ' +0900\n')
    f.write('categories: ' + row['カテゴリ'] + '\n')
    f.write('by: \'' + row['運営元団体名'] + '\'\n')
    f.write('service: \'' + row['URL'] + '\'\n')
    f.write('image-url: \'' + row['画像URL'] + '\'\n')
    f.write('---\n')

    # f.write('#' + row['タイトル（事業名）'] + '\n')
    # f.write(row['概要'] + '\n')

    f.close()