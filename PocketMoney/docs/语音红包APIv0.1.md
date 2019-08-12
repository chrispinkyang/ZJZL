## 未完成(2018.10.24)

1. 讯飞语音听写功能,粤语等方言识别功能需要以项目为单位申请.目前识别引擎为普通话.
2. 真实交易环境中的完整性测试.
3. 微信模板消息通知,模板消息未确定.代码中业务逻辑相关部分有注释.
4. 微信支付,企业付款等支付功能与小程序的绑定.
5. 提现功能(即企业付款)完成编码,未同步到生产服务器.
6. 支付后微信回调通知接口(/paynotify)未测试.

## 登录(v0.2 接收头像和昵称)

INTERFACE : /api/login/

METHOD: POST

RESQUEST:
	
	{
	"code":"ahcvscb",
	"userInfo": # 包含从微信获取的所有userInfo
	}

RESPONSE:

	{
	"token":"hjvdcasgcashc"
	"openid":"dcjbac"
	}

## 统一支付(v0.3 无需发送total_fee)

INTERFACE : /api/unifiedorder/

METHOD: POST

RESQUEST:
	
	{
        "body":订单描述,
        "pm_id":pm_id
    }

RESPONSE:

	{
	"appId": appid, 
	"timeStamp": timestamp,
	"nonceStr": nonce_str, 
	"package": package,
    "signType": sign_type,
	"paySign":
	"trade_no":
	}


## 收集Form_id

INTERFACE:/api/form_ids/

METHOD: POST

REQUEST:

    {
        "form_id":
        "prepay_id":
    }



## FAQ | FAQ

INTERFACE : /api/faq/

METHOD: GET

RESPONSE:

	{
    "msg": "succeed",
    "status": 0,
    "result": [
        {
            "id": 1,
            "question": "这是一条Question",
            "answer": "这是一条Answer",
            "createdTime": "2018-10-09 10:26:00"
        },
        {
            "id": 2,
            "question": "这是第二条QUESTION",
            "answer": "这是第二条ANSWER",
            "createdTime": "2018-10-09 10:30:00"
        }
    ]
	}

## TEXT | 文本消息

### 创建自定义文本

INTERFACE: /api/text/

METHOD: POST

REQUEST:

	{
	"content": "这是一条来自chris的文本"
	}

RESPONSE:

创建成功

	{
    "status": 0,
    "result": {
        "id": 23,
        "content": "这又是一条来自chris的文本"
    },
    "msg": "succeed"
	}

创建失败(有敏感词):

	{
    "msg": "消息包含敏感词汇",
    "status": 1
	}

### 获取所有模板文本(v0.2更新)

INTERFACE: /api/text/

METHOD: GET

RESPONSE:


	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "热门": [
            {
                "id": 6,
                "content": "钱唔系问题，问题系冇钱。"
            }
        ],
        "歌词": [],
        "TVB": [],
        "节日": [],
        "表白": [
            {
                "id": 5,
                "content": "啊？真喺嘅？你好犀利啊~"
            }
        ],
        "急口令": [],
        "整蛊": [
            {
                "id": 1,
                "content": "多谢老窦"
            },
            {
                "id": 2,
                "content": "妖，好衰咖~"
            },
            {
                "id": 3,
                "content": "有冇人可怜下我哩嗰孤家寡佬啊？"
            },
            {
                "id": 4,
                "content": "皇上，臣妾真喺冤枉啊~"
            }
        ],
        "本尊独创": [
            {
                "id": 23,
                "content": "这又是一条来自chris的文本"
            }
        ]
    }
	}


### 随机获取

INTERFACE: /api/text/pick/

METHOD: GET

RESPONSE:

	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "id": 5,
        "content": "啊？真喺嘅？你好犀利啊~"
    }
	}

## pocketmoney | 语音红包

注: 

整体流程:
先**创建红包**, 前端再向后端发起**统一支付**.

### 红包状态
-2: 被举报
-1: 已过期
0: 未激活
1: 已激活,进行中

### 添加payback字段,表示红包是否到期之后未取完,并已返还发起者钱包.

### 创建:

INTERFACE: /api/pocketmoney/

METHOD: POST

REQUEST:

	{
	"text_id": 1, # 获取文本消息的id
	"amount":10, # 金额总额(净红包金额,不包含服务费)
	"num":5 # 红包个数
	}

RESPONSE:

	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "id": 1,
        "nickname": null, # 用户昵称
        "avatar_url": null, # 用户头像
        "amount": 10, # 红包金额
        "remaining": 0, # 剩余金额
        "num": 5,# 总红包个数
        "left_num": 0, # 剩余红包个数
        "status": 0, # 红包状态: -2:被举报;-1:已冻结(过期/分发完);0:未激活;1:活跃
		"payback":True/False # 红包返还状态
        "createdTime": "2018-10-09 11:20:02", # 创建时间
        "expiredTime": "2018-10-10 11:20:02", # 过期时间
        "user": 1, # 创建者
        "text": 1 # 文本消息
    }
	}

