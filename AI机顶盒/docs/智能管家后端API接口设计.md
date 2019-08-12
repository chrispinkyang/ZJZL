INTERFACE: /api/brain/

METHOD: POST

content-type: json

##Request:

	{
	uuid:'265e668262'
	ongoing_service: 'Music'#未完成的服务
	texts:'sentence',
	language: 'Mandarin'/'Cantonese'
	}

Tips:数组形式传递文本,一个指令为一个元素,先测试单个指令.

##Response:

基本格式:

	{
	status: <int> #成功为0,失败为1
	msg: <string> #成功为'success', 失败为<错误信息>
	result: <Object> # 因服务类型而不同
		{
		speechtext:'' #智能管家响应语音文本
		language:''
		service:'' #服务类型:电视,智能家居,音乐和天气等.
		intent:<string> #用户意图
		data:# 操作数据
			{
			}
		
		}
	}

###电视控制

1.电源打开/关闭

	{
	status: <int> #成功为0,失败为1
	msg: <string> #成功为'success', 失败为<错误信息>
	result: 
		{
		SpeechTexts:'' #智能管家响应语音文本
		service:'Televison'
		intent:<string> #用户意图
		data:
			{
			op_type:'power',
			op_value:<int> # 打开为1,关闭为0
			}
		}
	}


2.音量调节/静音

	{
	status: <int> #成功为0,失败为1
	msg: <string> #成功为'success', 失败为<错误信息>
	result: 
		{
		speechtexts:'' #智能管家响应语音文本
		service:'Televison'
		intent:<string> #用户意图
		data:
			{
			op_type:'volume',
			op_value:<String> # 调高:'+',调低:'-',静音:'off'
			}
		}
	}


3.菜单切换
	
	{
	status: <int> #成功为0,失败为1
	msg: <string> #成功为'success', 失败为<错误信息>
	result: 
		{
		speechtexts:'' #智能管家响应语音文本
		service:'Televison'
		intent:<string> #用户意图
		data:
			{
			op_type:'menu',
			op_value:<int> # 进入:1,退出:0
			}
		}
	}

4.影视内容控制:
	
	{
	status: <int> #成功为0,失败为1
	msg: <string> #成功为'success', 失败为<错误信息>
	result: 
		{
		speechtexts:'' #智能管家响应语音文本
		service:'Televison'
		intent:<string> #用户意图
		data:
			{
			op_type:'control',
			op_value:<String> 
			# 播放/暂停 play/stop
			# 上集/下集 last/next
			# 快进/快退 fast/slow
			}
		}
	}

5.影视内容指定

	{
	status: <int> #成功为0,失败为1
	msg: <string> #成功为'success', 失败为<错误信息>
	result: 
		{
		speechtexts:'' #智能管家响应语音文本
		service:'Televison'
		intent:<string> #用户意图
		data:
			{
			op_type:'channel'/'program'
			op_value:<String>
			# 切换频道即为<频道名称/编号>
			# 播放节目即为<节目名称/编号>
			}
		}
	}


###智能家居

####基本类型:

	{
	status: <int> #成功为0,失败为1
	msg: <string> #成功为'success', 失败为<错误信息>
	result: 
		{
		SpeechTexts:'' #智能管家响应语音文本
		service:''# 定义操作对象
		intent:<string> #用户意图
		data:
			{
			op_type:'',
			op_value:<int> # 打开为1,关闭为0
			}
		}
	}

Tips:可操作的智能家居所有类型待归纳

**例子:空调**

	{
	status: <int> #成功为0,失败为1
	msg: <string> #成功为'success', 失败为<错误信息>
	result: 
		{
		SpeechTexts:'' #智能管家响应语音文本
		service:'airconditioner'
		intent:<string> #用户意图
		data:
			{
			op_type:'', #电源:power,温度:temp
			op_value:
			# 打开为1,关闭为0.<int>
			# 调节温度为 '+','-'<String> 或 具体数值 <int> 
			}
		}
	}

###音乐

1.网络搜索音乐

	{
	status: <int> #成功为0,失败为1
	msg: <string> #成功为'success', 失败为<错误信息>
	result: 
		{
		SpeechTexts:'' #智能管家响应语音文本
		service:'Music'# 定义操作对象
		intent:<string> #用户意图:歌手/歌曲名
		data:
			{
			op_type:'search',
			op_value:<String> # 返回音乐资源下载地址Url
			}
		}
	}

###天气

	{
	status: <int> #成功为0,失败为1
	msg: <string> #成功为'success', 失败为<错误信息>
	result: 
		{
		SpeechTexts:'' #智能管家响应语音文本
		service:'Weather'# 定义操作对象
		intent:<string> #用户意图:地区+日期
		data:#数组,以天为单位,返回一周内天气
			[
			{
			"city": "北京",
			"date": "2018-09-16",
			"date_for_voice": "17号",#"今天"/"明天"/"后天"/x号
			"img": ,#气象图url
			"lastUpdateTime": "2018-09-12 11:00",
			"tempHigh": "26℃",
			"tempLow": "15℃",
			"tempRange": "15℃ ~ 26℃",
			"weather": "多云",
			"weatherDescription": "温度适宜。",
			"weatherType": 1,
			"week": "周日",
			"wind": "北风微风",
			"windLevel": 0
			}
			]
		}
	}

Tips: data待定,待确定第三方天气接口的数据详细信息