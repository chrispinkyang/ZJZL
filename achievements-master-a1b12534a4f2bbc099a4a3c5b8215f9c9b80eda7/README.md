###1.1 clock interface
    Endpoint:/api/clocks/
    Method:POST/GET
    Header:Authorization: Token <string>

    POST:
         :body:
        {
	          "content": "test for clock",
              "goal_id": 11,
              "img":"sdsdsd"
        }
        :remarks:img fields is a choicable field
        :return:

        {
            "msg": "succeed",
            "status": 0,
            "result": {
                 "id": 1,
                 "clockTime": "2018-05-22 03:40:13",
                 "content": "test for clock",
                 "img": null,
                "isConfirm": false,
                "goal": 11,
                "user": 3
                }
        }

###refund interface
    Endpoint:/api/refund/
    Method:POST
    Header:Authorization: Token <string>
    request param:
        {
	          "transactin_id":transaction_id,
        }
        
        or
        
        {
        "out_trade_no":out_trade_no,
        "total_fee":toal_fee,
        "refund_fee":refund_fee
        }

###unifiedorder interface
    Endpoint:/api/unifiedorder/
    Method:POST
    Header:Authorization: Token <string>
    request param:
    {
        "body":订单描述,
        "total_fee":订单金额,
        "goal_id":goal_id  如果是目标创建者，则可不传，如果是监督者，那么必须传。
    }
    response:
    {
    "appId":appid,
    "timeStamp":timestamp,
    "nonceStr":nonce_str,
    "package":package,
    "signType":sign_type
    "trade_no":trade_no
    }
    
###refund interface
    Endpoint:/api/refund/
    Method:POST
    Header:Authorization: Token <string>
    request param:
    {
    "trade_no":trade_no
    }
    
###withdrawCash interface
    Endpoint:/api/refund/
    Method:POST
    Header:Authorization: Token <string>
    request param:
   {
    "desc":desc,
    "amount":amount
    }
    
    
###poster download
    Endpoint:/api/goals/{id}/generate_poster/
    Method:POST
    Header:Authorization: Token <string>
    request param:
    {
	"type":"result"     #type的值 ：result为挑战成功或者失败时的海报，create为创建目标时
    }
    
###捡道 