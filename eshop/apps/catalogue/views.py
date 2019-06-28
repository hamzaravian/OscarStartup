# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render
from oscar.apps.catalogue.views import ProductDetailView as CoreProductDetailView

# Create your views here.
class ProductDetailView(CoreProductDetailView):
       def get_context_data(self, **kwargs):
              ctx = super(ProductDetailView, self).get_context_data(**kwargs)
              ctx['user'] = self.request.user
              return ctx
