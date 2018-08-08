#-*- coding: UTF-8 -*-
from locust import HttpLocust, TaskSet, task
import json
import subprocess
import requests

'''创建UserBehavior()类继承TaskSet类，为用户行为。'''
class UserBehavior(TaskSet):

#创建baidu() 方法表示一个行为，访问百度首页。用@task() 装饰该方法为一个任务。1表示一个Locust实例被挑选执行的权重，数值越大，
#执行频率越高。在当前UserBehavior()行为下只有一个baidu()任务，所以，这里的权重设置为几，并无影响。
    def on_start(self):
        pass

    @task(1)
    def getTagVals(self):
        u'''
        request_url:请求路径
        request_params:请求头参数
        request_json:请求json参数
        '''
        request_url = "http://114.116.52.169:8005/tsp/continental-gateway/continental-gateway/realTimeUploadData"
        request_params = {"Contenttype" : "application/json"}
        try:
            with open("./real_time_upload_data.json", "r", encoding='utf-8') as f:
                request_json = json.dump(f.read())
        except (IOError):
            print ("open json filed!!!")

        respoonse = requests.post(url=request_url, params=request_params, json=request_json)

        if respoonse.status_code != 200:
            print ("返回异常：")
            print ("请求状态码：", respoonse.status_code)
        elif respoonse.status_code == 200:
            print ("返回成功")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

