# -*- coding: utf-8 -*-
"""
This has so much potential. We could create a Parent mixin that could be inherited
that way we could render a lot of different formats.
"""
# Create your views here.
from django.utils import simplejson as json
from django.utils.encoding import smart_unicode
from django.template import RequestContext, loader, defaultfilters
from django import http
from django.http import HttpResponse
import csv


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
        data["template"] = t.render(RequestContext(self.request, context))
        data["message"] = "success"
        return json.dumps(data, ensure_ascii=False)


class JSONRenderMixin(JSONTemplate):
    """
    Just return plain old JSON to be consumed by the browser
    """
    pass


class CSVRenderMixin(object):
    """
    Mixin for ListView. Override the render_to_response method
    so that it returns a nice csv file download thing
    if certain get parameter is found
    """
    csv_filename = "really_awesome_csv.csv"

    def prepare_data(self, queryset):
        """docstring for prepare_data"""
        prepared_data = list()
        values = queryset.values()
        keys = values[0].keys()
        prepared_data.append(keys)

        for v in values:
            row = list()
            for key in keys:
                if isinstance(v[key], unicode):
                    data = v[key].encode("utf8")
                else:
                    data = v[key]
                row.append(data)
            try:
                prepared_data.append(row)
            except UnicodeEncodeError:
                print "PROBLEM"
                continue

        return prepared_data

    def generate_file_download(self, data_list):
        """docstring for self.generate_file_download"""
        response = http.HttpResponse(mimetype="text/csv")
        response["Content-Disposition"] = "attachment; filename=%s" % self.csv_filename
        writer = csv.writer(response)

        for d in data_list:
            writer.writerow(d)

        return response

    def render_csv_to_response(self, queryset):
        """docstring for render_to_response"""
        return self.generate_file_download(self.prepare_data(queryset))

