import requests


def get_geo_info(city: str, type_info: str = 'coordinates'):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {'geocode': city, 'format': 'json'}

    response = requests.get(url, params)
    json = response.json()

    try:
        if type_info == 'coordinates':
            point_str = json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            point_array = [float(x) for x in point_str.split(' ')]
            return point_array

        elif type_info == 'country':
            return json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
                'GeocoderMetaData']['AddressDetails']['Country']['CountryName']
    except Exception as GetInfoError:
        raise GetInfoError


def map_image(coords=None, map_type="map", add_params: str = None):
    if coords:
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords[0]},{coords[1]}&l={map_type}"
    else:
        map_request = f"http://static-maps.yandex.ru/1.x/?l={map_type}"

    if add_params:
        map_request += f"&{add_params}"

    response = requests.get(map_request)
    if not response:
        raise ValueError

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except Exception as WriteError:
        print("Ошибка записи временного файла:", WriteError)
        raise WriteError
