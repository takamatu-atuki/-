import requests

API_KEY = '3814f32bff0da938'
GENRE_API = 'https://webservice.recruit.co.jp/hotpepper/genre/v1/'
AREA_API = 'https://webservice.recruit.co.jp/hotpepper/large_area/v1/'

def get_genres():
    try:
        res = requests.get(GENRE_API, params={'key': API_KEY, 'format': 'json'})
        res.raise_for_status()  # ステータスコードがエラーなら例外
        data = res.json()
        return data['results'].get('genre', [])
    except Exception as e:
        print("ジャンル取得エラー:", e)
        return []

def get_areas():
    try:
        res = requests.get(AREA_API, params={'key': API_KEY, 'format': 'json'})
        res.raise_for_status()
        data = res.json()
        return data['results'].get('large_area', [])
    except Exception as e:
        print("エリア取得エラー:", e)
        return []

