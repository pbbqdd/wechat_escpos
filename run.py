# -*- coding: utf-8 -*-
import time
from flask import Flask,request, make_response
import hashlib
import xml.etree.ElementTree as ET
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk import messages
from wechat_sdk.exceptions import ParseError
import test_printer as tp
import message123
conf = WechatConf(
    token='hfghdj',
    encrypt_mode='normal',
)
wechat = WechatBasic(conf=conf)
app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'] )
def wechat_auth():
  if request.method == 'GET':
    print request.data
    query = request.args  # GET 方法附上的参数
    print query
    signature = query.get('signature', '')
    timestamp = query.get('timestamp', '')
    nonce = query.get('nonce', '')
    echostr = query.get('echostr','')
    if wechat.check_signature(signature, timestamp, nonce):
      print 'Accept'
      return make_response(echostr)
    else:
      print 'Wrong'

#def wechat_text():
  if request.method =='POST':
    body= request.data
    try:
      wechat.parse_data(body)
      tp.printtest(wechat.message.get_text)
      tp.printtest("--------------------------------")
      tp.printtest(" ")
      
#      tp.printer.cut()
      return make_response("success")
    except ParseError:
      print "dddd"


  
if __name__ == '__main__':
	app.run(host="0.0.0.0")
