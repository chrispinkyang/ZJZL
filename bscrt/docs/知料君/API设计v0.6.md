站点: 193.112.36.39

全局认证:
Authorization:Token

# 登录接口:

INTERFACE:/api/login
    
METHOD:POST

REQUEST PARAM:
    
	{
    "code":"abedefjf"
    "userImg":avatar_url,
    "userName":nickname
    }
    
RESPONSE:
    
	{
    "token":"abedefg",
    "openid":"12234536"
    }

# Form Id收集

METHOD:POST

INTERFACE: /api/form_ids/

request:

	{
	"form_id":
	"prepay_id":
    }

response:

	{
	"msg": "succeed",
    "status": 0,
    "result": { "update formId success!"}
	}

#统一支付接口:

INTERFACE:/api/unifiedorder/

request:

未确定支付功能前:保证有question\_id即可正确返回trade_no(空)

	{
        "body":订单描述,
        "total_fee":订单金额,
        "question_id":question_id
    }

response:

	{
	'trade_no': ""
	}

# 去打听:

model: question(问题)

## 添加问题:

INTERFACE:/api/questions/

AUTHORIZATION:Token <string>

request:

	{
	"title": "test 180815",
	"content": "我就试试",
	"is_anonymous": 0,
	"duration": 12,
	"trade_no": "",
	"amount":20,
	"pictures":[
	"cbcc/cvhdc.jpeg",
	"cbcc/cvhdc.jpeg"
	]
	}

Response:

	{
    "status": 0,
    "msg": "succeed",
    "result": {
        "id": 15,
        "userImg": "https://wx.qlogo.cn/mmopen/vi_32/xWtjZibhkibwp6XJ00BXOLOaTJsf3COkBfC5EmAoEnRsqucPBY1lLV6KWliapbriazCkkrCTsYg4hWnb9yeRsDZosA/132",
        "nickname": "吖浩",
        "title": "test 180815",
        "content": "我就试试",
        "amount": 20,
        "createdTime": "2018-08-15 15:21:49",
        "expiredTime": "2018-08-16 03:21:49",
        "status": 1,
        "forward_count": 0,
        "is_anonymous": 0,
        "pm_status": "0",
        "pictures": [
            "cbcc/cvhdc.jpeg",
            "cbcc/cvhdc.jpeg"
        ],
        "is_expired": false
    }
	}

## 上传问题图片

METHOD: POST

INTERFACE: /api/ques_pictures/

AUTHORIZATION:Token <string>

request:
	
	{
	'image':<二进制编码>
	}

response:

	{
	'image':hyperlink-url,
	'uploadTime':
	}



# 添加回答:

method:POST

INTERFACE: /api/answers/

request:

	{
	'question_id':
	'content': 
	'is_anonymous': #0:不匿名,1:匿名
	}

response:

	{
	"msg": "succeed",
    "status": 0
    "result": {
        "id": 6,
        "question_id": 15,
        "user_id": 1,
        "is_anonymous": 0,
        "userImg": null,
        "nickname": null,
        "content": "我就试试回答",
        "money_paid": 0,
        "is_accepted": false,
        "createdTime": "2018-08-15 15:41:35",
        "pictures": ['jhchsc.jpeg','chjshc.jpeg','cjhvcc.jpeg']
    },
    
	}
	
## 如果重复回答
response:
	{
    "status": 1,
    "msg": "You have answered this question"
	}

## 上传回答图片

METHOD: POST

INTERFACE: /api/aswr_pictures/

AUTHORIZATION:Token <string>

request:
	
	{
	'image':<二进制编码>
	}

response:

	{
	'image':hyperlink-url,
	'uploadTime':
	}


# 修改回答:

METHOD:PUT

INTERFACE: /api/answers/<answer_id>/

request:

	{
	'content':
	'is_anonymous':
	'pictures':[]#json数组
	}

