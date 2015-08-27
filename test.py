#!/usr/bin/env python
#-*-coding:utf-8-*-
# Copyright 2009 chksong
#  chksong@qq.com
#

import os

import  tornado
import  tornado.web as web
import  tornado.ioloop
import  tornado.auth
import  tornado.httpserver
import  tornado.options

from tornado.options import  define , options

import  ueditorhander
import  upLoadFile

define("port",default=30000,help="run on the given port", type=int)

class testUeditor(tornado.web.RequestHandler):
    def get(self):

        self.render("ueditor.html")

    def post(self):
        pass

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/admin/ueditorHander", ueditorhander.UEditorManager),
            (r"/admin/uploadimage", upLoadFile.UpLoadImage),
            (r"/",testUeditor),
        ]

        setting =  dict (
            blog_title=u"testUeditor",
            blog_nav_First=u"主页",
            template_path=os.path.join(os.path.dirname(__file__),"templates"),
            static_path=os.path.join(os.path.dirname(__file__),"static"),
            xsrf_cookires=True,
            cookie_secret="I321Qu+ZacEL3uMlRPgVkrmmzn1FvKvYhP3Lobc",
            login_url="/auth/login" ,
            debug=True,
            autoescape=None,
        )

        tornado.web.Application.__init__(self,handlers,**setting)

def main():
    tornado.options.parse_command_line()
    http_server =tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ ==  "__main__":
    main()

