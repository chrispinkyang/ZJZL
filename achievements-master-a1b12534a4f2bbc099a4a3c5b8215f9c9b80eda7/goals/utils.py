from django.conf import settings
from rest_framework import response,exceptions
import PIL.Image as Image
import PIL.ImageFont as ImageFont
import PIL.ImageDraw as ImageDraw

import os
import requests
import io

#from goals.models import Wallet,TransactionRecord,MyUser

FLAG= "够朋友，就帮我完成这个目标..."

def render_response(result=None):
    res={
			'msg': "succeed",
			'status': 0,
			'result':result,
		}
    print(res)
    return response.Response(res)


def render_exceptions(msg=None,status=1):
    res={
		'msg':msg ,
		'status': status,
	}
    print(res)
    return response.Response(res)

class Poster(object):
    def __init__(self,goal):
        self.goal=goal


    def text_wrap(self,text,font,width,gap):
        lines = []
        # If the width of the text is smaller than image width
        # we don't need to split it, just add it to the lines array
        # and return
        if font.getsize(text)[0] <= width- gap * 2:
            lines.append(text)
        else:
            # split the line by spaces to get words
            words = [word for word in text]
            i = 0
            # append every word to a line while its width is shorter than image width
            while i < len(words):
                line = ''
                while i < len(words) and font.getsize(line + words[i])[0] <= 620 - 36 * 2:
                    line = line + words[i]
                    # line = line + words[i] + " "
                    i += 1
                if not line:
                    line = words[i]
                    i += 1
                # when the line gets longer than the max width do not append the word,
                # add the line to the lines array
                lines.append(line)
        return lines

    def make_goal_poster(self):
        font30 = ImageFont.truetype("NotoSansCJK-Regular.ttc", 30)
        font32 = ImageFont.truetype("NotoSansCJK-Regular.ttc", 32)
        #font36 = ImageFont.truetype("NotoSansCJK-Regular.ttc", 36)
        font26 = ImageFont.truetype("NotoSansCJK-Regular.ttc", 26)
        font50 = ImageFont.truetype("NotoSansCJK-Regular.ttc", 50)
        template=self.goal.poster_template
        if template:
            print("template:{}".format(template))
            template_file_name=os.path.split(template.path)[1]
            backImg = Image.open(os.path.join(settings.BASE_DIR,'media/poster_template',template_file_name))
        else:
            print("random choice template")
            backImg=Image.open(os.path.join(settings.BASE_DIR,"media/poster_template/background.png"))
        qrcode=self.goal.qrcode
        if qrcode:
            print("qrcode:{}".format(qrcode))
            qrcode_file_name=os.path.split(qrcode.path)[1]
            qrcode=Image.open(os.path.join(settings.BASE_DIR,"media/qrcode",qrcode_file_name))
            r,g,b,a=qrcode.split()
            backImg.paste(qrcode,(236,438),mask=a)
        draw = ImageDraw.Draw(backImg)
        username=self.goal.user.nickname
        if not username:
            username=str(self.goal.user)
        title="{}的目标:".format(username,)
        deadline="{}止".format(self.goal.finishedTime.strftime("%Y-%m-%d"))
        draw.text([282, 104], title, font=font32, fill="#FFFFFF")

        #text = "本月读完两本书<时间简史>,<三体>,<羞答答的玫瑰静悄悄的开>"
        # text="Rose is Rose Rose Rose Rose Rose Or what a fucking day"
        content=self.goal.content
        textwidth, textheight = font50.getsize(content)
        lines = self.text_wrap(content, font50,750,36)

        y = 194

        last_line=lines.pop()
        if lines:
            for line in lines:
                draw.text([36, y], line, font=font50, fill="#FFFFFF")
                y += textheight


        x=(750-36*2-font50.getsize(last_line)[0])/2+36
        draw.text([x, y], last_line, font=font50, fill="#FFFFFF")


        draw.text([310, 290],deadline , font=font26, fill="#F4FFFF")
        draw.text([180, 384], FLAG, font=font30, fill="#FFFFFF")
        #draw.text([36 + font26.getsize("奖金")[0], 864], str(self.conMoney), font=font26, fill="#FF569A")
        #draw.text([36 + font26.getsize("奖金40")[0], 864], "元已经准备好，看谁来拿", font=font26, fill="#B7C7D5")
        filename=username+str(self.goal.id)+'.png'
        filedir=os.path.join(settings.BASE_DIR,'media/poster/')
        filepath=os.path.join(filedir,filename)
        backImg.save(filepath, 'png')
        return filepath

    def make_result_poster(self,result):
        font42 = ImageFont.truetype("NotoSansCJK-Regular.ttc", 42)
        font34 = ImageFont.truetype("NotoSansCJK-Regular.ttc", 34)
        font26 = ImageFont.truetype("NotoSansCJK-Regular.ttc", 26)
        if result:
            backImg = Image.open(os.path.join(settings.BASE_DIR, 'media/poster_template', "success.png"))
        else:
            backImg = Image.open(os.path.join(settings.BASE_DIR, 'media/poster_template', "failure.png"))
        draw = ImageDraw.Draw(backImg)
        content=self.goal.content
        textwidth1, textheight1 = font42.getsize(content)
        lines = self.text_wrap(content, font42,648,36)
        x1=36
        y1 = 286

        last_line = lines.pop()
        if lines:
            for line in lines:
                draw.text([36, y1], line, font=42, fill="#000000")
                y1 += textheight1

        x = (648 - 36 * 2 - font42.getsize(last_line)[0]) / 2 + 36
        draw.text([x, y1], last_line, font=font42, fill="#000000")

        avatar_url=self.goal.user.avatar_url
        response=requests.get(avatar_url,stream=True)
        imgBuf=io.BytesIO(response.content)
        avatar = Image.open(imgBuf)
        backImg.paste(avatar,(250,464))
        username=self.goal.user.nickname

        textwidth2,textheight2=font34.getsize(username)
        x2=(648-textwidth2)/2
        y2=634
        draw.text([x2,y2],username,font=font34,fill="#586871")

        deadline = "{}止".format(self.goal.finishedTime.strftime("%Y-%m-%d"))
        draw.text([264, 820], deadline, font=font26, fill="#9FB5C8")

        filename = "_".join([username,str(self.goal.id),'result'])+ '.png'
        filedir = os.path.join(settings.BASE_DIR, 'media/poster/')
        filepath = os.path.join(filedir, filename)
        backImg.save(filepath, 'png')
        return filepath


















