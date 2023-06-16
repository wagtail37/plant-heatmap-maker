# plant-heatmap-maker
国別の植物ヒートマップを作成する

### やり方
１．[GBIF](https://www.gbif.org/ja/)からヒートマップを作成したい植物のオカレンスデータをダウンロードし、occurrenceDataSampleFolderファイルに入れる

２．getPlantCountryInfo.pyで国別のデータを抽出

３．normalizePlantData.pyで正規化

４．saveCountryMapFoliumToPng.pyでヒートマップを作成、作製したヒートマップはheatmapFolderに保存
