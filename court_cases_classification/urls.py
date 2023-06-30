from django.urls import path
from court_cases_classification import views


app_name = 'court_cases_classification'

urlpatterns = [
    path('list/', views.index, name='lecturer_list'),
    path('data/', views.upload_data, name='court_case'),
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('logout', views.logoutUser, name='logout'),
]