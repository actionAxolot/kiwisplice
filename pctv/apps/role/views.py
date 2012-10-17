from django.views.generic import ListView, TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from models import *
from forms import *


class RoleIndexView(TemplateView):
    """
    Placeholder view... still don't know what to place here
    """
    template_name = "role/index.html"

    def get(self, request):
        # Be kewl
        object_list = Role.objects.all()
        user_list = User.objects.all()

        return self.render_to_response({
            "object_list": object_list,
            "user_list": user_list
        })


class RoleCreateView(TemplateView):
    template_name = "role/create.html"

    def get(self, request, role_id=None):
        role = Role()
        if role_id:
            role = Role.objects.get(pk=role_id)

        form = RoleForm(instance=role)

        return self.render_to_response({"form": form})


    def post(self, request, role_id=None):
        role = Role()
        if role_id:
            role = Role.objects.get(pk=role_id)

        form = RoleForm(request.POST, request.FILES, instance=role)

        if form.is_valid():
            form.save()
            return redirect("role_dashboard")

        return self.render_to_response({"form": form})


class RoleView(TemplateView):
    template_name = "role/view.html"


class RoleUserCreateView(TemplateView):
    template_name = "role/user_create.html"

    def get(self, request):
        form = UserCreateForm()

        return self.render_to_response({"form": form})

    def post(self, request):
        form = UserCreateForm(request.POST, request.FILES)

        if form.is_valid():
            role = form.cleaned_data.get("role")
            user = User()
            user.username = form.cleaned_data["username"]
            user.email = form.cleaned_data["email"]
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.is_staff = True

            # If selected role is Master also check is_admin
            if form.cleaned_data["role"].slug == 'master':
                user.is_superuser = True

            user.set_password(form.cleaned_data["password2"])
            user.save()
            role.user.add(user)
            role.save()
            return redirect("role_dashboard")

        return self.render_to_response({"form": form})


class RoleUserEditView(TemplateView):
    template_name = "role/user_create.html"

    def get(self, request, user_id=None):
        user = get_object_or_404(User, pk=user_id)
        form = UserEditForm(initial=model_to_dict(user))

        return self.render_to_response({"form": form})

    def post(self, request, user_id=None):
        user = get_object_or_404(User, pk=user_id)
        form = UserEditForm(request.POST, request.FILES)
        if form.is_valid():
            role = form.cleaned_data.get("role")
            user.username = form.cleaned_data["username"]
            user.email = form.cleaned_data.get("email")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            role.user.add(user)
            role.save()
            return redirect("role_dashboard")

        return self.render_to_response({"form": form})


class RoleUserDeleteView(TemplateView):
    def get(self, request, user_id=None):
        User.objects.get(pk=user_id).delete()
        return redirect("role_dashboard")


class RoleUserView(ListView):
    template_name = "role/user_view.html"
    model = User


class RoleDeleteView(TemplateView):
    def get(self, request, role_id=None):
        if role_id:
            Role.objects.get(pk=role_id).delete()
            return redirect("role_dashboard")