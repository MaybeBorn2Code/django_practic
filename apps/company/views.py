# Python
from typing import Any

# Django
from django.shortcuts import render
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import (
    HttpRequest,
    HttpResponse,
    QueryDict,
)
from django.views.generic import (
    View,
    ListView,
)
from django.core.files.uploadedfile import InMemoryUploadedFile
from abstracts.mixins import HttpResponseMixin
# Local
from company.models import (
    Pen,
    Quantity,
)

from company.forms import (
    PenForm,
    QuantityForm
)


class PenView(HttpResponseMixin, View):
    """View special for Pen model."""

    form = PenForm

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        all_pen: QuerySet[PenForm] = Pen.objects.all()
        # delete duplicates of pen
        # have error in algoritm
        for row in Pen.objects.all().reverse():
            if Pen.objects.filter(title=row.title).count() > 1:
                row.delete()
        return self.get_http_response(
            request=request,
            template_name='html\pen.html',
            context={
                'ctx_form': self.form()
            }
        )

    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        data: PenForm = self.form(request.POST or None)
        if not data.is_valid():
            return HttpResponse("BAD")
        data.save()
        return HttpResponse("Pen sucessfully added")


class QuantityView(HttpResponseMixin, View):
    """View special for Quantity model."""

    form = QuantityForm

    def get(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        entered_keys: QuerySet[QuantityForm] = Quantity.objects.all()
        return self.get_http_response(
            request=request,
            template_name='html\quantity.html',
            context={
                'ctx_form': self.form()
            }
        )

    def post(
        self,
        request: HttpRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        data: QuantityForm = self.form(request.POST or None)
        if not data.is_valid():
            return HttpResponse("BAD, check input data!")
        data.save()
        return HttpResponse("Number of pen added successfully")
