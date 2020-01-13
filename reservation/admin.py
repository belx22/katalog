from django.contrib import admin
from reservation.models import Cite,Chambre,Categorie,Commentaire,client,reserv

#admin.AdminSite.app_index_template = './templates/admin/app_index.html'

admin.AdminSite.site_header = 'Administration de katalogue'
admin.site.register(Commentaire)
admin.site.register(Categorie)
admin.site.register(Cite)
admin.site.register(Chambre)
admin.site.register(client)
admin.site.register(reserv)