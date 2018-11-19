# -*- coding: utf-8 -*-
import scrapy
# 向服务器发送post请求需要导入FormRequest模块
from scrapy.http import Request, FormRequest
import urllib.request


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    ua = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}

    # 第一次请求
    def start_requests(self):
        ua = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        # 设置form表单发送的地址/ 回调函数/ 是否保存cookie/ 用户代理
        return [Request("https://accounts.douban.com/login", callback=self.parse, meta={"cookiejar": 1}, headers=ua)]

    # 这里是回调函数parse，第二次请求，之后跳转到个人主页https://www.douban.com/people/187530448/
    def parse(self, response):
        # 获取验证码图片的地址，若captcha为0，说明不需要输入验证码；若captcha不为0，说明需要输入验证码
        captcha = response.xpath("//img[@id='captcha_image']/@src").extract()
        url = "https://accounts.douban.com/login"

        # 需要输入验证码
        if len(captcha) > 0:
            print("Need verification code!")
            localpath = "A:/result/42/captcha.png"
            # 将验证码图片存储到本地
            urllib.request.urlretrieve(captcha[0], filename=localpath)
            print("Please check picture and input verification code: ")
            # 等待输入
            captcha_value = input()

            data = {
                "form_email": "yuqing.github@gmail.com",
                "form_password": "dd1993376211",
                "captcha-solution": captcha_value,
                "redir": "https://www.douban.com/people/187530448/",
            }

        # 不需要输入验证码
        else:
            print("Do not need verification code!")
            data = {
                "form_email": "yuqing.github@gmail.com",
                "form_password": "dd1993376211",
                "redir": "https://www.douban.com/people/187530448/",
            }

        print("Logging...")
        # 使用return以列表[]的形式发送post请求, 将上述data中封装好的信息以post请求方式使用FormRequest发送
        return [FormRequest.from_response(response,
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          headers=self.ua,
                                          formdata=data,
                                          callback=self.next,
                                          )]

    # 这里是回调函数next，爬取个人主页https://www.douban.com/people/187530448/的信息
    def next(self, response):
        print("Crawler has successfully logged in and got the data in yuqing's homepage!")
        title = response.xpath("/html/head/title/text()").extract()
        note = response.xpath("//div[@class='note']/text()").extract()
        print(title[0])
        print(note[0])





