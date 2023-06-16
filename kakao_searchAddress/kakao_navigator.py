import requests, json

def searchnavigator(): # GET 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = {'origin': '127.11015314141542,37.39472714688412',
            'destination': '127.10824367964793,37.401937080111644'}
    rsp = requests.get('https://apis-navi.kakaomobility.com/v1/directions', 
                       headers=headers, 
                       params=data
                    )
    
    return rsp.json()

# response = searchnavigator()
# formatted_json = json.dumps(response, indent=4, ensure_ascii=False)
# print(formatted_json)


#다중 경유지 길찾기
def searchnavigator(): # POST 요청
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY),
            #    "Content-Type": "application/json"
               }
    data = {"origin": {
        "x": "127.11024293202674",
        "y": " 37.394348634049784"
    }, "destination": {
        "x": "127.10860518470294",
        "y": "37.401999820065534"
    },"waypoints": [
        {
            "name": "name0",
            "x": 127.11341936045922,
            "y": 37.39639094915999
        }
    ],
    }
    rsp = requests.post('https://apis-navi.kakaomobility.com/v1/waypoints/directions', 
                       headers=headers, 
                       json = data
                    )
    
    return rsp.json()

response = searchnavigator()
formatted_json = json.dumps(response, indent=4, ensure_ascii=False)
print(formatted_json)