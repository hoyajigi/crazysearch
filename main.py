#!/usr/bin/env python

import wsgiref.handlers

#from google.appengine.api import mail

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class Person(db.Model):
	name=db.StringProperty(required=True)
	url=db.StringProperty(required=True)
	description=db.StringProperty(required=True)
	img=db.StringProperty(required=True)
	rank=db.IntegerProperty()


class MyHandler(webapp.RequestHandler):
	def get(self):
		query=self.request.get('q')
		items=db.GqlQuery('SELECT * FROM Person WHERE name=query OR url=query ORDER BY rank DESC')
		if self.request.get('xml'):
			values={
				'query':query,
				'items':items
			}
			self.response.out.write(template.render('template.xml',values))
		
		elif self.request.get('json'):
			names=
			descriptions=
			urls=
			values={
				'query':query,
				'names':names,
				'descriptions':descriptions,
				'urls':urls
			}
			self.response.out.write(template.render('template.xml',values))	
		
	def post(self):
		self.redirect('/')





def main():
	app=webapp.WSGIApplication([(r'.*',MyHandler)],debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__=="__main__":
	main()
	
	
