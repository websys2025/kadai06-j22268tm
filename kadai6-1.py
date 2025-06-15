import requests

APP_ID = "9b55c7e76dad03ebe208a9aacde6bd49e7760394"
API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId": "0002114519",  # 作物統計調査 作況調査
    "metaGetFlg": "Y", # メタ情報有無
    "cntGetFlg": "Y", # 件数取得フラグ
    "explanationGetFlg": "Y", # 解説情報有無
    "annotationGetFlg": "Y", # 注釈情報有無	
    "sectionHeaderFlg": "0", # セクションヘッダフラグ csv用
    "replaceSpChars": "0", # 特殊文字の置換	
    "lang": "J",  # 日本語を指定

}


response = requests.get(API_URL, params=params)
data = response.json()
print(data)