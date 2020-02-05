from django.shortcuts import redirect, get_object_or_404
from django.db.models import F

def link(request, id):
   db_id = models.Link.deocde_id(id)
   link_db = get_object_or_404(models.Link, id=db_id)
   models.Link.objects.filter(id=db_id).update(hits=F('hits')+1)
   return redirect(link_db.link)