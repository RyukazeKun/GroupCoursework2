from . import views
from django.urls import path, include

urlpatterns = [
    path('home/', views.homePage),
    path('account/', views.accountPage),
    path('account/update/', views.updateAccountPage),
    path('account/update/confirmed/', views.updateAccountPage),
    path('equipment/', views.equipmentsPage),
    path('reservation/', views.reservationsPage),
    path('reservation/bookequipment/', views.bookEquipmentPage),
    path('notification/', views.notificationsPage),
    path('CreateUserAccount.html', views.register),
]
