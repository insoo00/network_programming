import requests
from PIL import Image, ImageDraw
from io import BytesIO

API_URL = 'https://dapi.kakao.com/v2/vision/adult/detect'

def detect_product(image_url): # app_key와 이미지 파일의 URL을 POST로 전송하여 상품 검출을 수행 
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = { 'image_url' : image_url }
    resp = requests.post(API_URL, headers=headers, data=data) 
    return resp.json() # 검출 결과를 딕셔너리로 변환하여 반환


if __name__ == "__main__":
    # 상품 검출할 이미지의 URL 
    IMAGE_URL ='https://p.kakaocdn.net/th/talkp/wmbOXVOIV9/aKtMoWYi4P4NrK5nrCodk0/s2rwz0_640x640_s.jpg'
    detection_result = detect_product(IMAGE_URL)
    # print(detection_result)
    result = detection_result['result']
    for key, value in result.items():
        print(f"{key}: {value}")

    