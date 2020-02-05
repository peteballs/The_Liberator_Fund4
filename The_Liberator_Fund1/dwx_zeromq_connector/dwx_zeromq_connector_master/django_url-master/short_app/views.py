#from django.shortcuts import render
from tiny_link import models
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
   short_url = None
   if request.method == "POST":
      link_db = models.Link()
      link_db.link = request.POST.get("url")
      link_db.save()
      short_url = request.build_absolute_uri(link_db.get_short_id())
   return render_to_response("index.html",
                             {"short_url":short_url},
                             context_instance=RequestContext(request))
