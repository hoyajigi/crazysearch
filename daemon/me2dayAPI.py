# me2dayAPI.py

"""
me2py - python software for me2day(http://me2day.net) (API Wrapper, Unit Test, Shell)
copyright(c) 2007 Hur,Joone (joone@kldp.org)

This file is part of me2py.
me2py is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
at your option) any later version.

me2py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


import base64
import hashlib
import urllib
import httplib
import random


class me2dayResult:
	def __init__(self, body, status):
		self.body = body
		self.status = status


class me2dayConnection:

	def init(self, id, userKey, dataForm):

		self.id = id
		self.userKey = userKey
		self.debug = None
		self.dataForm = dataForm

		md5 = hashlib.md5()
		nonce = '%08x' % random.randint(0, 16 ** 8 - 1) 
		md5.update(nonce + userKey)
		self.basic_auth = 'Basic %s' % base64.b64encode('%s:%s' % (self.id, nonce + md5.hexdigest())) 

	def request(self, api, userID = None, params = None):
		con = httplib.HTTPConnection('me2day.net')
		if self.debug:
			con.set_debuglevel(2)

		if userID == None:
			url = '/api/%s.%s' % (api, self.dataForm)
		else:
			url = '/api/%s/%s.%s' % (api, userID, self.dataForm)

		if params != None:
			url = url + '?%s' % params 

		con.putrequest('GET', url)
		con.putheader('me2_application_key','c16cc23fae375a4566f23de54501395a') 
		con.endheaders()

		res = con.getresponse()
		r = res.read()
		con.close()

		if self.debug:
			print res.status, res.reason

		return me2dayResult(r, res.status)

	def requestAuth(self, api, data = None):
		con = httplib.HTTPConnection('me2day.net:80')
		if self.debug:
			con.set_debuglevel(2)

		con.putrequest('POST','http://me2day.net/api/%s/%s.%s' % (api, self.id, self.dataForm))
		con.putheader('Authorization', self.basic_auth)
		con.putheader('me2_application_key','7737cfe3ebce29d901a3e31e9a8b16ce') 

		if data: 
			con.putheader('Content-length', len(data))
			con.putheader('Content-type', 'application/x-www-form-urlencoded')

		con.endheaders()
		if data: 
			con.send(data)
		res = con.getresponse()
		r = res.read()
		con.close()

		if self.debug:
			print res.status, res.reason

		return me2dayResult(r, res.status)

connection = me2dayConnection()

def init(id, userKey, dataForm):
	connection.init(id, userKey, dataForm)


def getFriends(userID, scope):
	return connection.request('get_friends', userID, 'scope=%s' % scope)

def createPost(body, tags, icon):
	postParam = urllib.urlencode({'post[body]': body, 'post[tags]': tags, 'post[icon]': icon})
	return connection.requestAuth('create_post', postParam); 

def createComment(post_id, body):
	postParam = urllib.urlencode({'post_id': post_id, 'body': body})
	return connection.requestAuth('create_comment', postParam)
	
def getComments(post_id):
	param = urllib.urlencode({'post_id': post_id})
	return connection.request('get_comments', None, param)

def getLatests(userID):
	return connection.request('get_latests', userID) 

def getPerson(userID):
	return connection.request('get_person', userID)

def getSettings():
	return connection.requestAuth('get_settings')

def noop():
	return connection.requestAuth('noop')

