import pandas as pd
import folium
#画像保存用
import asyncio
from pyppeteer import launch
import os
import shutil

#国データ
url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
world_geo = f'{url}/world-countries.json'

df= pd.read_csv("normalizedCountryPlantDada.csv")

for i in range(2,df.shape[1]):#50個マップ作製する
    
    print(df.columns[i])
    # 地図生成
    folium_map = folium.Map(location=(35.690921,0),zoom_start=2)
    # 地図に色を塗る
    folium.Choropleth(
    geo_data=world_geo,
    name='choropleth',
    data=df,# 描画データ
    columns=["3letterCountryCode",df.columns[i]],# ["国コード", "値の列"]
    key_on='feature.id',
    fill_color='Greens',# 色指定
    fill_opacity=0.7,# 色の透明度
    line_opacity=0.2,#国境線の透明度
    legend_name=df.columns[i]#凡例
    ).add_to(folium_map)

    folium.LayerControl().add_to(folium_map)

    # 地図保存
    folium_map.save(df.columns[i]+'.html')

    async def html_to_png(html_path, output_path):
        browser = await launch()
        page = await browser.newPage()
        # 現在の作業ディレクトリを取得
        current_dir = os.getcwd()
        # HTML ファイルへの相対パスを作成
        relative_html_path = os.path.join(current_dir, html_path)
        # HTML ファイルを開く
        await page.goto(f'file://{relative_html_path}')
        # ページのスクリーンショットのための画面サイズ指定？
        await page.setViewport({
            'width': 1050,
            'height': 750,#世界地図がすべて入るように手動で調整した
            'deviceScaleFactor': 1
        })
        # ページを PNG 画像として保存
        await page.screenshot({'path': output_path})

        # ブラウザを閉じる
        await browser.close()

    # パスを指定
    html_path = df.columns[i]+'.html'
    output_path = df.columns[i]+'.png'

    # HTML を描画し、PNG で保存
    asyncio.get_event_loop().run_until_complete(html_to_png(html_path, output_path))

    # HTML ファイルを削除
    os.remove(html_path)

#出力したpngのヒートマップを一つのファイルにまとめる
def move_png_files(source_dir, destination_dir):
    # フォルダが存在しない場合は作成する
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # ソースディレクトリ内のファイルを走査
    for filename in os.listdir(source_dir):
        if filename.endswith('.png'):
            # PNGファイルの場合、新しいフォルダに移動する
            source_path = os.path.join(source_dir, filename)
            destination_path = os.path.join(destination_dir, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {destination_dir}")

# 現在のディレクトリを取得
current_directory = os.getcwd()
# 移動元ディレクトリと移動先ディレクトリのパスを指定
source_directory = current_directory
destination_directory = os.path.join(current_directory, 'heatmapFolder')
# PNGファイルを移動する
move_png_files(source_directory, destination_directory)