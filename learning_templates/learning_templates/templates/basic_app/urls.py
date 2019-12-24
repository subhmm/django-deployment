from django.conf.urls import urls
from basic_app import views

# template tagging
app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.index, name='index'),
    path('admin/',admin.site.urls)
    path('basic_app/',include('basic_app.urls'))
]
