from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('clients/',views.getClient,name='getClient'),
    path('client/create',views.createClient,name='createClient'),
    path('client/update/<int:id>',views.updateClient,name='updateClient'),
    path('client/delete/<int:id>',views.deleteClient,name='deleteClient'),
    path('offers/',views.getOffer,name='getOffer'),
    path('offer/update',views.updateOffer,name='updateOffer'),
    path('offer/create',views.createOffer,name='createOffer'),
    path('offer/delete',views.deleteOffer,name='deleteOffer'),
    path('agreements/',views.getAgreement,name='getAgreement'),
    path('agreement/update',views.updateAgreement,name='updateAgreement'),
    path('agreement/create',views.createAgreement,name='createAgreement'),
    path('agreement/delete',views.deleteAgreement,name='deleteAgreement')
]