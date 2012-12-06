# Create your views here.
from django.utils import simplejson as json, simplejson
from django.template import Context, loader
from django import http


class JSONTemplate(object):
    def render_to_response(self, context):
        """ Parent JSON mixin  """
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **kwargs):
        return http.HttpResponse(content, content_type="application/json", **kwargs)

    def convert_context_to_json(self, context):
        # Render the template
        return json.dumps(context, ensure_ascii=False)


class JSONTemplateRenderMixin(JSONTemplate):
    """
    Render a template as an ajax response. For example a dynamic table shown in a modal window
    """
    def convert_context_to_json(self, context):
        t = loader.get_template(self.template_name)
        data = {}
        data["template"] = t.render(Context(context))
        data["message"] = "success"
        return json.dumps(data, ensure_ascii=False)


class JSONRenderMixin(JSONTemplate):
    """
    Just return plain old JSON to be consumed by the browser
    """
    pass

