#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 18:30:23
# @Author  : sxmsr (582124404@qq.com)
# @Link    : www.baidu.com
# @Version : $Id$

from flask import Flask,render_template,redirect,url_for,request,current_app
from CetTicket import CetTicket,TicketNotFound


app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>hello world</h1>"

def getScore(temp_ticket=None,temp_name=None):
	ticket=temp_ticket
	name = temp_name
	try:
		result=CetTicket.get_score(ticket,name)
		result['error'] = False
		return result
	except:
		return dict(error=True)

def getTicket(temp_province=None,temp_school=None,temp_name=None,temp_cet=None):
	province = temp_province
	school = temp_school
	name = temp_name
	cet = temp_cet
	result = dict(error=False)
	try:
		result['ticket_number']=CetTicket.find_ticket_number(province,school,name,cet_type=cet)
	except TicketNotFound:
		result['error'] = True
	return result

def get_DLNU_Score(temp_name=None,temp_cet=None):
	province = u'辽宁'
	school = u'大连民族大学'
	name = temp_name
	cet=temp_cet
	result = getTicket(province,school,name,cet)
	if (result["error"]):
		return result
	ticket=result['ticket_number']
	return getScore(ticket,name)


if __name__ == "__main__":
	app.run(debug=True)
