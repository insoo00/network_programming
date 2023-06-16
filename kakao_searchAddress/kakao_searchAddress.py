import requests, json

def searchAddress(text): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {
        'query': text,
        # 'analyze_type' : 'exact',
        'page': 1,
        'size': 5
        
        }
    rsp = requests.get('https://dapi.kakao.com/v2/local/search/address', 
                       headers=headers, 
                       params=data
                    )
    
    return rsp.json()

response = searchAddress('능허대로 343')

formatted_json = json.dumps(response, indent=4, ensure_ascii=False)
print(formatted_json)
