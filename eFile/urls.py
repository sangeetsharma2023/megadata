# eFile/urls.py
from django.urls import path
from .views import home
from .views import received_list, received_add, received_edit, received_delete
from .views import issue_letter_list, issue_letter_detail, issue_letter_add, issue_letter_edit, issue_letter_delete
from .views import matter_add, matter_delete, matter_detail, matter_edit, matter_list, matter_detail_with_corr
from .views import mattercorr_add, mattercorr_delete, mattercorr_detail, mattercorr_edit, mattercorr_list, mattercorr_add_with_matter
from .views import create_flow, received_list_with_status, create_letter_flow, verify_received, letter_flow_detail
from .views import letter_flow_list_by_received,report_received_all, action_view, verify_view

urlpatterns = [
    path('home/',home,name='home'),

    path('received/', received_list, name='received_list'),
    #path('received/<int:pk>/', received_detail, name='received_detail'),
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
    path('matters/<int:pk>/detail_with_corr/', matter_detail_with_corr, name='matter_detail_with_corr'),
    path('matters/<int:matter_id>/add_mattercorr/', mattercorr_add_with_matter, name='mattercorr_add_with_matter'),

    path('mattercorrs/', mattercorr_list, name='mattercorr_list'),
    path('mattercorrs/<int:pk>/', mattercorr_detail, name='mattercorr_detail'),
    path('mattercorrs/add/', mattercorr_add, name='mattercorr_add'),
    path('mattercorrs/<int:pk>/edit/', mattercorr_edit, name='mattercorr_edit'),
    path('mattercorrs/<int:pk>/delete/', mattercorr_delete, name='mattercorr_delete'),

    path('create_flow/<int:receive_id>/', create_flow, name='create_flow'),
    path('received_list_with_status/', received_list_with_status, name='received_list_with_status'),
    path('create_letter_flow/<int:received_id>/', create_letter_flow, name='create_letter_flow'),
    path('verify_received/<int:received_id>/', verify_received, name='verify_received'),
    path('letter_flow_detail/<int:pk>/', letter_flow_detail, name='letter_flow_detail'),
    path('letter_flows/<int:received_id>/', letter_flow_list_by_received, name='letter_flow_list_by_received'),
    path('report_received_all/', report_received_all, name='report_received_all'),

    path('action/<int:receive_id>/', action_view, name='action_view'),
    path('verify/<int:receive_id>/', verify_view, name='verify_view'),

]

