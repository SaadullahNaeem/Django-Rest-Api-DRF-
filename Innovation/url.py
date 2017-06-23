from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^api/project/create/$', views.Projects.as_view(), name='project_create'),
    url(r'^api/projects$', views.ProjectGet.as_view(), name='project_get'),
    url(r'^api/collaborator/create/$', views.CollaboratorCreate.as_view(), name='collaborative_create'),
    url(r'^api/collaborators$', views.CollaboratorGet.as_view(), name='collaborative_get'),

]

