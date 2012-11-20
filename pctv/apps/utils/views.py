# Create your views here.
from django.utils import simplejson as json
from django.template import Context, loader
from django import http


class JSONTemplateRenderMixin(object):
    template_name = "template.html"

    def render_to_response(self, context):
        """ Return a JSON response with the rendered template  """
        return self.get_json_response(self.convert_context_to_json(context))


    def get_json_response(self, content, **kwargs):
        return http.HttpResponse(content, content_type="application/json", **kwargs)

    def convert_context_to_json(self, context):
        # Render the template
        t = loader.get_template(self.template_name)
        data = {}
        data["template"] = t.render(Context(context))
        data["message"] = "success"
        return json.dumps(data, ensure_ascii=False)
