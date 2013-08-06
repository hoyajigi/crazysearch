# me2day.py
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

import sys
import re
import me2dayAPI
from me2dayAPI import *
from xml.dom.minidom import *
from ConfigParser import *

class commandRunner:

	def decodingXML(self, xmlStr):
		dom = parseString(xmlStr)
		return dom.toxml('utf-8')

	def run(self, inputStr):
		cmd = inputStr.split(' ')		
		numOfParam = len(cmd) - 1
		
		res = me2dayResult('', 0)

		if cmd[0] == 'getFriends' or cmd[0] == 'gf':
			if numOfParam == 1:
				res = me2dayAPI.getFriends(cmd[1], 'all')
				r = self.decodingXML(res.body)
			elif numOfParam == 2:
				res = me2dayAPI.getFriends(cmd[1], cmd[2])
				r = self.decodingXML(res.body)
			else:
				r = 'Invalid Paramter'
			

		elif cmd[0] == 'createPost' or cmd[0] == 'cp':
			cmdList = re.findall('"[^"]*"', inputStr)
			if cmdList != None and len(cmdList) == 2:
				body = cmdList[0]
				body = body[1:len(body)-1]

				tags = cmdList[1]
				tags = tags[1:len(tags)-1]

				icon = 1 # default icon

				cmd[numOfParam].strip()
				if cmd[numOfParam].isdigit() == True: 
					icon = cmd[numOfParam]

				res = me2dayAPI.createPost(body, tags , icon)
				#r = decodingXML(res.body)
				dom = parseString(res.body)
				nodePermaLink = dom.getElementsByTagName('permalink')[0]
				self.lastCreatedPermLink = nodePermaLink.childNodes[0].data
				r = dom.toxml('utf-8')
			else:
				r = 'Invalid Parameters'
				
		elif cmd[0] == 'createComment' or cmd[0] == 'cc':
			if numOfParam >= 2:
				cmdList = re.findall('"[^"]*"', inputStr)
				if cmdList != None and len(cmdList) == 1:
					body = cmdList[0]
					body = body[1:len(body)-1]

					res = me2dayAPI.createComment(cmd[1], body)
					r = self.decodingXML(res.body)
			else:
				r = 'Invalid paramter'

		elif cmd[0] == 'getSettings' or cmd[0] == 'gs':
			if numOfParam == 0:
				res = me2dayAPI.getSettings()
				r = self.decodingXML(res.body)
			else:
				r = 'Invalid paramter'
		elif cmd[0] == 'getLatests' or cmd[0] == 'gl':
			if numOfParam == 1:
				res = me2dayAPI.getLatests(cmd[1])
				r = self.decodingXML(res.body)
			else:
				r = 'Invalid paramter'
				
		elif cmd[0] == 'getComments' or cmd[0] == 'gc':
			if numOfParam == 1:
				res = me2dayAPI.getComments(cmd[1])
				r = self.decodingXML(res.body)
			else:
				r = 'Invalid Parameter'
		elif cmd[0] == 'getPerson' or cmd[0] == 'gp':
			if numOfParam == 1:
				res = me2dayAPI.getPerson(cmd[1])
				r = self.decodingXML(res.body)
			else:
				r = 'Invalid Parameter'

		elif cmd[0] == 'noop':
			res = me2dayAPI.noop()
			r = self.decodingXML(res.body)
		elif cmd[0] == 'help' or cmd[0] == 'h':
			print 'me2day Commands:' 
			print 'createPost(cp)  createComment(cc)' 
			print 'getFriends(gf)  getLatests(gl) '
			print 'getPerson(gp)   getSettings(gs)'
			r = ''
		else:
			r = 'Invalid Command'

		print(r)
		
		return res.status


	def loadConfig(self):
		# Load the user information from the configuration file
		config = SafeConfigParser()
		configFileList = config.read('.me2day')

		# Create a new configuration file
		if len(configFileList) == 0:
			config.add_section("UserInfo")
			id = raw_input('\nInput your me2day ID? ')
			userKey = raw_input('Input your userKey? ')
			config.set('UserInfo', 'userID', id)
			config.set('UserInfo', 'userKey', userKey)
			f = open('.me2day', 'w')
			config.write(f)
			f.close()		
		else:
			try:
				id = config.get('UserInfo', 'userID')
				userKey = config.get('UserInfo', 'userKey')
			except NoSectionError:
				print 'No Section UserInfo' 
				print 'Check the configuration file'
				exit()

		r = me2dayAPI.init(id, userKey, 'xml')
		return id

if __name__ == '__main__':
	
	me2day = commandRunner()
	me2day.loadConfig()
	
	while 1:
		inputStr = raw_input('me2day>')
		if len(inputStr) == 0:
			continue
		if inputStr == 'quit' or inputStr[0] == 'q':
			print 'good bye'
			break
		else:
			me2day.run(inputStr)
			

