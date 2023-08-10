from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tables', views.tables, name='tables'),
    path('charts',views.charts, name='charts'),
    path('details/<int:id>',views.studentDetail, name='details'),
]