### 红包详情

INTERFACE: /api/pocketmoney/<id>/

METHOD: GET

RESPONSE:

	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "id": 3,
        "nickName": "吖浩",
        "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/tem4sxTqBNYhNjRqpNCB5TMSD9fp9sGUmJiaI1nia9rNFoNibNibia1GqWQfXMYudds3KlC8x9ianfUjM2v4wWo48DcQ/132",
        "content": "妖，好衰咖~", 
        "amount": 10, # 总金额
        "remaining": 9.9, # 剩余金额
        "num": 100, # 红包个数
        "left_num": 99, # 剩余红包个数
        "status": 1, # 红包状态
        "createdTime": "2018-10-11 15:31:00",#创建时间
        "expiredTime": "2018-10-12 15:31:00",#过期时间
        "user": 3,
        "text": 2,
        "answers": [
            {
                "id": 23,
                "nickName": "吖浩",
                "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/tem4sxTqBNYhNjRqpNCB5TMSD9fp9sGUmJiaI1nia9rNFoNibNibia1GqWQfXMYudds3KlC8x9ianfUjM2v4wWo48DcQ/132",
                "audio": "/media/audio/wx74f741a75dce159e.o6zAJs-PQRbzjZKw4IQ8iQ53DcqE.sU7qvj6yjjmsab39991cc1d7bb0223488b_Gs1bZts.mp3",
                "duration": 0,
                "correct": 0,
                "status": 1,
                "received": "2.00",
                "createdTime": "2018-10-18 15:52:00",
                "user": 3,
                "pm": 3
            }
        ]
    }
	}


### 个人中心 -- 我发出的红包

INTERFACE: /api/pocketmoney/

METHOD: GET

RESPONSE:
	
	{
    "msg": "succeed",
    "status": 0,
    "result": {
        "count": 1,
        "total_amount": 10,
        "data": [
            {
                "id": 7,
                "nickName": null,
                "avatarUrl": null,
                "content": "妖，好衰咖~",
                "amount": 10,
                "remaining": 0,
                "num": 5,
                "left_num": 0,
                "status": 0,
                "createdTime": "2018-10-19 10:53:37",
                "expiredTime": "2018-10-20 10:53:37",
                "user": 1,
                "text": 2
            },
			{
                "id": 2,
                "nickname": null,
                "avatar_url": null,
				"content": "妖，好衰咖~",
                "amount": 20,
                "remaining": 10,
                "num": 5,
                "left_num": 5,
                "status": 1,
                "createdTime": "2018-10-09 11:24:00",
                "expiredTime": "2018-10-10 11:24:00",
                "user": 1,
                "text": 2
            }
        ]
    }
	}


## Answers| 回答领取红包

### 新建回答

INTERFACE: /api/answers/

METHOD:POST

	{
        "pm_id":1,# 红包ID
		"audio": # 录音文件
		"duration": #录音时长
    }

失败情况归纳:

	{
    "status": 1,
    "msg": ""
	}

msg字段值(中文):

- 你已领取过这个红包
- 问题已失效

### 个人中心 -- 我收到的红包

INTERFACE: /api/answers/

METHOD:GET

RESPONSE:
	
	{
    "status": 0,
    "result": {
        "nickName": "吖浩",
        "data": [
            {
                "id": 23,
                "nickName": "吖浩",
                "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/tem4sxTqBNYhNjRqpNCB5TMSD9fp9sGUmJiaI1nia9rNFoNibNibia1GqWQfXMYudds3KlC8x9ianfUjM2v4wWo48DcQ/132",
                "audio": "http://139.199.63.137/media/audio/wx74f741a75dce159e.o6zAJs-PQRbzjZKw4IQ8iQ53DcqE.sU7qvj6yjjmsab39991cc1d7bb0223488b_Gs1bZts.mp3",
                "duration": 0, # 录音时长
                "correct": 0, # 正确率
                "status": 1, # 回答状态 1:匹配成功 (只返回成功的回答)
                "received": "2.00",# 该回答获得金额 字符串类型
                "createdTime": "2018-10-18 15:52:00",
                "user": 3,
                "pm": 3
            }
        ],
        "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/tem4sxTqBNYhNjRqpNCB5TMSD9fp9sGUmJiaI1nia9rNFoNibNibia1GqWQfXMYudds3KlC8x9ianfUjM2v4wWo48DcQ/132",
        "total_amount": "2.00", # 总金额 字符串类型
        "count": 1 # 领取个数
    },
    "msg": "succeed"
	}


## 举报

INTERFACE: /api/pocketmoney/<pm_id>/report/
METHOD: POST
REQUEST:
	
	{
	"report_type": 1
	}

举报类型:
 	
- 0: '其它'
- 1: '色情'
- 2: '造谣'
- 3: '政治'