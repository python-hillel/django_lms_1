from django.contrib import admin
from django.urls import path, re_path, include

from core.views import index
# from core.views import view_with_param
# from core.views import view_without_param


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('students/', include('students.urls')),

    # path('test/route/param/', view_without_param),          # test/route/param/
    # path(r'test/route/<str:value>/', view_with_param),       # test/route/df;lkjhrlkjgf's/
]

# \n    \t      \b


# https://  www.digitalocean.com   /community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru

# https://www.digitalocean.com/

# http://127.0.0.1:45632      /students/update/6/

# http://127.0.0.1:45632/students/students/update/6/
