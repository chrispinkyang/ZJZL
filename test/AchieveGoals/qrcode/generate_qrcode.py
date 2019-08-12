def generate_qrcode(username,goal_id):
    logging.info("generate qrcode")
    access_token = cache.get('token')
    if access_token is None:
        logging.info("get access_token")
        status, access_token = get_access_token()
        if status:
            cache.set('token', access_token)
        else:
            raise RuntimeError("get access token failure")
    req_url = "https://api.weixin.qq.com/wxa/getwxacodeunlimit"
    scene="?id={}".format(goal_id)
    data = {
            "scene": scene,
            "page": "pages/confirmTarget/confirmTarget",
            "width": 250,
            "is_hyaline": True
    }

    querystring = {"access_token": access_token}

    headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
        }

    response = requests.request("POST", req_url, data=json.dumps(data), headers=headers, params=querystring,stream=True)

    if response.status_code == 200:
        filename="_".join(["qrcode",username,str(goal_id)])+'.jpeg'
        filepath = os.path.join(settings.BASE_DIR, 'media/qrcode',filename)
        #imgBuf=io.BytesIO(response.content)
        #img=Image.open(imgBuf)
        #img=img.resize((106,106),Image.ANTIALIAS)
        #img.save(filepath)
        with open(filepath,'wb') as f:
            for chunk in response.iter_content(512):
                f.write(chunk)
        return os.path.join("qrcode",filename)
    else:
        pass

if __name__ == '__main__':
    username = 'oAUG94qYKfRFs6WZLZUFkChTnQN8'
    req_url = "https://api.weixin.qq.com/wxa/getwxacodeunlimit"
    data:{'scene': '?id=20', 'page': 'pages/confirmTarget/confirmTarget', 'width': 250, 'is_hyaline': True}
    headers:{'Cache-Control': 'no-cache', 'Content-Type': 'application/json'}
    querystring:{'access_token': '12_tUqv419hK6xo1rBOAiijbgbczg96nOIJ5IwIdXomkuIuerJj5dDAqVx-ik8Egm2LgKl_IW2frIgTW6krViOZLfkiAsmDiKsL8gOOapjS7rZuzsad83EYOFKWJtI1RUXYvVp-5ho8qodlGcODGVOdAGAXMF'}
    response = requests.request("POST", req_url, data=json.dumps(data), headers=headers, params=querystring,stream=True)
    print(response)