import pandas as pd
import folium
#画像保存用
import asyncio
from pyppeteer import launch
import os

#国データ
url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
world_geo = f'{url}/world-countries.json'

df= pd.read_csv("normalizedCountryPlantDada.csv")

for i in range(2,52):#50個マップ作製する
    
    print(df.columns[i])
    # 地図生成
    folium_map = folium.Map(location=(35.690921,0),zoom_start=2)
    # 地図に色を塗る
    folium.Choropleth(
    geo_data=world_geo,
    name='choropleth',
    data=df,# 描画データ
    columns=["3-letter country codes",df.columns[i]],# ["国コード", "値の列"]
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
        # HTML ファイルを開く
        await page.goto(f'file:///C:/Users/wagta/Documents/SONY_CSL_RA/Python_exe_folder/git_sample/{html_path}')
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