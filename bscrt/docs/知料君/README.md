ZJCHILINK CLOUD API Documentation
===================================

![ZJCHILINK](http://zjchilink.com/res/201710/11/3a4e6972cd2dd51f.png)

BASE URL:  https://aa.zjchilink.com
HTTP Port: 8084/
MQTT Port: 9880/1883
UDP  BC  : 9820(src)  9830(dst)
-----------------

>分页说明
请求数据为列表时，如果没有给出分页信息，默认每页显示10个条目，如果需要指定每页显示条目数量
，那么需要指定limit参数，如果指定页数则需要指定page参数

   
    limit:表示该页显示条目个数
    请求示例：http://192.168.0.240:8000/api/iot/messages/?limit=3&page=2
    响应示例：
    ""page": {
            "total_page": 3,
            "current_page": 2,
            "page_pieces": 3,
            "total_pieces": 9
        }

### 1. User management


#### 1.1 User - User - GET SMS verification code

    Endpoint 	    : /api/accounts/register_get_smscode/

    Request Type 	: POST

    Request Params  :
    {
    "username": "13825182430"
    }

    Response 	:
    {
        "status": status code,
        "msg":{
            "username": "username",
        },
        "desc":"status description"
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200001: Request SMS code success
    400001: The user has already existed
    400002: Phone number error
    400003: Request Params error

#### 1.2 User -  Endpoint for user registration(SMS mode).

    Endpoint 	    : /api/accounts/register_sms/

    Request Type 	: POST

    Request Params  :
    {
        "username": "username",
        "email": "none",
        "password": "password",
        "password_2": "password again",
        "sms_code": <sms code>,
        "first_name": "none",
        "last_name": "none"
    }

    Response 	:
    {
        "status": status code,
        "msg":{
            "username": "username",
            "email": "none",
            "password": "password",
            "password_2": "password again",
            "first_name": "none",
            "last_name": "none"
        },
        "desc":"status description"
    }

    HTTP status code: HTTP_201_CREATED

    status(status code):

    200002:Registration success.
    400004:Email already exists.
    400005:Password should be at least 8 characters long（MAX：32）.
    400006:Passwords doesn't match.
    400007:Username already exists.
    400008:Invite code is not valid / expired.
    400009:SMS validation code is invalid

    400003: Request Params error



#### 1.3 User -  Endpoint for user login.

    Endpoint 	    : /api/accounts/login/

    Request Type 	: POST

    Request Params  :
    {
        "username":"username",
        "password":"password",
        "language": "chs/cht/en",
        "uuid"    : "device uuid",
        "devtype" : "ios/android/pc/web/wechat/emb"
    }

    Response 	:
    {
        "msg": {
            "wechat_service": "",
            "ip_joined": "",
            "qq_service": "",
            "addr_joined": "guangzhou",
            "language": "chs/cht/en",
            "id": 2,
            "username": "18823360820",
            "first_name": "none",
            "last_name": "none",
            "last_login": null,
            "is_active": true,
            "email": "email",
            "date_joined": "2018-01-24T21:31:49.484597Z",
            "token": "811d00a468a3a1f8a6fe5fd7dafde55e6505b2f7"
            "avatar_url": "local:001",
            "signature": "签名内容",
            "extend_userinfo": "user@pass",
            "user_admin": false,
            "user_manager": false,
            "user_normal": true,
            "user_guest": false,
            "user_iot": false,
            "user_aacloud": false,
            "user_health": false
        },
        "status": status code,
        "desc":"status description"
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200003:Login success.
    400010:This username is not valid.
    400011:User not active.
    400012:Invalid credentials(Password error).
    400013:Please enter username or email to login.

    400003: Request Params error

#### 1.4 User - Retrieve User Profile / User Data

    Endpoint 	    : /api/accounts/user_get_profile/

    Request Type 	: GET

    Header          : Authorization = Token <token string>

    Request Params  :


    Response 	:
    {
        "msg": {
            "wechat_service": "",
            "ip_joined": "",
            "qq_service": "",
            "addr_joined": "guangzhou",
            "language": "chs/cht/en",
            "id": 2,
            "username": "18823360820",
            "first_name": "none",
            "last_name": "none",
            "last_login": null,
            "is_active": true,
            "email": "email",
            "date_joined": "2018-01-24T21:31:49.484597Z",
            "token": "811d00a468a3a1f8a6fe5fd7dafde55e6505b2f7"
            "avatar_url": "",
            "signature": "签名内容",
            "extend_userinfo": "user@pass",
            "user_admin": false,
            "user_manager": false,
            "user_normal": true,
            "user_guest": false,
            "user_iot": false,
            "user_aacloud": false,
            "user_health": false
        },
        "status": status code,
        "desc":"status description"
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200004:Retrieve User Profile success.
    401014:Token is not valid/
    400015:The user does not exist.
    400016:User not active.

    400003: Request Params error


#### 1.5 User -  Endpoint to reset password by the old password.

    Endpoint 	    : /api/accounts/password_reset_old_psw/

    Request Type 	: POST

    Request Params  :
    {
        "username": "username",
        "old_password": "old password",
        "new_password": "new password",
        "new_password_2": "new password_again"
    }

    Response 	:
    {
        "msg": {
            "password": "password",
            "username": "username"
        },
        "status": status code,
        "desc":"status description"
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200005:Reset password success.
    401017:Old password error.
    400018:The user does not exist.
    400019:Passwords do not match, try again.
    *400020:Invalid password, try again.
    400003: Request Params error


#### 1.6 User -  Endpoint to reset password by SMS verification(GET SMS verification code).

    Endpoint 	    : /api/accounts/password_reset_get_smscode/

    Request Type 	: POST

    Request Params  :
    {
    "username": "13825182430"
    }

    Response 	:
    {
        "status": status code,
        "msg":{
            "username": "username",
        },
        "desc":"status description"
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200001: Request SMS code success
    400001: The user has already existed
    400002: Phone number error
    400003: Request Params error


#### 1.7 User -  Endpoint to reset password by the SMS verification.

    Endpoint 	    : /api/accounts/password_reset_sms/

    Request Type 	: POST

    Request Params  :
    {
        "username": "username",
        "sms_code": <sms code>,
        "new_password": "new password",
        "new_password_2": "new password_again"
    }

    Response 	:
    {
        "msg": {
            "password": "password",
            "username": "username"
        },
        "status": status code
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200007:Reset password success.
    401024:sms code error.
    400025:The user does not exist.
    400026:Passwords do not match, try again.
    *400027:Invalid password, try again.
    400003: Request Params error


#### 1.8 User -  Endpoint to update user profile

    Endpoint 	    : /api/accounts/user_update_profile/

    Request Type 	: POST

    Header          : Authorization = Token <token string>

    Request Params  :

    {
        "profile":{
            "wechat_service": "wechat_service",
            "ip_joined": "ip_joined",
            "qq_service": "qq_service",
            "addr_joined": "addr_joined",
            "avatar_url": "avatar_url",
            "signature": "个人签名",
            "extend_userinfo":"user@pass"

        },
        "user":{
            "last_name":"你好中文",
            "email":"hello@163.com",
            "first_name": "first_name",
            "last_name": "last_name",
        }
    }


    Response 	:
    {
        "msg": {
            "wechat_service": "",
            "ip_joined": "",
            "qq_service": "",
            "addr_joined": "guangzhou",
            "language": "chs/cht/en",
            "id": 2,
            "username": "18823360820",
            "first_name": "none",
            "last_name": "none",
            "last_login": null,
            "is_active": true,
            "email": "email",
            "date_joined": "2018-01-24T21:31:49.484597Z",
            "token": "811d00a468a3a1f8a6fe5fd7dafde55e6505b2f7"
            "avatar_url": "",
            "signature": "签名内容",
            "extend_userinfo": "user@pass",
            "user_admin": false,
            "user_manager": false,
            "user_normal": true,
            "user_guest": false,
            "user_iot": false,
            "user_aacloud": false,
            "user_health": false
        },
        "status": status code,
        "desc":"status description"
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200008:Update user profile success.
    401028:Token is not valid/HTTP_401_UNAUTHORIZED.
    400029:User not active.
    400040:User not active.
    400003: Request Params error




#### 1.9 User -  Endpoint to update user avatar image

    Endpoint 	    : /api/accounts/user_update_avatar/

    Request Type 	: POST

    Header          : Authorization = Token <token string>

    Request Params  :
    {
        "image_type": "jpg/png/bmp",
        "image_size": "2097152(byte)",
        "image_name": "image name",
        "data_type": "base64/raw/hex",
        "image_data": "image data"
    }

    Response 	:
    {
        "msg": {
            "image_type": "jpg/png/bmp",
            "image_size": "2097152(byte)",
            "image_name": "image name",
            "data_type" : "base64/raw/hex",
            "avatar_url": "avatar url"
        },
        "status": status code,
        "desc":"status description"
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200009:Update user avatar image success.
    401030:Token is not valid/HTTP_401_UNAUTHORIZED.
    400031:Image format does not support.
    400032:Too big image size(MAX:720 x 720 MIN: 144 x 144)
    400033:User not active.
    400003: Request Params error





#### 1.10 User - Retrieve User avatar image

    Endpoint 	    : /api/accounts/user_get_avatar/user_id/avatar.jpg/

    Request Type 	: GET

    Header          : Authorization = Token <token string>

    Request Params  :


    Response(ERROR) :
    {
        "msg": {
        },
        "status": status cod,
        "desc":"status description"
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200010: Request success, return image.
    400034: Token is not valid.
    400035: User not active.
    400036: avatar not set
    400003: Request Params error

#### 1.11 User - 微信授权登录（第三方登录通用）
    说明: 每次授权登录前, 以微信user_id为参数向智联云获取登录账号。
         请求账号成功后, 按"1.3"登录接入进行登录, 密码为open_id+user_id(解码)

    Endpoint 	    : /api/accounts/user_get_username_external/user_id

    Request Type 	: GET

    Header          :

    Request Params  :


    Response:
    {
        "msg": {
            "wechat_service": "user_id",
            "language": "chs/cht/en",
            "id": 2,
            "username": "18823360820",
        },
        "status": status code,
        "desc":"status description"
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200011: Request success.
    400037: Token is not valid.
    400038: User not authorization.
    400039: User not active.
    400040: Email format error.
    400003: Request Params error.



#### 1.12 User - 微信授权注册（第三方登录通用）

    说明: 微信授权登录, 以微信user_id为参数向智联云获取登录账号结果为400036时, 说明
         该微信user_id尚未绑定手机注册。此时应按"1.2"进行注册,
    注意: 增加: "wechat_service": "user_id", 密码为open_id+user_id(解码)


### 2. Device management



#### 2.1 General data - manage iot general data (single)

   Endpoint 	    : /api/iot/iot_manage_view/

   Request Type 	: POST/PUT/DELETE/GET

   Header          : Authorization = Token <token string>

   Request:

   *GET  /api/iot/iot_manage_view/   get all the device related with this user
   
      filter param:[page|ver|type_sub|category|uuid|icon|title]
      filter format:/api/iot/iot_manage_view/?page=1&ver=0.0.1&...
         
   response:
   
    {
    "msg": {
        "page": {
            "total_page": 1,
            "current_page": 1,
            "page_pieces": 10,
            "total_pieces": 3
        },
        "data": [
            {
                "id": 10,
                "title": "4K智能管家",
                "ver": "0.0.1",
                "icon": "",
                "user_id": 9,
                "create_time": "2018-06-21 14:02:57",
                "update_time": "2018-06-21 14:02:57",
                "category": "gw",
                "type_sub": "AA01GW-UG",
                "uuid": "00158d00011d6087",
                "body": "4K智能管家",
                "perm": null,
                "authorization_id": null,
                "param": {
                    "id": 4,
                    "info_id": 10,
                    "zgb_short": null,
                    "zgb_ieee": "00158d0000d04701",
                    "zgb_ver": "v1.0.0",
                    "zgb_channel": null,
                    "zgb_status": null,
                    "status_id": null,
                    "ip": null,
                    "lng": null,
                    "devinfo": null,
                    "room_id": 6,
                    "floor_id": 5,
                    "unit_id": 4,
                    "env_thsensor_id": null,
                    "env_pmsensor_id": null,
                    "is_local_env": false,
                    "shortcut_dev_id1": null,
                    "shortcut_dev_id2": null,
                    "shortcut_dev_id3": null,
                    "shortcut_dev_id4": null,
                    "ap_ssid": null,
                    "access_ssid": null,
                    "access_pass": null,
                    "is_remind_devoff": false,
                    "remind_start_time": null,
                    "remind_stop_time": null
                }
            },
            {
                "id": 13,
                "title": "4K智能管家(POST)",
                "ver": "0.0.1",
                "icon": "",
                "user_id": 9,
                "create_time": "2018-07-18 10:05:14",
                "update_time": "2018-07-18 10:05:14",
                "category": "gw",
                "type_sub": "AA01GW-UG",
                "uuid": "00158d0000d04701",
                "body": "智能网关",
                "perm": null,
                "authorization_id": null,
                "param": {
                    "id": 7,
                    "info_id": 13,
                    "zgb_short": null,
                    "zgb_ieee": "00158d0000d04701",
                    "zgb_ver": "v1.0.0",
                    "zgb_channel": null,
                    "zgb_status": null,
                    "status_id": null,
                    "ip": null,
                    "lng": null,
                    "devinfo": null,
                    "room_id": 6,
                    "floor_id": 5,
                    "unit_id": 4,
                    "env_thsensor_id": null,
                    "env_pmsensor_id": null,
                    "is_local_env": false,
                    "shortcut_dev_id1": null,
                    "shortcut_dev_id2": null,
                    "shortcut_dev_id3": null,
                    "shortcut_dev_id4": null,
                    "ap_ssid": null,
                    "access_ssid": null,
                    "access_pass": null,
                    "is_remind_devoff": false,
                    "remind_start_time": null,
                    "remind_stop_time": null
                }
            },
            {
                "id": 14,
                "title": "4K智能管家(POST)",
                "ver": "0.0.1",
                "icon": "",
                "user_id": 9,
                "create_time": "2018-07-18 10:12:37",
                "update_time": "2018-07-18 10:12:37",
                "category": "gw",
                "type_sub": "AA01GW-UG",
                "uuid": "00158d0000d04702",
                "body": "智能网关",
                "perm": null,
                "authorization_id": null,
                "param": {
                    "id": 8,
                    "info_id": 14,
                    "zgb_short": null,
                    "zgb_ieee": "00158d0000d04701",
                    "zgb_ver": "v1.0.0",
                    "zgb_channel": null,
                    "zgb_status": null,
                    "status_id": null,
                    "ip": null,
                    "lng": null,
                    "devinfo": null,
                    "room_id": 6,
                    "floor_id": 5,
                    "unit_id": 4,
                    "env_thsensor_id": null,
                    "env_pmsensor_id": null,
                    "is_local_env": false,
                    "shortcut_dev_id1": null,
                    "shortcut_dev_id2": null,
                    "shortcut_dev_id3": null,
                    "shortcut_dev_id4": null,
                    "ap_ssid": null,
                    "access_ssid": null,
                    "access_pass": null,
                    "is_remind_devoff": false,
                    "remind_start_time": null,
                    "remind_stop_time": null
                }
            }
        ]
    },
    "status": 200016,
    "desc": "请求通用数据列表成功"
    }
    
   *GET  /api/iot/iot_manage_view/id/   get single device info that pk equals id
   
         example: GET /api/iot/iot_manage_view/6/
         
   *DELETE /api/iot/iot_manage_view/id/  delete device info that pk equals id
   
         example: DELETE /api/iot/iot_manage_view/6/
         
   *PUT /api/iot/iot_manage_view/id/   update device info that pk equals id
   
        example:PUT /api/iot/iot_manage_view/3/
        
   Request Params :
   
    {
	"data":
	{
		"title":"4K智能管家(USB)",
		"param":{
			"zgb_short":"FF:FF",
			"ip":"192.168.0.110"
		}
	}
	
    }

   Response
   
    {
    "msg": {
        "data": {
            "id": 13,
            "title": "4K智能管家",
            "ver": "0.0.1",
            "icon": "",
            "user_id": 9,
            "create_time": "2018-06-21 14:02:57",
            "update_time": "2018-06-21 14:02:57",
            "category": "gw",
            "type_sub": "AA01GW-UG",
            "uuid": "00158d0000d04701",
            "body": "4K智能管家",
            "perm": null,
            "authorization_id": null,
            "param": {
                "id": 7,
                "info_id": 13,
                "zgb_short": null,
                "zgb_ieee": "00158d0000d04701",
                "zgb_ver": "v1.0.0",
                "zgb_channel": null,
                "zgb_status": null,
                "status_id": null,
                "ip": null,
                "lng": null,
                "devinfo": null,
                "room_id": 6,
                "floor_id": 5,
                "unit_id": 4,
                "env_thsensor_id": null,
                "env_pmsensor_id": null,
                "is_local_env": false,
                "shortcut_dev_id1": null,
                "shortcut_dev_id2": null,
                "shortcut_dev_id3": null,
                "shortcut_dev_id4": null,
                "ap_ssid": null,
                "access_ssid": null,
                "access_pass": null,
                "is_remind_devoff": false,
                "remind_start_time": null,
                "remind_stop_time": null
            }
        }
    },
    "status": 200015,
    "desc": "更新设备通用数据成功"
    }

   *POST /api/iot/iot_manage_view/   create a device infomation
    Request Params :
    
    {
	"data":	{
		"user_id":	2,
		"category":	"gw",
		"type_sub":	"AA01GW-UG",
		"uuid":	"00158d0000d04701",
		"title":	"4K智能管家(POST)",
		"ver":	"0.0.1",
		"body":	"智能网关",
		"param":	{
			"zgb_ieee":	"00158d0000d04701",
			"zgb_ver":	"v1.0.0"
		}
	  }
    }

   Response 	:
   
    {
    "msg": {
        "data": {
            "id": 13,
            "title": "4K智能管家(POST)",
            "ver": "0.0.1",
            "icon": "",
            "user_id": 9,
            "create_time": "2018-07-18 10:05:14",
            "update_time": "2018-07-18 10:05:14",
            "category": "gw",
            "type_sub": "AA01GW-UG",
            "uuid": "00158d0000d04701",
            "body": "智能网关",
            "perm": null,
            "authorization_id": null,
            "param": {
                "id": 7,
                "info_id": 13,
                "zgb_short": null,
                "zgb_ieee": "00158d0000d04701",
                "zgb_ver": "v1.0.0",
                "zgb_channel": null,
                "zgb_status": null,
                "status_id": null,
                "ip": null,
                "lng": null,
                "devinfo": null,
                "room_id": 6,
                "floor_id": 5,
                "unit_id": 4,
                "env_thsensor_id": null,
                "env_pmsensor_id": null,
                "is_local_env": false,
                "shortcut_dev_id1": null,
                "shortcut_dev_id2": null,
                "shortcut_dev_id3": null,
                "shortcut_dev_id4": null,
                "ap_ssid": null,
                "access_ssid": null,
                "access_pass": null,
                "is_remind_devoff": false,
                "remind_start_time": null,
                "remind_stop_time": null
            }
        }
    },
    "status": 200013,
    "desc": "创建设备通用数据成功"
    }
   
   >status(status code):

    200012:请求设备通用数据成功
    200013: 创建设备通用数据成功
    200014: 删除设备通用数据成功
    200015: 更新设备通用数据成功
    200016:请求通用数据列表成功
    400000: 认证令牌无效。
    400003: 请求参数错误
    400042: 权限不足
    400064:设备已存在
    400065:设备不存在
    400072:创建设备通用信息失败
    400073:创建设备私有信息失败
    400074:空间不存在
    500000: 服务器内部错误
    

####  2.2 Authorization  endpoint for authorize a user to manage a device
   Endpoint 	    : /api/iot/authorization/

   Request Type 	: POST/PUT/DELETE/GET

   Header          : Authorization = Token <token string>

   *GET  /api/iot/authorization/  Get all the authorization related with this user

   *POST /api/iot/authorization/  create a new authorization record that assotiate the user with the device

   Request param:

    {
	"data":
	{
        "info_id":4,            //通用信息ID
        "authorized_id":2,      //被授权者，需要明确指定
        "perm":7                //权限
	}
    }


   Response Param:

    {
    "msg": {
        "data": {
            "id": 26,
            "info_id": 4,
            "authorizer_id": 7,
            "authorized_id": 2,
            "remarks": "",
            "perm": "7"
        }
    },
    "status": 200018,
    "desc": "创建授权数据成功"
    }

   *GET /api/iot/authorization/id/ get signle authorization that pk equals id

   *DELETE /api/iot/authorization/id/ delete authorization record that pk equals id

   *PUT /api/iot/authorization/id/  update authorization that pk equals id

   Request param:
   
    {
	"data":
	{
    "perm":6
	}
    }
    
   Response Param:

    {
    "msg": {
        "data": {
            "id": 16,
            "info_id": 6,
            "authorizer_id": 7,
            "authorized_id": 1,
            "remarks": "",
            "perm": "6"
        }
    },
    "status": 200019,
    "desc": "更新授权数据成功"
    }
 
   >status(status code):

    200017:请求授权数据成功
    200018:创建授权数据成功
    200019:更新授权数据成功
    200020:删除授权数据成功
    200021:请求授权数据列表成功
    400000: 认证令牌无效。
    400003: 请求参数错误
    400042: 权限不足
    400065:设备不存在
    400084:授权对象不存在
    400085:创建授权条目失败
    400086:授权不能超过2级
    400087:授权条目不存在
    400088:授权条目已存在
    500000: 服务器内部错误
 
   

#### 2.3 Space endpoint
    Endpoint 	    : /api/iot/space/

    Request Type 	: POST/PUT/DELETE/GET

    Header          : Authorization = Token <token string>

   *GET /api/iot/space/ Get all the space information related with this user
   
   *DELETE /api/iot/space/id/ delete space record that pk equals id
   
   *PUT /api/iot/space/id/ update space record that pk equals id
   
   *POST /api/iot/space/ create a space
   
   example:
           
   request data:
   
          {
	        "data": {
			"type":"unit",
			"superior_id":            //上一级空间ID,如果空间类型为unit时可不提供
			"home_id":2,              //家庭ID,可选，如果未提供，则默认为该用户创建的默认家庭
			"title": "地下室14",
			"is_default":false   //是否为默认空间，可选，如果提供，值为false，   
		     }	
          }
          
          
   response data:
          
    {
    "msg": {
        "page": {
            "total_page": 1,
            "current_page": 1,
            "page_pieces": 1,
            "total_pieces": 1
        },
        "data": {
            "id": 3,
            "home_id": 2,
            "superior": null,
            "type": "unit",
            "icon": null,
            "title": "地下室14",
            "is_default": false
        }
    },
    "status": 200023,
    "desc": "创建空间数据成功"
    }
    
   >status(status code):

    200022:请求空间数据成功
    200023:创建空间数据成功
    200024:更新空间数据成功
    200025:删除空间数据成功
    200026:请求空间数据列表成功:
    400000: 认证令牌无效。
    400003: 请求参数错误
    400042: 权限不足
    400074:空间不存在
    400079:家庭不存在
    400080:空间已存在
    400081:创建空间失败
    400082:不能创建默认空间
    400083:默认空间不能删除  
    500000: 服务器内部错误

#### 2.4 gateway registration
    Endpoint 	    : /api/accounts/register/gw

    Request Type 	: POST

    Request Param:

    {
       'data':
       {
          'username':'abcdefghigk',
          'password':'xyzsfsfdsf',
       }
    }

    Response Param:
    {
    "msg": {
        "page": {
            "total_page": 1,
            "current_page": 1,
            "page_pieces": 10,
            "total_pieces": 1
        },
        "data":
            {
                "id": 2,
                "token":"sfdsfsfsfd",

            } ,
         }
    "status": "200012",
    "desc": "请求通用类型数据成功"
   }

###2.5 patch interface
   interface:/api/iot/patch/

   method POST

   header:Authorization = Token <token string>

   param request:
   
        {
    "data": [{
		"body": {
			"is_default": false,
			"title": "房间7",
			"type": "unit"
		},
		"method": "POST",
		"seq": "1",
		"url": "http://127.0.0.1:8000/api/iot/space/"
	}, {
		"body": {
			"gw_id": 1,
			"is_default": false,
			"superior": 4,
			"title": "杂物间3",
			"type": "room"
		},
		"method": "POST",
		"seq": "2",
		"url": "http://127.0.0.1:8000/api/iot/space/"
	}]
    }

   :Response:

    {
    "msg": [
        {
            "seq": "1",
            "status_sub": 200023,
            "desc_sub": "创建空间数据成功",
            "data": {
                "id": 32,
                "home_id": 2,
                "superior_id": null,
                "type": "unit",
                "icon": null,
                "title": "房间7",
                "is_default": false
            }
        },
        {
            "seq": "2",
            "status_sub": 400003,
            "desc_sub": "请求参数错误",
            "data": null,
            "err": "if space type is room,param 'superior_id' is needed"
        }
    ],
    "status": 200201,
    "desc": "批量请求部分成功"
    }
   
   >status(status code):
   
    200200:批量请求成功
	200201:批量请求部分成功
	400400:批量请求失败
	400089:请求方法不支持
    400090:协议不支持
    400091:请求url非法

###2.6 sms alarm
    interface:/api/iot/sms/alarm/

    :method POST

    :header:Authorization = Token <token string>
    
    :param request
    {
    "data":
    {
	"msg_type":"illegalunlock",
	"device":"sftryertutyu0wess114",
	"name":"向先生",
	"receiver":"13825182430"
      }
    }
    :return:

    {
    "msg": {
        "page": {
            "total_page": 1,
            "current_page": 1,
            "page_pieces": 1,
            "total_pieces": 1
        },
        "data": "1116ca32-b569-4922-8c22-4e18da795e22" #短信的序列
    },
    "status": "200012",
    "desc": "请求通用类型数据成功"
    }


   msg_type:
   "illegalunlock":撬锁报警
   "hijack": 劫持报警
   "temperary_authrization":


###2.7 HomeMember Management
   Endpoint 	    : /api/iot/members/

   Request Type 	: POST/PUT/DELETE/GET

   Header          : Authorization = Token <token string>

   *GET /api/iot/members/id GET single member
   
   *DELETE /api/iot/members/id/ delete members record that pk equals id
   
   *PUT /api/iot/members/id/ update members record that pk equals id
   
        request:
        {
            "data":
            {
	            "user_id":3, 
            }
        }
        response:
        {
    "msg": {
        "page": {
            "total_page": 1,
            "current_page": 1,
            "page_pieces": 1,
            "total_pieces": 1
        },
        "data": {
            "id": 2,
            "home_id": 3,
            "title": "小星星",
            "icon": "local:5011",
            "username": "18825196895",
            "is_remind": false,
            "remind_time_start": null,
            "remind_time_end": null,
            "is_remind_week0": false,
            "is_remind_week1": false,
            "is_remind_week2": false,
            "is_remind_week3": false,
            "is_remind_week4": false,
            "is_remind_week5": false,
            "is_remind_week6": false,
            "keys": []
        }
    },
    "status": 200015,
    "desc": "更新通用类型数据成功"
   }
   *POST /api/iot/members/ create a space
        example:/api/iot/members/
        request param:
        
        {
            "data":
            {
	            "home_id":3,
	            "title":"小猴子",
	            "icon":"local:5011"
            }
        }
        
   response:
   
    {
    "msg": {
        "page": {
            "total_page": 1,
            "current_page": 1,
            "page_pieces": 1,
            "total_pieces": 1
        },
        "data": {
            "id": 3,
            "home_id": 2,
            "title": "小猴子",
            "icon": "local:5011",
            "username": null,
            "is_remind": false,
            "remind_time_start": null,
            "remind_time_end": null,
            "is_remind_week0": false,
            "is_remind_week1": false,
            "is_remind_week2": false,
            "is_remind_week3": false,
            "is_remind_week4": false,
            "is_remind_week5": false,
            "is_remind_week6": false,
            "keys": []
        }
    },
    "status": 200013,
    "desc": "创建通用类型数据成功"
    }
    
   *GET /api/iot/members/  get all the members
   
     {
    "msg": {
        "page": {
            "total_page": 1,
            "current_page": 1,
            "page_pieces": 10,
            "total_pieces": 2
        },
        "data": [
            {
                "id": 1,
                "home_id": 2,
                "title": "18610059767",
                "icon": "5001",
                "username": "18610059767",
                "is_remind": false,
                "remind_time_start": null,
                "remind_time_end": null,
                "is_remind_week0": false,
                "is_remind_week1": false,
                "is_remind_week2": false,
                "is_remind_week3": false,
                "is_remind_week4": false,
                "is_remind_week5": false,
                "is_remind_week6": false,
                "keys": [
                    {
                        "id": 2,
                        "info_id": null,
                        "key_type": 0,
                        "key_name": "test",
                        "key_number": "12345678",
                        "title": "18610059767",
                        "icon": "5001",
                        "is_remind": false,
                        "remind_time_start": null,
                        "remind_time_end": null,
                        "is_remind_week0": false,
                        "is_remind_week1": false,
                        "is_remind_week2": false,
                        "is_remind_week3": false,
                        "is_remind_week4": false,
                        "is_remind_week5": false,
                        "is_remind_week6": false
                    }
                ]
            },
            {
                "id": 3,
                "home_id": 2,
                "title": "小猴子",
                "icon": "local:5011",
                "username": null,
                "is_remind": false,
                "remind_time_start": null,
                "remind_time_end": null,
                "is_remind_week0": false,
                "is_remind_week1": false,
                "is_remind_week2": false,
                "is_remind_week3": false,
                "is_remind_week4": false,
                "is_remind_week5": false,
                "is_remind_week6": false,
                "keys": []
            }
        ]
    },
    "status": 200012,
    "desc": "请求通用类型数据成功"
  }
  
   >status(status code):

    200042:请求家庭成员数据成功
    200043:创建家庭成员数据成功
    200044:更新家庭成员数据成功
    200045:删除家庭成员数据成功
    200046:请求家庭成员数据列表成功
    400000: 认证令牌无效。
    400003: 请求参数错误
    400042: 权限不足
    400093:家庭成员不存在
    400094:家庭成员已存在
    400095:创建家庭成员失败
    400096:更新家庭成员失败
    500000:服务器内部错误
    
        
###2.8 Keys Management
   Endpoint 	    : /api/iot/keys/

   Request Type 	: POST/PUT/DELETE/GET

   Header          : Authorization = Token <token string>
   
   *GET /api/iot/keys/ GET all keys
   
   >过滤条件: info_id、key_type、key_number
   例子：/api/iot/keys/?info_id=6&key_type=1&key_number=12345678
      
   *GET /api/iot/keys/id/ GET single keys
   
   *DELETE /api/iot/keys/id/ delete keys record that pk equals id
   
   *PUT /api/iot/keys/id/   update keys record that pk equals id
    request:
   
    {
    "data":
    {
	"info_id":6,
	"member_id":3,
	"key_type":1,
	"key_name":"36586",
	"key_number":1
    }
    }
 respone:
 
       {
    "msg": {
        "data": {
            "id": 5,
            "info_id": 6,
            "key_type": 1,
            "key_name": "36586",
            "key_number": 1,
            "title": "小猴子",
            "icon": "local:5011",
            "member_id": 3
        }
    },
    "status": 200015,
    "desc": "更新通用类型数据成功"
    }
 
   *POST /api/iot/keys/ create a key
   request:
    
    {
        "data":
        {
	"info_id":6,
	"member_id":3,   可以为空
	"key_type":1,
	"key_name":"little apple",
	"key_number":1
    }
    }
  response:
    
     {
    "msg": {
        "data": {
            "id": 5,
            "info_id": 6,
            "key_type": 1,
            "key_name": "little apple",
            "key_number": 1,
            "title": "小猴子",
            "icon": "local:5011",
            "member_id": 3
        }
    },
    "status": 200013,
    "desc": "创建通用类型数据成功"
    }
    
  >status
  
    200029:请求钥匙数据成功
    200030:创建钥匙数据成功
    200031:更新钥匙数据成功
    200032:删除钥匙数据成功
    200033:请求钥匙数据列表成功
    400003:参数错误
    400042:权限不足
    400065:设备不存在
    400097:创建钥匙数据失败
    400098:钥匙不存在
    400099:钥匙已存在
    400100:更新钥匙数据失败
    500000:服务器内部错误
    

    
  
###2.9 Message Management
   Endpoint 	    : /api/iot/messages/

   Request Type 	: POST/DELETE/GET

   Header          : Authorization = Token <token string>
   
   *GET /api/iot/messages/ get all messages related with this user
   
    filter param:[info_id/category/level/date_lte/date_gte/page/limit/level_lte/level_gte]
    注：lte表示小于等于  gte表示大于等于
    example:/api/iot/messages/?limit=3&page=2&info_id=20&level_gte=1
    
   *GET /api/iot/messages/id GET single message
   
   *DELETE /api/iot/messages/id/ delete message record that pk equals id
   
   *POST /api/iot/messages/ create a message
   request:
   
    {
    "data":
    {
	"info_id":18,    //必填
	"level":2,     //选填  默认为1
	"message_type":"operation_info",//必填
	"flag":"fingerprint_unlock",//必填
	"key_id":1,   //可选，如果为填 则显示为用户名称为您有家人
	"occur_time":"标准时间格式"，
	"receiver":"13825182430"   //可选，根据模板填写
    }
    }
  response:
  
    {
    "msg": {
        "data": {
            "id": 11,
            "user_id": 10,
            "info_id": 18,
            "category": "lock",
            "level": 2,
            "message_type": "operation_info",
            "flag": "fingerprint_unlock",
            "created_time": "2018-07-28 13:47:26",
            "occur_time": "2018-07-28 11:11:11",
            "content": "您有家人使用指纹开锁，已到家。"
        }
    },
    "status": 200039,
    "desc": "创建消息成功"
    }
    
  
    消息的level定义
    1  通知
    2  提醒
    3  告警
  
    消息类型（message_type)与消息指示（flag）见文档《消息推送汇总》
    
   >status
   
    200038:{请求消息成功
    200039:{创建消息成功
    200040:删除消息成功
    200041:请求消息列表成功
    400042:权限不足
    400065:设备不存在
    500000:服务器内部错误
    
 
###2.10temporay password
   Endpoint 	    : /api/iot/temporary_passwords/

   Request Type 	: POST/GET

   Header          : Authorization = Token <token string>
   
   >GET /api/iot/temporary_passwords/  get all the temporary password related with the user
   >POST /api/iot/temporary_passwords/  create a temporary password item
   
    {
        "data":
        {
  	"authorizer_id":9,
	"info_id":6,
	"phone":"16620039353",
	"start_time":"2018-07-06 10:30",
	"duration":60,
	"temporary_password":"234567",
	"end_time":"2018-07-06 11:30"
     }
    }
    
   response:
   
    {
    "msg": {
        "data": {
            "id": 20,
            "phone": "16620039353",
            "title": null,
            "start_time": "2018-07-06 10:30",
            "duration": 60,
            "description": "1.0小时",
            "created_time": "2018-07-09 10:15:06",
            "end_time": "2018-07-06 11:30",
            "authorizer": 9,
            "info_id": 6
        }
    },
    "status": 200013,
    "desc": "创建通用类型数据成功"
   }
  

    HTTP status code: HTTP_200_OK

   >status(status code):
   
    200034:请求临时密码数据成功
    200035:创建临时密码数据成功
    200036:请求临时密码数据列表成功
    400003:参数错误
    400101:授权人不存在
    400042:权限不足
    400065:设备不存在
    500000:服务器内部错误
        
    
    
###2.11 home management
   Endpoint 	    : /api/iot/home/

   Request Type 	: PUT/GET/

   Header          : Authorization = Token <token string>
   
   >status
   
    200024:请求家庭数据成功
    200025:更新家庭数据成功
    400042:权限不足
    400065:设备不存在
    400066:创建临时密码失败
    400092:更新家庭数据失败
    400101:授权人不存在
    500000:服务器内部错误
    
###2.12 version management
   Endpoint 	    : /api/iot/version/

   Request Type 	: GET

   Header          : Authorization = Token <token string>
   
   >获取最新版本：
   request url:/api/iot/versions/latest/?device_type=1
   response:
   
    {
    "msg": {
        "data": {
            "id": 2,
            "device_type": 1,
            "version": "1.0.0",
            "filename": "http://192.168.0.240:8000/media/version/mqttfx-1.7.1-demo1-windows-x64_8RahhtM.exe",
            "create_time": "2018-07-03 14:28:41",
            "description": "test",
            "checksum": "1234567890"
        }
    },
    "status": 200037,
    "desc": "请求最新版本信息成功"
    }
    
   >请求版本列表:
   request url:/api/iot/versions/
   filter param:[device_type','version']
   example:/api/iot/versions/?device_type=1&version=1.0.0
   
   >status
   
    200037:请求最新版本信息成功
    200047:请求版本信息列表成功
    500000:服务器内部错误
    
   >device_type 
   
    1,'智能网关'
    2,'智能网关(USB)
    3,'Zigbee'
    4,'Zigbee协调器'
    5,'Android'
    6,'IOS'
  
###2.13 get_timestamp

   Endpoint 	    : /api/iot/get_timestamp/

   Request Type 	: GET

   Header          : Authorization = Token <token string>
   
   Response
   
    {
    "msg": {
        "data": {
            "timestamp": 1532679058
        }
    },
    "status": 200049,
    "desc": "获取时间戳成功"
    }
    
##2.13 feedback

   Endpoint 	    : /api/iot/feedback/

   Request Type 	: POST

   Header          : Authorization = Token <token string>
   
   create a feedback
   
   request param:
   
    {
        "data":{
        "category":1,    //设备类型，必填
        "contact":13825132345,   //联系方式，选填
        "content":"开锁有问题",  //反馈内容，必填
        "images":[                             //图片，选填,base64格式,code为base64编码后的内容
            {"code":"werwtwteyeyety","image_type":"jpg"},
            {"code":"tetetetyetyeyey","image_type":"jpg"}
            ]
       }
    }
    
   response
   
    {
    "msg": {
        "data": {
            "category":1,    //设备类型
            "contact":13825132345,   
            "content":"开锁有问题",  
            "images":["media/feedback/pic1932434345.jpg","media/feedback/pic1932434346.jpg"], 
            "created_time":"2018-07-30"
        }
    },
    "status": 200048,
    "desc": "创建意见反馈信息成功"
    }
    
   设备类型定义：
   1,智能网关
   2,智能门锁
   3,摄像头
   4,开关
   5，插座
   6，窗帘电机
   7，红外转发器
   8，情景面板
   9，传感器
   10,app
   11,其它
 
##2.15 share
     
   Endpoint 	    : /api/iot/share/

   Request Type 	: POST

   Header          : Authorization = Token <token string>
   
   request
   
    
    {
        "data":
            {
	            "receiver":"13825182430",
	            "platform":"ios"       //平台  值ios/android
            }
        }
    
   response:
   
    {
    "msg": {
        "data": "send success"
    },
    "status": 200050,
    "desc": "分享成功"
    }
    
### 3. APP management

#### 3.1 QR Code data format

    info: base url/api/app/type/uuid

    app:  django 'app' 应用
    type: 产品和信息型号
    uuid: 产品和信息uuid

#### 3.2 APP and firmware release manage

    Endpoint 	    : /api/app/release_view/

    Request Type 	: POST/PUT/DELETE

    Header          : Authorization = Token <token string> (user:admin)

    Request Params  :
    {
        "type": TYPE ID,
        "name": APP NAME,
        "platform": platform type,
        "package_name": package name,
        "version": version,
        "brief": brief,
        "icon_url": icon_url,
        "pm": PM,
        "qrcode": QR CODE INFO URL,
        "app_version":[
            {
                info_id(integer)：APP版权信息id
                type(varchar256):应用类型
                name(varchar256):应用名称
                appid(varchar256):应用唯一标识
                platform(varchar256):应用平台类型
                package_name(varchar256):应用包名
                version(varchar256):当前版本号
                size(integer)：文件大小
                update_brief(varchar512):版本更新说明
                icon_url(varchar256):应用ICON URL
                down_url(varchar256):应用链接 URL
                qrcode(varchar4096):二维码信息
                ip(integer): 应用版权信息ID
            }

        ]
    }

    Response 	:
    {
        "msg": {
            id(integer)：主键，版权信息id
            type_id(varchar256):应用类型id
            name(varchar256):应用名称
            platform(varchar256):应用平台类型
            package_name(varchar256):应用包名
            version(varchar256):应用版本号
            brief(varchar4096):应用简介
            icon_url(varchar256):应用ICON URL
            pm(varchar256):应用产品经理
            qrcode(varchar4096):二维码信息
            down_count(integer):下载次数
            create_time(datetime)：创建时间
            app_version:[
                {
                    info_id(integer)：APP版权信息id
                    type(varchar256):应用类型
                    name(varchar256):应用名称
                    appid(varchar256):应用唯一标识
                    platform(varchar256):应用平台类型
                    package_name(varchar256):应用包名
                    version(varchar256):当前版本号
                    size(integer)：文件大小
                    update_brief(varchar512):版本更新说明
                    icon_url(varchar256):应用ICON URL
                    down_url(varchar256):应用链接 URL
                    qrcode(varchar4096):二维码信息
                    ip(integer): 应用版权信息ID
                }

            ]
        },
        "status": 200301,
        "desc": base_utils.get_status_desc(200013, 'chs')
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200301: create general data success.
    200302: delete general data success.
    200303: update general data success.
    400301: Token is not valid/HTTP_401_UNAUTHORIZED.
    400302: Permission denied.
    400303: Unmatched data.
    400304: Unmatched data.
    400003: Request Params error


### 4. MQTT management

#### 4.1 MQTT INFO
    HOST: aa.zjchilink.com
    PORT:9880
    Authentication: https user
    Connection parameters: username,password,clientid(device uuid)
    Qos:  根据不同消息类型，默认：0
    Retain: 根据不同消息类型，默认：True
    Payload Type: String/JSON

#### 4.2 MQTT Subscribe
    -----------------------------------------------
    Topic Consists: username/category/uuid/exectype
    -----------------------------------------------
        category: device category
        uuid: device uuid (32 byte)
        exectype: create/update/delete/query/control/set
        e.g: 188000000000/switch/ABC123/create (sub user 188000000000, device ABC123 create info)
    -----------------------------------------------

#### 4.2 MQTT Publish
    -----------------------------------------------
    Topic Consists: username/category/uuid/exectype
    -----------------------------------------------
    Content:
    {
        "msg": {
            "sn": serial number,
            "id": 2,
            "user_id": 2,
            "create_time": "2018-04-12 12:01:02",
            "update_time": "2018-04-12 12:01:02",
            "category": "gw",
            "type": "AA01GW-UG",
            "cluster": "1001",
            "uuid": "QWERTYUIOP0987654321ZXCVBNM",
            "title": "4k IA智能机顶盒",
            "ver": "0.0.1",
            "icon": "1001",
            "body": "智能网关",
            "perm": 7,
            "param": {
                ...
            }
        },
        "status": 200401,
        "desc": base_utils.get_status_desc(200013, 'chs')
    }

    status(status code):
    200401: mqtt publish success.
    200402: mqtt subscribe success.
    400401: Token is not valid/HTTP_401_UNAUTHORIZED.
    400402: Permission denied.
    400403: mqtt publish error.
    400404: mqtt subscribe error.

    -----------------------------------------------


### 5. Category/Type Definition
    见《产品名称类别型号对照表》

### 6. ICON Definition
    见《智能家居系统图标和编码》

### 7. Permission Definition

    编号     标识        说明
     7	   qcusad       浏览 + 控制 + 更新 + 授权 + 创建 + 删除
     6	   qcusa        浏览 + 控制 + 更新 + 授权 + 创建
     5	   qcus         浏览 + 控制 + 更新 + 授权
     4	   qcu          浏览 + 控制 + 更新
     3	   qc           浏览 + 控制
     2	   q            浏览
     1	   n            无权限

### 8. City List Definition



### 9. Operation Status Definition

    200501: 关闭
    200502: 常开
    200503: 开启
    200503: 暂停
    200503: 停止
    200503: 正常状态
    200503: 设备处于添加状态
    200503: 请求添加信息
    200503: 请求更新信息
    200503: 请求控制设备
    200503: 请求删除信息
    200503: 正在添加信息
    200503: 正在更新信息
    200503: 正在控制设备
    200503: 正在删除设备
    200503: 添加信息成功
    200503: 更新信息成功
    200503: 控制设备成功
    200503: 删除信息成功
    200503: 请求网关进入允许加入状态
    200503: 设备状态正常
    200503: 请求设置信息
    200503: 正在设置信息
    200503: 设置信息成功
    400501: 密码错误
    400502: 权限不足
    400503: 密钥错误
    400504: 非法用户
    400505: 授权失效
    400505: 操作失败
    400505: 反锁
    400505: 系统锁定
    400505: 撬锁报警
    400505: 次数超限报警
    400505: 低电量报警
    400505: 开锁事件
    400505: 胁迫报警
    400505: 添加用户
    400505: 删除用户
    400505: 撬锁芯报警
    400505: 假锁报警
    400505: 故障报警
    400505: 锁定状态解除
    400505: 门锁已恢复出厂设置
    400505: 本地修改用户密码
    400505: 未拔钥匙
    400505: 长时间未开锁报警
    400505: 按键短路
    400505: 存储器异常
    400505: 触摸芯片异常
    400505: 低压检测电路异常
    400505: 读卡电路异常
    400505: 检卡电路异常
    400505: 指纹通讯异常
    400505: RTC晶振电路异常
    400505: 存在相同名称信息
    400505: 网关无法访问互联网
    400505: 网关zigbee网络错误
    400505: 未知错误，请联系客服
    400505: 设备不在线
    400505: 请求设备状态
    400505: 设备信号弱
    400505: 设备电量不足
    400505: 节点设备无应答
    400505: 设备本地存储错误
    400505: 请求设备参数错误
    400505: 添加到云服务器失败
    400505: 时间格式错误
    400505: 管理员密码错误
    400505: 密码格式错误
    400505: 数量超过最大限制
    400505: 更新信息到云服务器失败
    400505: 删除信息从云服务器失败
    400505: 该信息不存在


### 10. UDP Broadcast

    Protocol: UDP Broadcast
    Port    : 9820
    Content :

    {
        "msg": {
            "sn": serial number,
            "id": 2,
            "user_id": 2,
            "create_time": "2018-04-12 12:01:02",
            "update_time": "2018-04-12 12:01:02",
            "category": "gw",
            "type": "AA01GW-UG",
            "cluster": "1001",
            "uuid": "QWERTYUIOP0987654321ZXCVBNM",
            "title": "4k IA智能机顶盒",
            "ver": "0.0.1",
            "icon": "1001",
            "body": "智能网关",
            "perm": 7,
            "param": {
                "zgb_short": "FF:FF",
                "zgb_ieee": "FF:FF:FF:FF:FF:FF:FF:FF",
                "zgb_ver": "01",
                "zgb_channel": "12",
                "zgb_status": "1",
                "status": 1,
                "ip": "192.168.1.100",
                "lng": "7654.56|456.5",
                "devinfo": "Iphone 8",
                "env_thsensor_id": null,
                "env_pmsensor_id": null,
                "is_local_env": false,
                "shortcut_dev_id1": null,
                "shortcut_dev_id2": null,
                "shortcut_dev_id3": null,
                "shortcut_dev_id4": null,
                "ap_ssid": null,
                "access_ssid": null,
                "access_pass": null,
                "is_remind_devoff": true,
                "remind_start_time": "08:30",
                "remind_stop_time": "18:30",
                "space": [

                ]
            }
        },
        "status": 200501,
        "desc": base_utils.get_status_desc(200013, 'chs')
    }

    status(status code):

    200601: Available device.
    200602: Unmatched data.
    200603: Unmatched data.
    400601: Unmatched data.
    400602: Unmatched data.
    400603: Unmatched data.


### 11. SMS +++++++++++++++++++++

#### 11.1 SMS Sending interface

    Endpoint 	    : /api/sms/sms_manage_view/

    Request Type 	: POST

    Header          : Authorization = Token <token string>

    Request Params  :
    {
        "id": 2,
        "user_id": 2,
        "create_time": "2018-04-12 12:01:02",
        "update_time": "2018-04-12 12:01:02",
        "category": "gw",
        "type": "AA01GW-UG",
        "cluster": "1001",
        "uuid": "QWERTYUIOP0987654321ZXCVBNM",
        "title": "4k IA智能机顶盒",
        "ver": "0.0.1",
        "icon": "1001",
        "body": "智能网关",
        "perm": 7,
        "param": {
            ...
        }
    }


    Response 	:
    {
        "msg": {

            "id": 2,
            "user_id": 2,
            "create_time": "2018-04-12 12:01:02",
            "update_time": "2018-04-12 12:01:02",
            "category": "gw",
            "type": "AA01GW-UG",
            "cluster": "1001",
            "uuid": "QWERTYUIOP0987654321ZXCVBNM",
            "title": "4k IA智能机顶盒",
            "ver": "0.0.1",
            "icon": "1001",
            "body": "智能网关",
            "perm": 7,
            "param": {
                ...
            }
        },
        "status": 200013,
        "desc": base_utils.get_status_desc(200013, 'chs')
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200013: create general data success.
    200014: delete general data success.
    200015: update general data success.
    400047: Token is not valid/HTTP_401_UNAUTHORIZED.
    400048: Permission denied.
    400049: Unmatched data.
    400050: Unmatched data.
    400051: Unmatched data.
    400052: Unmatched data.
    400003: Request Params error



### 11. PUSH +++++++++++++++++++++

#### 11.1 PUSH Sending interface

    Endpoint 	    : /api/push/push_manage_view/

    Request Type 	: POST

    Header          : Authorization = Token <token string>

    Request Params  :
    {
        "id": 2,
        "user_id": 2,
        "create_time": "2018-04-12 12:01:02",
        "update_time": "2018-04-12 12:01:02",
        "category": "gw",
        "type": "AA01GW-UG",
        "cluster": "1001",
        "uuid": "QWERTYUIOP0987654321ZXCVBNM",
        "title": "4k IA智能机顶盒",
        "ver": "0.0.1",
        "icon": "1001",
        "body": "智能网关",
        "perm": 7,
        "param": {
            ...
        }
    }


    Response 	:
    {
        "msg": {

            "id": 2,
            "user_id": 2,
            "create_time": "2018-04-12 12:01:02",
            "update_time": "2018-04-12 12:01:02",
            "category": "gw",
            "type": "AA01GW-UG",
            "cluster": "1001",
            "uuid": "QWERTYUIOP0987654321ZXCVBNM",
            "title": "4k IA智能机顶盒",
            "ver": "0.0.1",
            "icon": "1001",
            "body": "智能网关",
            "perm": 7,
            "param": {
                ...
            }
        },
        "status": 200013,
        "desc": base_utils.get_status_desc(200013, 'chs')
    }

    HTTP status code: HTTP_200_OK

    status(status code):

    200013: create general data success.
    200014: delete general data success.
    200015: update general data success.
    400047: Token is not valid/HTTP_401_UNAUTHORIZED.
    400048: Permission denied.
    400049: Unmatched data.
    400050: Unmatched data.
    400051: Unmatched data.
    400052: Unmatched data.
    400003: Request Params error


### 12. Device Data format:

    #### 12.1 gateway:
        {
            "id": 1,
            "title": "4K智能管家(POST)",
            "ver": "0.0.1",
            "icon": "",
            "user_id": 2,
            "create_time": "2018-06-15 02:40:25",
            "update_time": "2018-06-15 02:40:25",
            "category": "gw",
            "type_sub": "AA01GW-UG",
            "uuid": "00158d0000d04700",
            "body": "智能网关",
            "perm": null,
            "param": {
                "id": 1,
                "info_id": 1,
                "zgb_short": null,
                "zgb_ieee": "00158d0000d04700",
                "zgb_ver": "v1.0.0",
                "zgb_channel": null,
                "zgb_status": null,
                "status_id": null,
                "ip": null,
                "lng": null,
                "devinfo": null,
                "room_id": null,
                "floor_id": null,
                "unit_id": null,
                "env_thsensor_id": null,
                "env_pmsensor_id": null,
                "is_local_env": false,
                "shortcut_dev_id1": null,
                "shortcut_dev_id2": null,
                "shortcut_dev_id3": null,
                "shortcut_dev_id4": null,
                "ap_ssid": null,
                "access_ssid": null,
                "access_pass": null,
                "is_remind_devoff": false,
                "remind_start_time": null,
                "remind_stop_time": null
            }
        }
        
        
        

    #### 12.2 lock:
        {
            "id": 3,
            "user_id": 2,
            "create_time": "2018-04-12 12:01:02",
            "update_time": "2018-04-12 12:01:02",
            "category": "lock",
            "type": "AA02SL-HE",
            "cluster": "1001",
            "uuid": "QWERTYUIOP0987654321ZXCVBSL",
            "title": "智能门锁",
            "ver": "0.0.1",
            "icon": "1001",
            "body": "智能门锁",
            "perm": 7,
            "param": {
                "zgb_short": "FF:FF",
                "zgb_ieee": "FF:FF:FF:FF:FF:FF:FF:FF",
                "zgb_ver": "01",
                "zgb_channel": "12",
                "zgb_status": "1",
                "status": 1,
                "ip": "192.168.1.100",
                "lng": "7654.56|456.5",
                "devinfo": "Iphone 8",
                "battery": 99,
                "unit_id": 1,
                "floor_id": 2,
                "room_id": 3,
                "operate": 0,
                "user": null,
                "pass": null,
                "appid": 1,
                "keyid": 1,
                "keytype": 1,
                "usertype": 1,
                "no_open_count": 0,
                "no_close_count": 0,
                "temp_pass": null,
                "temp_duration": 0,
                "temp_phone": null,
                "temp_brief": null,
                "temp_time": null,
                "door_contact_id": null,
                "is_remind_status": 0,
                "no_open_remtime": null,
                "no_close_remtime": null,
                "lowpower_limit": 20,
                "pass_error_limit": 5,
                "is_push_operate": true,
                "is_push_lowpower": true,
                "is_push_noopen": true,
                "is_push_passerr": true,
                "is_push_hijack": true,
                "is_push_illegalunlcok": true,
                "hijack_name": null,
                "hijack_contact": null,
                "hijack_contact_phone": null,
                "hijack_contact_addr": null,
                "illegalunlcok_alarm_phone1": null,
                "illegalunlcok_alarm_contact1": null,
                "illegalunlcok_alarm_phone2": null,
                "illegalunlcok_alarm_contact2": null
            }
        }
    #### 12.3 camera:
        {
            "id": 3,
            "user_id": 2,
            "create_time": "2018-04-12 12:01:02",
            "update_time": "2018-04-12 12:01:02",
            "category": "camera",
            "type": "AA02NC1Y-XM",
            "cluster": "1001",
            "uuid": "QWERTYUIOP0987654321ZXCVBCM",
            "title": "网络摄像头",
            "ver": "0.0.1",
            "icon": "1001",
            "body": "网络摄像头",
            "perm": 7,
            "param": {
                "status": 1,
                "ip": "192.168.1.100",
                "lng": "7654.56|456.5",
                "devinfo": "Iphone 8",
                "battery": 99,
                "unit_id": 1,
                "floor_id": 2,
                "room_id": 3,
                "operate": 0,
                "user": null,
                "pass": null,
                "admin_user": null,
                "admin_pass": null,
                "p2pid": null,
                "wifi_ssid": null,
                "wifi_pass": null,
                "wifi_channel": null,
                "wifi_status": null,
                "wifi_safety": null,
                "is_mirror": false,
                "volume": 80,
                "is_full_screen": false,
                "dev_time": "0000-00-00 00:00:00",
                "time_zone": null,
                "is_auto_time": true,
                "ntp_server": null,
                "sd_capacity": null,
                "sd_status": null,
                "record_cover": false,
                "record_sound": true,
                "record_timer": true
            }
        }
    #### 12.4 switch:
        {
            "id": 4,
            "user_id": 2,
            "create_time": "2018-04-12 12:01:02",
            "update_time": "2018-04-12 12:01:02",
            "category": "switch",
            "type": "AA03SW3K-HN-15A",
            "cluster": "1001",
            "uuid": "QWERTYUIOP0987654321ZXCVBCM",
            "title": "智能开关",
            "ver": "0.0.1",
            "icon": "1001",
            "body": "智能开关",
            "perm": 7,
            "param": {
                "zgb_short": "FF:FF",
                "zgb_ieee": "FF:FF:FF:FF:FF:FF:FF:FF",
                "zgb_ver": "01",
                "zgb_channel": "12",
                "zgb_status": "1",
                "status": 1,
                "ip": "192.168.1.100",
                "lng": "7654.56|456.5",
                "devinfo": "Iphone 8",
                "battery": 99,
                "unit_id": 1,
                "floor_id": 2,
                "room_id": 3,
                "operate": 0,
                "operate_channel_id": 0,
                "channel": [{
                        "id": 1,
                        "swtich_id": 4,
                        "icon": "1001",
                        "title": "客厅灯",
                        "unit_id": 1,
                        "floor_id": 2,
                        "room_id": 3,
                        "status": 1,
                        "value": 0,
                        "onclick_bind_id": null,
                        "onclick_bind_value": null,
                        "doubleclick_bind_id": null,
                        "doubleclick_bind_value": null,
                        "current_power": null,
                        "rated_power": null,
                        "no_open_count": 0,
                        "no_close_count": 0,
                        "countdown_state": 0,
                        "countdown": 0,
                        "countdown_value": 0
                    },

                    {
                        "id": 2,
                        "swtich_id": 4,
                        "icon": "1001",
                        "title": "厨房灯",
                        "unit_id": 1,
                        "floor_id": 2,
                        "room_id": 3,
                        "status": 1,
                        "value": 100,
                        "onclick_bind_id": null,
                        "onclick_bind_value": null,
                        "doubleclick_bind_id": null,
                        "doubleclick_bind_value": null,
                        "current_power": null,
                        "rated_power": null,
                        "no_open_count": 0,
                        "no_close_count": 0,
                        "countdown_state": 0,
                        "countdown": 0,
                        "countdown_value": 0
                    },

                    {
                        "id": 3,
                        "swtich_id": 4,
                        "icon": "1001",
                        "title": "卧室灯",
                        "unit_id": 1,
                        "floor_id": 2,
                        "room_id": 3,
                        "status": 1,
                        "value": 100,
                        "onclick_bind_id": null,
                        "onclick_bind_value": null,
                        "doubleclick_bind_id": null,
                        "doubleclick_bind_value": null,
                        "current_power": null,
                        "rated_power": null,
                        "no_open_count": 0,
                        "no_close_count": 0,
                        "countdown_state": 0,
                        "countdown": 0,
                        "countdown_value": 0
                    }
                ]
            }
        }

### 13 USB网关配网流程

    Protocol: UDP Broadcast
    Port    : 9820

    ###13.1 请求wifi列表
     {
        "status":200552
     }
    
    ###13.2 请求wifi成功
    {
        "status":200553,
        "data":[
                {
                "auth":3,
                "encry":3,
                "ssid":"不要上我"
                },
                ...
             ]
        }
        
    ###13.3请求wifi失败
     {
        "status":400514
     }
     
    ###13.4请求连接wifi
    {
        "status":200554，
        "data":{
            "auth":3,
            "encry":3,
            "ssid":"不要上我",
            "pwd":"nopass"
     }
     
    ###13.5连接wifi失败
    {
        "status":400515
     }
     
    
    auth认证方式定义
        OPEN 			0
        SHARED 			1
        WPAPSK 			2
        WPA2PSK 		3
        WPAPSKWPA2PSK 	4

    Encry 加密方式定义
        NONE 		0
        WEP 		1
        TKIP		2
        AES			3
        TKIPAES 	4	
  
###版本升级流程
    Protocol: UDP Broadcast
    Port    : 9820
    200552	请求获取wifi列表（USB网关）
    200553	获取wifi列表成功（USB网关）
    200554	请求连接wifi（USB网关）
    200555	固件已是最新
               