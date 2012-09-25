# Create your views here.
from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse


class HomeView(RedirectView):
    """
    Redirect accordingly. If user's not logged in redirect to login view
    else redirect to... prospections for now
    """
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.url = reverse("prospection_dashboard")
        else:
            self.url = reverse("login")

        return super(HomeView, self).get(self, request, *args, **kwargs)


class LoginView(TemplateView):
    """Display a login form and process credentials"""
    template_name = "home/index.html"
