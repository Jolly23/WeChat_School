# -*- coding: utf-8 -*-
from app import db
from flask import url_for
from app.user.models import regUser
from app.education.models import Course, User_course

from app.library.newbook_list_httpRequestVersion import book_list
from app.internet.drcom import drcom
from app.education.courses_lis import urp_courses
from app.education.urp import urp

class checkevent:
    def __init__(self, fromuser):

        self.fromuser = fromuser
        self.exist_user = regUser.query.filter_by(openid = self.fromuser).first()


    def recentgrade(self):
        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            geturp = urp(self.exist_user.username, self.exist_user.password_urp)
            if geturp.login():
                grades = geturp.get_recentdata()
                return grades
            else:
                text = u'教务系统密码错误,请重新绑定'
                return text

    def resitgrade(self):
        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            geturp = urp(self.exist_user.username, self.exist_user.password_urp)
            if geturp.login():
                grades = geturp.resitData()
                return grades
            else:
                text = u'教务系统密码错误,请重新绑定'
                return text

    def testinfo(self):
        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            geturp = urp(self.exist_user.username, self.exist_user.password_urp)
            if geturp.login():
                text = geturp.testInfo()
                return text
            else:
                text = u'教务系统密码错误,请重新绑定'
                return text

    def fullgrade(self):
        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            geturp = urp(self.exist_user.username, self.exist_user.password_urp)
            if geturp.login():
                grades = geturp.get_fulldata()
                return grades
            else:
                text = u'教务系统密码错误,请重新绑定'
                return text
    def webgrade(self):
	if self.exist_user is None:
	    text = u'请绑定后使用'
            return text
	else:
	    geturp = urp(self.exist_user.username, self.exist_user.password_urp)
            if geturp.login():
                grades = geturp.get_webgrade()
	        return grades
            else:
                text = u'教务系统密码错误,请重新绑定'
                return text

    def booklist(self):

        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            booklist = book_list(self.exist_user.username)
            booklist.login()
            booklist = booklist.get_booklists()
            return booklist

    def delay_return(self):

        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            delaybook = book_list(self.exist_user.username)
            delaybook.login()
            delaybook = delaybook.delay_return()
            return delaybook

    def course(self):
        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            getCourse = urp_courses(self.exist_user.username, self.exist_user.password_urp)
            data = getCourse.get_courses()
            return data

    def webcourse(self):
        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            getCourse = urp_courses(self.exist_user.username, self.exist_user.password_urp)
            data = getCourse.get_webusercourse()
            return data


    def updatecourses(self):
        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            getCourse = urp_courses(self.exist_user.username, self.exist_user.password_urp)
            if getCourse.login():
                getCourse.usercourse()
                return  u'课程更新成功'
            else:
                text = u'教务系统密码错误,请重新绑定'
                return text


    def binding(self):

        if self.exist_user is None:
	    url = url_for('user.login',openid=self.fromuser,_external=True)
            #url = u'http://127.0.0.1/login?openid=' + self.fromuser
            href = u'<a href="%s">点我绑定</a>' %url
            return href

        else:
            text = u'您已绑定,如密码变化,请先解除绑定.'
            return text

    def drcom(self):
        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            getdrcom= drcom(self.exist_user.username, self.exist_user.password_drcom)
            if getdrcom.login():
                flow_date = getdrcom.deal_data()
                return flow_date
            else:
                text = u'校园网密码错误,请重新绑定'
                return text

    def drcom_logout(self):
        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            getdrcom= drcom(self.exist_user.username, self.exist_user.password_drcom)
            if getdrcom.login():
                text = getdrcom.logout()
                return text
            else:
                status = u'校园网密码错误,请重新绑定'
                return status

    def unlock(self):
        if self.exist_user is None:
            text = u'请绑定后使用'
            return text
        else:
            db.session.delete(self.exist_user)
            db.session.commit()
            text = u'解除绑定成功'
            return text

    def codeinfo(self):
        text = u'因鄙人极厌官僚之风，深恶校园各项业务之繁琐，书信不能达无奈出此下策，历时两月终出此作略有瑕疵望众海涵。于念逝去之爱情，又鉴于民院帮手民大助手之粗俗，故得此名愿其永存于此      ————二流程序员书'
        return text

    def eggs(self):
        text = u"猜猜我是不是帅哥，答对有奖/:,@P/:,@P"
	#text = "http://autobox.meiriq.com/list/302da1ab"
        return text

    def userguide(self):
        url = url_for('user.feedback',_external=True)
        text = u'我写的还不够傻瓜吗？(*^__^*) 嘻嘻……just a joke\n<a href="%s">点我吐槽</a>'%url
        return text

    def subscribe(self):
        text = u'同学欢迎使用民院小偲\n使用教程：\n（一）点击账户，绑定用户\n（二）点击账户，课程更新!课程更新!课程更新!重要的事说三遍！\nTips:\n各项功能在面板对应的按钮中，不要问我！我只会扯淡。\n\n超过晚上8点，点击课表助手推送为第二天课表。课表信息错误时，请点击课程更新。\n当遇到什么问题或者发现bug回复即可，小编一定会第一时间帮你解决。'
        return text
    
    def weberror(self):
        text = u"获取信息的网站无法访问，请稍后再试"
        return text

    def key_check(self,key):
        lookup = {
            'binding': self.binding,
            'unlock': self.unlock,
            'updatecourses':self.updatecourses,
	    #'updatecourses':self.weberror,
            'drcom_logout': self.drcom_logout,
            'grade': self.recentgrade,
	    #'grade': self.weberror,
            'fullgrade':self.fullgrade,
	    #'fullgrade':self.weberror,
            'testinfo':self.testinfo,
	    #'testinfo':self.weberror,
            'course':self.course,
	    #'course':self.weberror,
            'book_list': self.booklist,
            'delaybook': self.delay_return,
            'drcom_flow': self.drcom,
            'codeinfo':self.codeinfo,
            'eggs': self.eggs,
            'userguide': self.userguide,
            'subscribe':self.subscribe,
            'resitgrade':self.resitgrade,
	    #'resitgrade':self.weberror,
	    'webgrade':self.webgrade,
	    'webcourse':self.webcourse,
	    'weberror':self.weberror

         }
        lookup.get(key, lambda: None)()
        func = lookup[key]
        return func()


