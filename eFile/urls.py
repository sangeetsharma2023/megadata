# eFile/urls.py
from django.urls import path
from .views import received_list, received_detail, received_add, received_edit, received_delete
from .views import issue_letter_list, issue_letter_detail, issue_letter_add, issue_letter_edit, issue_letter_delete
from .views import matter_add, matter_delete, matter_detail, matter_edit, matter_list
from .views import mattercorr_add, mattercorr_delete, mattercorr_detail, mattercorr_edit, mattercorr_list


urlpatterns = [
    path('received/', received_list, name='received_list'),
    path('received/<int:pk>/', received_detail, name='received_detail'),
    path('received/add/', received_add, name='received_add'),
    path('received/<int:pk>/edit/', received_edit, name='received_edit'),
    path('received/<int:pk>/delete/', received_delete, name='received_delete'),
    
    path('issue_letters/', issue_letter_list, name='issue_letter_list'),
    path('issue_letters/<int:pk>/', issue_letter_detail, name='issue_letter_detail'),
    path('issue_letters/add/', issue_letter_add, name='issue_letter_add'),
    path('issue_letters/<int:pk>/edit/', issue_letter_edit, name='issue_letter_edit'),
    path('issue_letters/<int:pk>/delete/', issue_letter_delete, name='issue_letter_delete'),

    path('matter/', matter_list, name='matter_list'),   
    path('matter/<int:pk>/', matter_detail, name='matter_detail'),
    path('matter/add/', matter_add, name='matter_add'),
    path('matter/<int:pk>/edit/', matter_edit, name='matter_edit'),
    path('matter/<int:pk>/delete/', matter_delete, name='matter_delete'),

    path('mattercorrs/', mattercorr_list, name='mattercorr_list'),
    path('mattercorrs/<int:pk>/', mattercorr_detail, name='mattercorr_detail'),
    path('mattercorrs/add/', mattercorr_add, name='mattercorr_add'),
    path('mattercorrs/<int:pk>/edit/', mattercorr_edit, name='mattercorr_edit'),
    path('mattercorrs/<int:pk>/delete/', mattercorr_delete, name='mattercorr_delete'),


]

