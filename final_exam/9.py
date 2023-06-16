import requests
from PIL import Image, ImageDraw
from io import BytesIO
from urllib import parse,request
import cv2

API_URL = 'https://dapi.kakao.com/v2/vision/thumbnail/crop'

def make_thumbnail(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(REST_API_KEY)}
    data = { 
            'image_url' : image_url,
            'width' : 200,
            'height': 200
        }
    resp = requests.post(API_URL, headers=headers, data=data) 
    return resp.json() # 검출 결과를 딕셔너리로 변환하여 반환

if __name__ == "__main__":
    IMAGE_URL ='https://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/07.jpg'
    makeThumbnail = make_thumbnail(IMAGE_URL)

    image_path = 'thumbnail.jpg'
    request.urlretrieve(makeThumbnail['thumbnail_image_url'], image_path)
    img = cv2.imread(image_path)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
