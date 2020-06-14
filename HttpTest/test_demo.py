import requests

#通讯录管理
class TestDemo():
    def setup(self):        #定义setup方法，以便执行用例时可以获取token值
        corpid = "wwf909985f20e7bb66"
        corpsecret = "ZxzplF-X8jacr_C5Hda0WMIFTM2VtrlGUneQvXGJDEQ"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        r = requests.get(url=url, params=param)
        self.token = r.json()["access_token"]

    def teardown(self):
        pass

    #创建标签
    def test_creat_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        params = {
            "access_token":self.token
        }
        json = {
            "tagname": "人力部",
            "tagid": 1     #非负整型，指定此参数时新增的标签会生成对应的标签id，不指定时则以目前最大的id自增
        }
        r = requests.post(url=url,params=params,json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    #获取标签列表
    def test_getlist_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/list"
        params = {
            "access_token": self.token
        }
        r = requests.get(url=url, params=params)
        print(r.json())

    #更新标签名
    def test_update_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/update"
        params = {
            "access_token": self.token
        }
        json = {
            "tagid": 1,
            "tagname": "人力行政部"
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 增加标签成员
    def test_insertlistnum_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers"
        params = {
            "access_token": self.token
        }
        json = {
            "tagid": 1,
            "userlist": "YinYingYi"
        }
        r = requests.post(url=url, params=params,json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    #获取标签成员
    def test_getlistnum_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/get"
        params = {
            "access_token": self.token,
            "tagid": 1
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0

    #删除标签
    def test_delete_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/delete"
        params = {
            "access_token": self.token,
            "tagid": 1
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0
