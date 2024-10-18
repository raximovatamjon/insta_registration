import requests
import json
def instadownloader(link):
     url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/"

     querystring = {"url":link}

     headers = {
          "X-RapidAPI-Key": "9684d516ebmshfdd0f57cdc9c9f8p190768jsn6e661bc23529",
          "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
     }

     response = requests.get(url, headers=headers, params=querystring)
     rest=json.loads(response.text)
     dict = {}
     if rest['type'] =='video':
          dict['type']='video'
          dict['media']=rest['media']
     print(rest,'\n',dict)

instadownloader('https://www.instagram.com/p/CIFEJvAlxkz/')