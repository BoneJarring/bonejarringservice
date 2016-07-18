from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic



class IndexView(generic.DetailView):
    template_name = 'bjsvc/index.html'
    context_object_name = {}

    def get_queryset(self):
        return ()