response:

	{
    "result": {
        "id": 6,
        "question_id": 15,
        "user_id": 1,
        "is_anonymous": 0,
        "userImg": null,
        "nickname": null,
        "content": "我就试试修改回答",
        "money_paid": 0,
        "is_accepted": false,
        "createdTime": "2018-08-15 15:41:35",
        "pictures": [
            "mymymy.gif"
        ]
    },
    "msg": "succeed",
    "status": 0
	}

# 查看回答:

method:get

INTERFACE:/api/answers/<answer_id>/

response:

	{
    "id": 1,
    "question_id": 2,
    "user_id": 1,
    "is_anonymous": 0,
    "userImg": null,
    "nickname": null,
    "content": "try to answer.",
    "money_paid": 0,
    "is_accepted": false,
    "createdTime": "2018-08-09 11:21:45",
    "pictures": ['jhchsc.jpeg','chjshc.jpeg','cjhvcc.jpeg']
	}


# 我的提问:

method:get

INTERFACE: /api/questions/

response:

	{
    "result": [
        {
            "id": 11,
            "userImg": "https://wx.qlogo.cn/mmopen/vi_32/xWtjZibhkibwp6XJ00BXOLOaTJsf3COkBfC5EmAoEnRsqucPBY1lLV6KWliapbriazCkkrCTsYg4hWnb9yeRsDZosA/132",
            "nickname": "吖浩",
            "title": "dfdfdgdfgd",
            "content": "ddfvdfdfd",
            "amount": null,
            "createdTime": "2018-08-14 14:33:31",
            "expiredTime": "2018-08-14 23:33:31",
            "status": 0,
            "forward_count": 0,
            "is_anonymous": 0,
            "pm_status": null,
            "pictures": [
                "http://193.112.36.39/media/upload/question/wx66d63dc560d6172b.o6zAJs-PQRbzjZKw4IQ8iQ53DcqE.gxWyOJlwZfSj289fcbd859ea_Vc5CZLz.png"
            ],
            "is_expired": true
        },
        {
            "id": 12,
            "userImg": "https://wx.qlogo.cn/mmopen/vi_32/xWtjZibhkibwp6XJ00BXOLOaTJsf3COkBfC5EmAoEnRsqucPBY1lLV6KWliapbriazCkkrCTsYg4hWnb9yeRsDZosA/132",
            "nickname": "吖浩",
            "title": "dssdfds",
            "content": "sdfsdvvdsv",
            "amount": null,
            "createdTime": "2018-08-14 18:19:09",
            "expiredTime": "2018-08-15 05:19:09",
            "status": 1,
            "forward_count": 0,
            "is_anonymous": 0,
            "pm_status": null,
            "pictures": [
                "http://193.112.36.39/media/upload/question/wx66d63dc560d6172b.o6zAJs-PQRbzjZKw4IQ8iQ53DcqE.ydwzXAvXQtfe289fcbd859ea_dO9CfiF.png"
            ],
            "is_expired": true
        },
        {
            "id": 14,
            "userImg": "https://wx.qlogo.cn/mmopen/vi_32/xWtjZibhkibwp6XJ00BXOLOaTJsf3COkBfC5EmAoEnRsqucPBY1lLV6KWliapbriazCkkrCTsYg4hWnb9yeRsDZosA/132",
            "nickname": "吖浩",
            "title": "陈俊豪",
            "content": "在哪里？",
            "amount": 1,
            "createdTime": "2018-08-14 18:30:51",
            "expiredTime": "2018-08-15 12:30:51",
            "status": 1,
            "forward_count": 0,
            "is_anonymous": 0,
            "pm_status": "0",
            "pictures": [
                "http://193.112.36.39/media/upload/question/wx66d63dc560d6172b.o6zAJs-PQRbzjZKw4IQ8iQ53DcqE.a7siPzSqAIia289fcbd859ea_Bd0jTz6.png"
            ],
            "is_expired": true
        },
        {
            "id": 15,
            "userImg": "https://wx.qlogo.cn/mmopen/vi_32/xWtjZibhkibwp6XJ00BXOLOaTJsf3COkBfC5EmAoEnRsqucPBY1lLV6KWliapbriazCkkrCTsYg4hWnb9yeRsDZosA/132",
            "nickname": "吖浩",
            "title": "test 180815",
            "content": "我就试试",
            "amount": 20,
            "createdTime": "2018-08-15 15:21:49",
            "expiredTime": "2018-08-16 03:21:49",
            "status": 1,
            "forward_count": 0,
            "is_anonymous": 0,
            "pm_status": "0",
            "pictures": [
                "cbcc/cvhdc.jpeg",
                "cbcc/cvhdc.jpeg"
            ],
            "is_expired": false
        }
    ],
    "msg": "succeed",
    "status": 0
	}

