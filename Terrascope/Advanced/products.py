def get_products(collection, startDate, endDate, bbox = None, tileId = None):
    import requests
    from urllib.parse import urljoin

    headers = {'Accept': 'application/json'}
    payload = {
        'collection': collection,
        'start': startDate.strftime('%Y-%m-%d'),
        'end': endDate.strftime('%Y-%m-%d'),
        'accessedFrom': 'MEP'
    }
    if bbox is not None:
        payload['bbox'] = bbox
    if tileId is not None:
        payload['tileId'] = tileId        
    response = requests.get(urljoin('https://services.terrascope.be/catalogue/', 'products'),
                            headers = headers,
                            params = payload)

    if response.status_code == requests.codes.ok:
        result = response.json()
        return result['features']
    else:
        response.raise_for_status()

def get_product_paths(products, band_name):
    paths = []
    for product in products:      
        for band in product['properties']['links']['data']:
            if band['title'] == band_name:
                paths.append(band['href'][7:])   
    return paths
