from flask import Flask ,request ,render_template 
import scan
from google.cloud import vision
import os
import google.generativeai as genai
import generator
import os

app = Flask(__name__)

@app.route('/')
def menu():
     return render_template('index.html')

# https://(localhost等ドメイン)/upload
# 
@app.route('/upload', methods=['POST'])
def upload():
    if request.method=='POST':
        img = request.files['img_file']
        # 受け取った写真をOCRにかける
        scan_result = scan.scan_textbook(img)
        # OCRの文字列をもとにCSVファイルを作成してもらう
        result = generator.generate(scan_result)
        # 結果を表示
        return render_template('result.html',result=result)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)
