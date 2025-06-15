# 大気汚染物質広域監視システムのAPIを利用

# 環境省大気汚染物質広域監視システム そらまめくん
# https://soramame.env.go.jp/

import requests

APP_URL = "https://soramame.env.go.jp/soramame/api/data_search"
params = {
    "Start_YM": "202506", # 取得開始年月 (必須)
    "End_YM": "202506", # 取得終了年月 (オプション 指定しない場合は現在の年月)
    "TDFKN_CD": "13",  # 東京都 (必須)
    "REQUEST_DATA": "TEMP,SO2,NO" # 取得項目の属性名 TEMP:気温, SO2:二酸化硫黄, NO:一酸化窒素 (オプション)
}

response = requests.get(APP_URL, params=params)


# apiのパラメータで指定できる期間が月単位で、レスポンスデータが1時間単位で出てくるので、データ取得にかなり時間がかかります。
data = response.json()
print(data)