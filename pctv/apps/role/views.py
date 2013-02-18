from apps.role.forms import UserCreateForm, UserEditForm
from django.contrib.auth.models import Group, User
from django.forms.models import model_to_dict
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, TemplateView


class RoleIndexView(TemplateView):
    """
    Placeholder view... still don't know what to place here
    """
    template_name = "role/index.html"

    def get(self, request):
        # Be kewl
        object_list = Group.objects.all()
        user_list = User.objects.all()

        return self.render_to_response({
            "object_list": object_list,
            "user_list": user_list
        })


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
            group = form.cleaned_data.get("group")
            user = User()
            user.username = form.cleaned_data["username"]
            user.email = form.cleaned_data["email"]
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.is_staff = True

            # If selected group is Master also check is_admin
            if form.cleaned_data["group"].name == 'Administrador':
                user.is_superuser = True

            user.set_password(form.cleaned_data["password2"])
            user.save()
            user.groups.add(group)
            user.save()
            return redirect("role_dashboard")

        return self.render_to_response({"form": form})


class RoleUserEditView(TemplateView):
    template_name = "role/user_create.html"

    def get(self, request, user_id=None):
        user = get_object_or_404(User, pk=user_id)
        user_dict = model_to_dict(user)
        user_dict["commission_percentage"] = user.account.commission_percentage
        form = UserEditForm(initial=user_dict)

        return self.render_to_response({"form": form})

    def post(self, request, user_id=None):
        user = get_object_or_404(User, pk=user_id)
        form = UserEditForm(request.POST, request.FILES)
        if form.is_valid():
            group = form.cleaned_data.get("group")
            user.username = form.cleaned_data["username"]
            user.email = form.cleaned_data.get("email")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")

            if form.cleaned_data["group"] == "Administrador":
                user.is_superuser = True

            # We'll add this because some users might have more than one
            for g in user.groups.all():
                user.groups.remove(g)
            user.groups.add(group)
            user.account.commission_percentage = form.cleaned_data["commission_percentage"]
            user.account.save()
            user.save()
            return redirect("role_dashboard")

        return self.render_to_response({"form": form})


class RoleUserDeleteView(TemplateView):
    def get(self, request, user_id=None):
        User.objects.get(pk=user_id).delete()
        return redirect("role_dashboard")


class RoleUserView(ListView):
    template_name = "role/user_view.html"
    model = User
