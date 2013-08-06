# coding=UTF-8

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

import unittest
import me2day

runner = me2day.commandRunner()
userID = runner.loadConfig()

class me2dayTestCase(unittest.TestCase):

	def test1_getLatests(self):
		self.assertEquals(runner.run('getLatests %s' % userID), 200)
	def test2_getFriends(self):
		self.assertEquals(runner.run('getFriends %s all' % userID), 200)
	# must call the teset4,5 after the test3 is called 
	# The test3,4 use the post ID created by the test3
	def test3_createPost(self):
		self.assertEquals(runner.run('createPost \"me2day API unit test 3\" \"me2py unittest 테스트\"'), 200)
	def test4_createComment(self):
		self.assertEquals(runner.run('createComment %s \"createComment API Test\"' % runner.lastCreatedPermLink), 200)
	def test5_getComments(self):
		self.assertEquals(runner.run('getComments %s' % runner.lastCreatedPermLink), 200)
	def test6_getPerson(self):
		self.assertEquals(runner.run('getPerson %s' % userID), 200)
	def test7_getSettings(self):
		self.assertEquals(runner.run('getSettings'), 200)
	def test8_noop(self):
		self.assertEquals(runner.run('noop'), 200)

if __name__ == '__main__':
	unittest.main(argv=(' ', '-v'))
