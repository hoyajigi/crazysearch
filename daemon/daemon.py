# -*- coding: utf-8 -*-
import me2dayAPI
import _mysql
import re
from xml.dom.minidom import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

r = me2dayAPI.init("", "", 'xml')

def decodingXML(xmlStr):
	dom = parseString(xmlStr)
	return dom.toxml('utf-8')

def gt(dom,name):
	try:
		return dom.getElementsByTagName(name)[0].childNodes[0].data
	except Exception:
		return ""

def query(sql):
	db=_mysql.connect("localhost","root","","me2echelon")
	db.set_character_set('utf8')
	db.query(sql)
	r=db.store_result()
	if r:
		data=r.fetch_row()
	else:
		data=((""),)
	db.close()
	return data[0]

def sw():
	sql="SELECT `name` FROM `crazysearch_user` ORDER BY `last` ASC LIMIT 0,1"
	return query(sql)[0]

def ip(name,nickname,description,img,rank):
	sql=u"""INSERT INTO `me2echelon`.`crazysearch_user` (`id` ,`name` ,`nickname` ,`description` ,`img` ,`rank` ,`last`)
	VALUES (NULL , '%s', '%s', '%s', '%s', '%s', NOW( ));
	"""%(name,_mysql.escape_string(nickname),_mysql.escape_string(description),img,rank)
	sql=sql.encode('utf-8')
	try:
		query(sql)
	except Exception:
		pass

def ut(name):
	sql="UPDATE `me2echelon`.`crazysearch_user` SET `last` = NOW( ) WHERE `crazysearch_user`.`name` ='%s' LIMIT 1 ;"%name
	query(sql)


while 1: #데몬은 죽지 않는다
	who=sw().rstrip()
	print who
	res = me2dayAPI.getFriends(who,"all")
#	dom = decodingXML(res.body)
	dom=parseString(res.body)
	friends=dom.getElementsByTagName("person")
	#=re.findall("<id>(.*)</id>",r)
	for friend in friends:
		name=gt(friend,"id")
		nickname=gt(friend,"nickname")
		description=gt(friend,"description")
		img=gt(friend,"face")
		rank=gt(friend,"friendsCount")
		ip(name,nickname,description,img,rank)
#	faces=re.findall("<face>(.*)</face>",r)
#	print(faces[0])
#	break
	ut(who)

#crazy search
#shout=Shout(message=self.request.get('message'),who=self.request.get('who'))
#shout.put()




#friend deletion alert
#mail.send_mail("HOYAJIGI <hoyajigi@gmail.com>","hoyajigi@gmail.com","new message",self.request.get('message'))


#search engine






