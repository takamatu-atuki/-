from flask import Blueprint, render_template, request
import requests

main_routes = Blueprint('main', __name__)

API_KEY = '3814f32bff0da938'
BASE_URL = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/'


@main_routes.route('/')
def index():
    GENRE_API = 'https://webservice.recruit.co.jp/hotpepper/genre/v1/'
    AREA_API = 'https://webservice.recruit.co.jp/hotpepper/large_area/v1/'

    genre_res = requests.get(GENRE_API, params={'key': API_KEY, 'format': 'json'})
    area_res = requests.get(AREA_API, params={'key': API_KEY, 'format': 'json'})

    genre_data = genre_res.json()
    area_data = area_res.json()

    genres = genre_data['results'].get('genre', [])
    areas = area_data['results'].get('large_area', [])

    return render_template('index.html', genres=genres, areas=areas)



@main_routes.route('/search')
def search():
    GENRE_API = 'https://webservice.recruit.co.jp/hotpepper/genre/v1/'
    AREA_API = 'https://webservice.recruit.co.jp/hotpepper/large_area/v1/'

    genre_res = requests.get(GENRE_API, params={'key': API_KEY, 'format': 'json'})
    area_res = requests.get(AREA_API, params={'key': API_KEY, 'format': 'json'})

    genre_data = genre_res.json()
    area_data = area_res.json()

    genres = genre_data['results'].get('genre', [])
    areas = area_data['results'].get('large_area', [])

    return render_template('search.html', genres=genres, areas=areas)


@main_routes.route('/results', methods=['POST'])
def results():
    area = request.form.get('area')
    genre = request.form.get('genre')
    keyword = request.form.get('keyword')

    params = {
        'key': API_KEY,
        'large_area': area,
        'genre': genre,
        'keyword': keyword,
        'format': 'json'
    }

    res = requests.get(BASE_URL, params=params)
    data = res.json()

    shops = []
    if 'results' in data and 'shop' in data['results']:
        for s in data['results']['shop']:
            shops.append({
                'id': s['id'],
                'name': s['name'],
                'genre': s['genre']['name'],
                'area': s['large_area']['name'],
                'price': s['budget']['name'],
                'address': s['address'],
                'image': s['photo']['pc']['l'],
                'keywords': [s.get('station_name', ""), s['genre']['catch']]
            })

    return render_template('results.html', shops=shops)


@main_routes.route('/shop/<shop_id>', endpoint='shop_detail')
def shop_detail(shop_id):
    params = {
        'key': API_KEY,
        'id': shop_id,
        'format': 'json'
    }

    res = requests.get(BASE_URL, params=params)
    data = res.json()
    shop = data['results']['shop'][0] if 'results' in data and 'shop' in data['results'] else None

    if shop:
        shop['lat'] = shop.get('lat')
        shop['lng'] = shop.get('lng')

    return render_template('shop_detail.html', shop=shop)

