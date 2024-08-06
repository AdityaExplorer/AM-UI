from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Home,name='home_page_acesss'),
    path('Create_Acc',views.Create_Accs,name='Create_Acc_ACCOUNT'),
    path('add_data', views.add_data, name='add_data'),
    path('view_data', views.view_data, name='view_data'),
    path('edit_data/<int:user_id>/', views.edit_data, name='edit_data'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
