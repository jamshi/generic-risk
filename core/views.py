# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.http import HttpResponse
from .models import RiskType
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import render


class RiskView(View):

    def get(self, request, risk_code=None):
        if risk_code is not None:
            return self._get_risk(risk_code)
        return self._get_all_risk()

    def _get_all_risk(self):
        risks = [x.deliver_formatted() for x in RiskType.objects.all()]
        return JsonResponse(risks, safe=False)

    def _get_risk(self, risk_code):
        try:
            risk = RiskType.objects.get(risk_code__iexact=risk_code)
            return JsonResponse(risk.deliver_formatted(), safe=False)
        except:
            return HttpResponseNotFound()


def home(request):
    return render(request, 'index.html')