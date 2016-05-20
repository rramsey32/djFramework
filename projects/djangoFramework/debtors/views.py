from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Company, Debtor, Debt, Comment

def index(request):
    latest_debtor_list = Debtor.objects.order_by("-debtor_name")[:5]
    context = {'latest_debtor_list': latest_debtor_list}
    return render(request, 'debtors/index.html', context)

def detail(request, debtor_id):
    try:
        debtor = Debtor.objects.get(pk=debtor_id)
    except Debt.DoesNotExist:
        raise Http404("Debt does not exist")
    return render(request, 'debtors/detail.html', {'debtor': debtor})

def profile(request):
    return render_to_response("account/profile.html",locals(),context_instance=RequestContext(request))