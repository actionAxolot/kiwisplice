from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from views import *


urlpatterns = patterns('',
#	url("^crear-rol/$", login_required(RoleCreateView.as_view()), name="role_create"),
#    url("^crear-rol/(?P<role_id>\w+)/$", login_required(RoleCreateView.as_view()), name="role_create_params"),
    url("^listar-roles/", login_required(RoleView.as_view()), name="role_view"),
    url("^editar-usuario/(?P<user_id>\w+)/$", login_required(RoleUserEditView.as_view()), name="role_create_user_params"),
    url("^crear-usuario/$", login_required(RoleUserCreateView.as_view()), name="role_create_user"),
    url("^listar-usuarios/", login_required(RoleUserView.as_view()), name="role_view_user"),
    url("^borrar-rol/(?P<role_id>\w+)/$", login_required(RoleDeleteView.as_view()), name="role_delete_params"),
    url("^borrar-usuario/(?P<user_id>\w+)/$", login_required(RoleUserDeleteView.as_view()), name="role_delete_user_params"),
    url("^$", login_required(RoleIndexView.as_view()), name="role_dashboard"),
)
