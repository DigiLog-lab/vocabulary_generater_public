import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

CRED = os.environ['GOOGLE_API_KEY_gemini']


def generate(input):

      genai.configure(api_key=CRED)
 
      # モデルを指定する
      model = genai.GenerativeModel('gemini-pro')

      chat = model.start_chat()
      prompt = (input +
            '上記の文章から文法上重要なキーワードや単語や熟語を抜き出し、50問程度の一問一答の問題を作成してください。'+
            'そして問題文と答えをペアにしたcsvスクリプトを作成してください。'+
            'csvのフォーマットは次のようにしてください。'+
            '作成した問題,解答'+
            'ただし、問題と解答の間にはカンマを必ず入れてください。'+
            '英文が来た時は、問題を英語で書き、答えを日本語で書いてください'+
            '日本語が来たときは、答えも問題も日本語で書いてください。'+
            '上記のプロンプトを厳格に守って生成してください。')

      response = chat.send_message(prompt)
      return response.text
    

