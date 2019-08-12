INTERFACE: /api/think/

METHOD: POST

Content-type: application/json

## 基本请求格式:

Request:

	{
	"uuid":"12345678",
	"ongoingservice":"Weather" # 还在进行中的服务,上下文功能,没有为None
	"text: "今天天气怎么样" # 查询语句
	"lang":"Mandarin"/"Cantonese" # 语言 该字段暂不使用
	}

## 电视控制:

### Example 1:

Request:


```python
{
"uuid": "12345678",
"ongoingservice": null,
"text": "帮我打开电视"
}
```


Response:
	
	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "已为您打开电视",
        "service": "Television",
        "intent": "power_on",
        "data": {
            "op_type": "power",
            "op_value": 1
        }
    }
	}

### example 2

Request:
	
	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "声音太大了"
	}

Response:
	
	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "已为您调低电视音量",
        "service": "Television",
        "intent": "volumn_down",
        "data": {
            "op_type": "volume",
            "op_value": "-"
        }
    }
	}

## 播放操作控制

### Example 1
Request:

	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "暂停"
	}

Response:
	
	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "暂停",
        "service": "PlayControl",
        "intent": "PlayControl",
        "data": {
            "op_type": "control",
            "op_value": "stop"
        }
    }
	}

### Example 2

Request:
	
	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "快进"
	}

Response:

	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "快进",
        "service": "PlayControl",
        "intent": "PlayControl",
        "data": {
            "op_type": "control",
            "op_value": "forward"
        }
    }
	}

## 播放内容控制(频道/节目)

### Example 1
Request:

	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "我想看湖南卫视"
	}

Response:

	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "为您播放湖南卫视",
        "service": "PlayContent",
        "intent": "PlayContent",
        "data": {
            "op_type": "content",
            "op_value": "湖南卫视"
        }
    }
	}

### Example 2

Request:

	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "有没有快乐大本营"
	}

Response:
	
	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "为您播放快乐大本营",
        "service": "PlayContent",
        "intent": "PlayContent",
        "data": {
            "op_type": "content",
            "op_value": "快乐大本营"
        }
    }
	}

# 智能家居功能

## 设置场景

### Example 1

Request:

	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "设置回家模式"
	}

Response:

	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "已为你设置回家模式",
        "service": "Scene",
        "intent": "set_presence_mode",
        "data": {
            "op_type": "scene",
            "op_value": "presence"
        }
    }
	}

### Example 2

request:

	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "设置离家模式"
	}

response:

	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "为您设置离家模式",
        "service": "Scene",
        "intent": "set_absence_mode",
        "data": {
            "op_type": "scene",
            "op_value": "absence"
        }
    }
	}

## 空调功能

### Example 1
Request:
	
	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "太热了"
	}

Response:

	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "已为您调低空调温度",
        "service": "Airconditioner",
        "intent": "temp_down",
        "data": {
            "op_type": "temp",
            "op_value": "-"
        }
    }
	}

### Example 2

Request:

	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "把空调调到25度"
	}

Response:
	
	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "已为您把空调调到25度",
        "service": "Airconditioner",
        "intent": "temp_set",
        "data": {
            "op_type": "temp",
            "op_value": "25"
        }
    }
	}


## 窗帘功能

### Example 1

Request:
	
	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "打开窗帘"
	}
	

Response:
	
	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "为您打开窗帘",
        "service": "Curtain",
        "intent": "curtain_on",
        "data": {
            "op_type": "draw",
            "op_value": 100
        }
    }
	}

### Example 2(未识别操作)

Request:

	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "窗帘嘻嘻哈哈"
	}

Response:

	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "未能识别您对窗帘的操作",
        "service": "Curtain",
        "intent": "unmatched",
        "data": {
            "op_type": "unmatched",
            "op_value": "unmatched"
        }
    }
	}

## 音乐功能

### Example 1
Request:
	
	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "我想听吻别"
	}

Response:
	
	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "为您播放张学友的吻别",
        "service": "Music",
        "intent": "吻别",
        "data": {
            "op_type": "download_url",
            "op_value": "http://dl.stream.qqmusic.qq.com/C400004RDW5Q2ol2jj.m4a?vkey=8DD64EE1033721CDF19699DF23415EEA4610DAAF1AF7170B2F888C5E3A85FFA76D19D146677B6D6C052A277B1BE729BBE083E687D73CFBEE&guid=5115346800&fromtag=30"
        }
    }
	}

### Example 2
Request:
	
	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "给我放一首林俊杰的歌"
	}

Response:

	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "为您播放林俊杰的不为谁而作的歌",
        "service": "Music",
        "intent": "不为谁而作的歌",
        "data": {
            "op_type": "download_url",
            "op_value": "http://dl.stream.qqmusic.qq.com/C400002K4xqW4A7m7q.m4a?vkey=66838B4F1EA745E3DFEC9EE30FAAD2C34955DB35F814150D535C747ADD3A4A4DA2810DFE6B1519190D8F5CE010EB765D7DF425A57019D333&guid=5115346800&fromtag=30"
        }
    }
	}

## 天气功能:

Request:
	
	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "今天珠海天气怎么样"
	}