# 问题详情:

method:get

INTERFACE:/api/question/<question_id>/

Response:

	{
    "result": {
        "id": 15,
        "userImg": "https://wx.qlogo.cn/mmopen/vi_32/xWtjZibhkibwp6XJ00BXOLOaTJsf3COkBfC5EmAoEnRsqucPBY1lLV6KWliapbriazCkkrCTsYg4hWnb9yeRsDZosA/132",
        "nickname": "吖浩",
        "title": "test 180815",
        "content": "我就试试",
        "amount": 20,
        "createdTime": "2018-08-15 15:21:49",
        "expiredTime": "2018-08-16 03:21:49",
        "status": 1,
        "forward_count": 0,
        "is_anonymous": 0,
        "pm_status": "0",
        "pictures": [
            "cbcc/cvhdc.jpeg",
            "cbcc/cvhdc.jpeg"
        ],
        "is_expired": false,
		"forwarders":[
			{
			'nickname':"chjdbcd",
			'userImg':"cvhdcbdcd.jpeg"
			},
			{
			'nickname':"chjdbcd",
			'userImg':"cvhdcbdcd.jpeg"
			}
			]
        "answers": [ #数组返回所有答案
            {
                "id": 6,
                "question_id": 15,
                "user_id": 1,
                "is_anonymous": 0,
                "userImg": null,
                "nickname": null,
                "content": "我就试试修改回答",
                "money_paid": 0,
                "is_accepted": false,
                "createdTime": "2018-08-15 15:41:35",
                "pictures": [
                    "mymymy.gif"
                ]
            },
			{
                "id": 1,
                "question_id": 2,
                "user_id": 3,
                "is_anonymous": 0,
                "userImg": null,
                "nickname": null,
                "content": "try to answer.",
                "money_paid": 0,
                "is_accepted": false,
                "createdTime": "2018-08-09 11:21:45",
                "pictures": []
            }
        ]
    },
    "msg": "succeed",
    "status": 0
	}



# 转发关注问题:

INTERFACE:/api/follow/

METHOD: POST

request:

	{
	"question_id":15
	}

response:
	
	{
    "result": {
        "id": 4,
        "follower_id": 1,
        "question_id": 15,
        "nickname": "吖浩",
        "userImg": "https://wx.qlogo.cn/mmopen/vi_32/xWtjZibhkibwp6XJ00BXOLOaTJsf3COkBfC5EmAoEnRsqucPBY1lLV6KWliapbriazCkkrCTsYg4hWnb9yeRsDZosA/132",
        "amount": "20.0",
        "status": "1",
        "is_expired": false,
        "is_answered": true
    },
    "msg": "succeed",
    "status": 0
	}


# 去回答(查看关注问题列表):

METHOD: GET

INTERFACE: /api/follow/

