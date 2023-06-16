import requests, json

def searchweb(text): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {
        'query': text,
        'sort' : 'accuracy',
        'page': 1,
        'size': 5
        
        }
    rsp = requests.get('https://dapi.kakao.com/v2/search/web', 
                       headers=headers, 
                       params=data
                    )
    
    return rsp.json()

response = searchweb('아이유')

formatted_json = json.dumps(response, indent=4, ensure_ascii=False)
print(formatted_json)

def searchvideo(text): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'query': text}
    rsp = requests.get('https://dapi.kakao.com/v2/search/vclip', 
                       headers=headers, 
                       params=data
                    )
    
    return rsp.json()

def searchimage(text): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'query': text}
    rsp = requests.get('https://dapi.kakao.com/v2/search/image', 
                       headers=headers, 
                       params=data
                    )
    
    return rsp.json()


def searchblog(text): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'query': text}
    rsp = requests.get('https://dapi.kakao.com/v2/search/blog', 
                       headers=headers, 
                       params=data
                    )
    
    return rsp.json()

