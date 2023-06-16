import requests, json

def searchAddress(text): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {
        'query': text,
        'analyze_type' : 'similar'
        }
    rsp = requests.get('https://dapi.kakao.com/v2/local/search/address', 
                       headers=headers, 
                       params=data
                    )
    
    return rsp.json()

response = searchAddress('전북 삼성동 100')

formatted_json = json.dumps(response, indent=4, ensure_ascii=False)
print(formatted_json)

def searchregion(): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'x': '126.92909933485126',
            'y' : '36.77176975242896'}
    rsp = requests.get('https://dapi.kakao.com/v2/local/geo/coord2regioncode', 
                       headers=headers, 
                       params=data
                    )
    
    return rsp.json()

response = searchregion()

formatted_json = json.dumps(response, indent=4, ensure_ascii=False)
print(formatted_json)

#좌표로 주소 변환
def searchasd(): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'x':'127.423084873712',
            'y':'37.0789561558879'}
    rsp = requests.get('https://dapi.kakao.com/v2/local/geo/coord2address', 
                       headers=headers, 
                       params=data
                    )
    
    return rsp.json()

response = searchasd()
formatted_json = json.dumps(response, indent=4, ensure_ascii=False)
print(formatted_json)


def searchkeword(text): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'query': text}
    rsp = requests.get('https://dapi.kakao.com/v2/local/search/keyword', 
                       headers=headers, 
                       params=data
                    )
    
    return rsp.json()

response = searchkeword('맛집')
formatted_json = json.dumps(response, indent=4, ensure_ascii=False)
print(formatted_json)


def searchcategory(): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'category_group_code': 'MT1'}
    rsp = requests.get('https://dapi.kakao.com/v2/local/search/category', 
                       headers=headers, 
                       params=data
                    )
    
    return rsp.json()

response = searchcategory()
formatted_json = json.dumps(response, indent=4, ensure_ascii=False)
print(formatted_json)

