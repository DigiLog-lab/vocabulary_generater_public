import os
from google.cloud import vision
from google.oauth2 import service_account
from dotenv import load_dotenv


def scan_textbook(img):

    load_dotenv()

    cred = os.environ['CRED']

    # 認証情報を読み取る
    credentials = service_account.Credentials.from_service_account_file(cred)
    client = vision.ImageAnnotatorClient(credentials=credentials)
    content = img.read()

    # OCRを実行
    image = vision.Image(content=content)
    responce=client.text_detection(image=image)
    texts=responce.text_annotations[0].description
    return texts