response:

	{
    "status": 0,
    "result": [
        {
            "id": 6,
            "userImg": null,
            "nickname": null,
            "title": "chris test",
            "content": "just a test",
            "amount": null,
            "createdTime": "2018-08-10 18:03:29",
            "expiredTime": "2018-08-11 04:03:29",
            "status": 0,
            "forward_count": 0,
            "is_anonymous": 0,
            "pm_status": null,
            "pictures": [],
            "is_expired": true
        },
        {
            "id": 7,
            "userImg": null,
            "nickname": null,
            "title": "chris GGG",
            "content": "just a test",
            "amount": null,
            "createdTime": "2018-08-10 18:03:46",
            "expiredTime": "2018-08-11 04:03:46",
            "status": 0,
            "forward_count": 0,
            "is_anonymous": 0,
            "pm_status": null,
            "pictures": [],
            "is_expired": true
        },
        {
            "id": 8,
            "userImg": null,
            "nickname": null,
            "title": "busy friday",
            "content": "dull monday",
            "amount": null,
            "createdTime": "2018-08-10 18:04:22",
            "expiredTime": "2018-08-11 04:04:22",
            "status": 0,
            "forward_count": 0,
            "is_anonymous": 0,
            "pm_status": null,
            "pictures": [],
            "is_expired": true
        }
    ],
    "msg": "succeed"
	}

# 我的钱包

method:GET

INTERFACE: /api/wallet/

response:

	{
    "status": 0,
    "result": [
        {
            "balance": 2000
        }
    ],
    "msg": "succeed"
	}

# 话费充值-钱包功能

METHOD: POST

INTERFACE: /api/wallet/recharge/

REQUEST:

	{
	'phoneno':'18819451571', #充值号码
	'amount':300, #消耗积分
	}

response:

	{
    "msg": "succeed",
    "status": 0,
    "result": "Submit order: recharge 1000 yuan to phone 18819451571 successful"
	}

# 分发红包

METHOD: POST

INTERFACE:/api/questions/<question_id>/distribute/

REQUEST:

	{
	#answer_id
	"selected_answers":[6,7,8]
	}

RESPONSE:

	{
    "msg": "succeed",
    "result": "successful distribution",
    "status": 0
	}


# 记录转发:

METHOD: GET

INTERFACE : api/questions/<question_id>/forward/

response:

	{
    "result": "forward record success",
    "msg": "succeed",
    "status": 0
	}

# 收支记事本

METHOD: GET

INTERFACE: api/transaction_records/

response:

	{
    "status": 0,
    "msg": "succeed",
    "result": {
        "income": [
			{
                "id": 1,
                "from_nickname": "吖浩",
                "from_userImg": "https://wx.qlogo.cn/mmopen/vi_32/xWtjZibhkibwp6XJ00BXOLOaTJsf3COkBfC5EmAoEnRsqucPBY1lLV6KWliapbriazCkkrCTsYg4hWnb9yeRsDZosA/132",
                "operateType": "income",
                "amount": 20,
                "description": "红包分发",
                "trade_no": null,
                "status": "done",
                "createdTime": "2018-08-15 15:21:49",
                "finishedTime": "2018-08-15 15:21:49",
                "user": 2,
                "question": 15
            },
			{
                "id": 1,
                "from_nickname": "吖浩",
				"from_userImg": "https://wx.qlogo.cn/mmopen/vi_32/
                "operateType": "pay",
                "amount": 20,
                "description": "红包分发",
                "trade_no": null,
                "status": "done",
                "createdTime": "2018-08-15 15:21:49",
                "finishedTime": "2018-08-15 15:21:49",
                "user": 2,
                "question": 15
            }
			],
        "pay": [
            {
                "id": 1,
                "from_nickname": "吖浩",
				"from_userImg": "https://wx.qlogo.cn/mmopen/vi_32/
                "operateType": "pay",
                "amount": 20,
                "description": "红包分发",
                "trade_no": null,
                "status": "done",
                "createdTime": "2018-08-15 15:21:49",
                "finishedTime": "2018-08-15 15:21:49",
                "user": 2,
                "question": 15
            }
        ]
    }
	}