Response:
	
	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "今天珠海全天多云，气温25℃ ~ 31℃，空气质量优，有无持续风向微风，气温较高，请尽量避免午后高温时段的户外活动。",
        "service": "weather",
        "intent": "query",
        "data": [
            {
                "city": "珠海",
                "date": "2018-09-20",
                "date_for_voice": "今天",
                "img": "http://aiui-res.ufile.ucloud.com.cn/weather/01.png",
                "lastUpdateTime": "2018-09-20 11:00",
                "tempHigh": "31℃",
                "tempLow": "25℃",
                "tempRange": "25℃ ~ 31℃",
                "weather": "多云",
                "weatherDescription": "气温较高，请尽量避免午后高温时段的户外活动。",
                "weatherType": 1,
                "week": "周四",
                "wind": "无持续风向微风",
                "windLevel": 0
            },
            {
                "city": "珠海",
                "date": "2018-09-21",
                "date_for_voice": "明天",
                "img": "http://aiui-res.ufile.ucloud.com.cn/weather/01.png",
                "lastUpdateTime": "2018-09-20 11:00",
                "tempHigh": "32℃",
                "tempLow": "25℃",
                "tempRange": "25℃ ~ 32℃",
                "weather": "多云",
                "weatherDescription": "气温较高，请尽量避免午后高温时段的户外活动。",
                "weatherType": 1,
                "week": "周五",
                "wind": "无持续风向微风",
                "windLevel": 0
            },
            {
                "city": "珠海",
                "date": "2018-09-22",
                "date_for_voice": "后天",
                "img": "http://aiui-res.ufile.ucloud.com.cn/weather/01.png",
                "lastUpdateTime": "2018-09-20 11:00",
                "tempHigh": "30℃",
                "tempLow": "26℃",
                "tempRange": "26℃ ~ 30℃",
                "weather": "多云转阵雨",
                "weatherDescription": "有点热，适合穿短袖短裙等夏季清凉衣物。",
                "weatherType": 1,
                "week": "周六",
                "wind": "无持续风向微风",
                "windLevel": 0
            },
            {
                "city": "珠海",
                "date": "2018-09-23",
                "date_for_voice": "23号",
                "img": "http://aiui-res.ufile.ucloud.com.cn/weather/03.png",
                "lastUpdateTime": "2018-09-20 11:00",
                "tempHigh": "30℃",
                "tempLow": "25℃",
                "tempRange": "25℃ ~ 30℃",
                "weather": "阵雨",
                "weatherDescription": "有点热，适合穿短袖短裙等夏季清凉衣物。",
                "weatherType": 3,
                "week": "周日",
                "wind": "无持续风向微风",
                "windLevel": 0
            },
            {
                "city": "珠海",
                "date": "2018-09-24",
                "date_for_voice": "24号",
                "img": "http://aiui-res.ufile.ucloud.com.cn/weather/03.png",
                "lastUpdateTime": "2018-09-20 11:00",
                "tempHigh": "29℃",
                "tempLow": "24℃",
                "tempRange": "24℃ ~ 29℃",
                "weather": "阵雨",
                "weatherDescription": "有点热，适合穿短袖短裙等夏季清凉衣物。",
                "weatherType": 3,
                "week": "下周一",
                "wind": "无持续风向微风",
                "windLevel": 0
            },
            {
                "city": "珠海",
                "date": "2018-09-25",
                "date_for_voice": "25号",
                "img": "http://aiui-res.ufile.ucloud.com.cn/weather/03.png",
                "lastUpdateTime": "2018-09-20 11:00",
                "tempHigh": "30℃",
                "tempLow": "25℃",
                "tempRange": "25℃ ~ 30℃",
                "weather": "阵雨",
                "weatherDescription": "有点热，适合穿短袖短裙等夏季清凉衣物。",
                "weatherType": 3,
                "week": "下周二",
                "wind": "无持续风向微风",
                "windLevel": 0
            },
            {
                "city": "珠海",
                "date": "2018-09-26",
                "date_for_voice": "26号",
                "img": "http://aiui-res.ufile.ucloud.com.cn/weather/03.png",
                "lastUpdateTime": "2018-09-20 11:00",
                "tempHigh": "30℃",
                "tempLow": "26℃",
                "tempRange": "26℃ ~ 30℃",
                "weather": "阵雨转小雨",
                "weatherDescription": "有点热，适合穿短袖短裙等夏季清凉衣物。",
                "weatherType": 3,
                "week": "下周三",
                "wind": "无持续风向微风",
                "windLevel": 0
            }
        ]
    }
	}

## OpenQA

### Example 1

Request:

	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "我饿了"
	}

Response:
	
	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "忍着呗，就当减肥了！",
        "service": "openQA",
        "intent": "chat",
        "data": {
            "op_type": "speech",
            "op_value": "忍着呗，就当减肥了！"
        }
    }
	}


### Example 2

Request:

	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "今天心情不好"
	}

Response:

	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "别不高兴了，我希望每天都能看到你的微笑。",
        "service": "openQA",
        "intent": "chat",
        "data": {
            "op_type": "speech",
            "op_value": "别不高兴了，我希望每天都能看到你的微笑。"
        }
    }
	}

## 解析失败

Request:
	
	{
	"uuid": "12345678",
	"ongoingservice": null,
	"text": "嘻嘻哈哈唧唧咋咋"
	}

Response:
	
	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "speechtext": "抱歉，您能再说一遍吗？",
        "service": "Unclear",
        "intent": "Unclear",
        "data": {
            "op_type": "speech",
            "op_value": "抱歉，您能再说一遍吗？"
        }
    }
	}