# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from crazysearch.models import *
from django.db.models import Q
import re

def main_page(request):
	template=get_template('main_page.html')
	variable=Context({})
	output=template.render(variable)
	return HttpResponse(output)

def search(request):
	output="hi"
	if request.REQUEST.has_key("q"):
		query=request.REQUEST["q"]
		users=User.objects.filter(Q(nickname__istartswith=query)|Q(name__istartswith=query))
		users=users.order_by('-rank')[:10]
		if request.REQUEST.has_key("xml"):
			template=get_template('template.xml')
			variable=Context({'query':query,'users':users})
			output=template.render(variable)
		elif request.REQUEST.has_key("json"):
			names=descriptions=urls=""
			t=0
			for user in users:
				if t!=0:
					names+=","
					descriptions+=","
					urls+=","
				t=1
				names+='"'+user.nickname.replace("\"","&quot;")+'"'
				descriptions+="\""+user.description.replace("\"","&quot;")+"\""
				urls+="\"http://me2day.net/"+user.name+"\""
			template=get_template('template.json')
			variable=Context({'query':query,'names':names,'descriptions':descriptions,'urls':urls})
			output=template.render(variable)
		elif query.endswith("}"):
			m=re.search("(.*)\{(.*)\}",query)
			body=m.group(1)
			tag=m.group(2)
			return HttpResponseRedirect("http://me2day.net/posts/new?new_post[body]="+body+"&new_post[tags]="+tag)
		elif query.endswith("!"):
			m=re.search("(.*)!",query)
			word=m.group(1)
			if re.match("[a-zA-Z]",word):
				return HttpResponseRedirect("http://www.google.com/dictionary?aq=f&langpair=ko|en&hl=ko&q="+word)
			else:
				return HttpResponseRedirect("http://www.google.com/dictionary?aq=f&langpair=ko|ko&hl=ko&q="+word)
		else:
			try:
				return HttpResponseRedirect("http://me2day.net/"+users[0].name)
			except Exception:
				return HttpResponseRedirect("http://www.google.com/search?q="+query.replace(" ","+"))
	else:
	  output="hello3"
	return HttpResponse(output)

