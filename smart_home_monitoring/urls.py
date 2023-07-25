from django.urls import path
from smart_home_monitoring import views


app_name = 'smart_home_monitoring'

urlpatterns = [
    path('list/', views.index, name='lecturer_list'),
    path('smart/data/', views.upload_data, name='upload_data'),
    path('smart/data/download/page', views.download_page, name='download_page'),
    path('smart/data/download/', views.downloads, name='download'),
    path('smart/data/about', views.about, name='about'),
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('logout', views.logoutUser, name='logout'),
]