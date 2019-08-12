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

