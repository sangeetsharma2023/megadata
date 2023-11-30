from django.urls import path
from .views import AddFileView, AddVerifyFlowView, CreateFlowView, DeleteVerifyFlowView, EditFileView, DeleteFileView, EditVerifyFlowView, HomeView, LetterFlowListView, VerifyFlowListView, ViewFileView, FileListView,FileInfoListView
from .views import AddSenderView, EditSenderView, DeleteSenderView, SenderListView, ViewSenderView
from .views import ReceivedWithNewMatterView,ReceivedWithExistingMatterView, ReceivedListView,ReceivedDeleteView,ReceivedDetailView,ReceivedEditView

from .views import get_file_info




app_name = 'fs'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AddFileView.as_view(), name='add_file'),
    path('edit/<int:file_id>/', EditFileView.as_view(), name='edit_file'),
    path('delete/<int:file_id>/', DeleteFileView.as_view(), name='delete_file'),
    path('view/', FileListView.as_view(), name='view_file_list'),
    path('view/<int:file_id>/', ViewFileView.as_view(), name='view_file'),
    path('file-info-popup/', FileInfoListView.as_view(template_name='fs/file_info_popup.html'), name='file_info_popup'),
    path('get_file_info/', get_file_info, name='get_file_info'),
    # Add other URL patterns as needed

    # url for Sender Model
    path('add_sender/', AddSenderView.as_view(), name='add_sender'),
    path('edit_sender/<int:sender_id>/', EditSenderView.as_view(), name='edit_sender'),
    path('delete_sender/<int:sender_id>/', DeleteSenderView.as_view(), name='delete_sender'),
    path('sender_list/', SenderListView.as_view(), name='sender_list'),
    path('view_sender/<int:sender_id>/', ViewSenderView.as_view(), name='view_sender'),

    #Received With matter
    path('received_with_new_matter/', ReceivedWithNewMatterView.as_view(), name='received_with_new_matter'),
    path('received_with_existing_matter/', ReceivedWithExistingMatterView.as_view(), name='received_with_existing_matter'),
    path('received_list/', ReceivedListView.as_view(), name='received_list'),

    path('received_edit/<int:pk>/', ReceivedEditView.as_view(), name='received_edit'),
    path('received_delete/<int:pk>/', ReceivedDeleteView.as_view(), name='received_delete'),
    path('received_detail/<int:pk>/', ReceivedDetailView.as_view(), name='received_detail'),

    path('create_flow/<int:receive_id>/', CreateFlowView.as_view(), name='create_flow'),
    path('add_verify_flow/<int:letter_flow_id>/', AddVerifyFlowView.as_view(), name='add_verify_flow'),
    path('edit_verify_flow/<int:verify_flow_id>/', EditVerifyFlowView.as_view(), name='edit_verify_flow'),
    path('delete_verify_flow/<int:verify_flow_id>/', DeleteVerifyFlowView.as_view(), name='delete_verify_flow'),
    path('view_verify_flows/', VerifyFlowListView.as_view(), name='view_verify_flows'),
    path('letter_flow_list/<int:receive_id>/', LetterFlowListView.as_view(), name='letter_flow_list'),
 


]

    


