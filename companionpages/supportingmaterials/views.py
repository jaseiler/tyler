# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from .forms import CompanionForm
from .models import Article

class CompanionArticleListView(generic.ListView):
    model = Article
    template_name = 'supportingmaterials/index.html'
    context_object_name = 'companion_article_list'

class CompanionArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'supportingmaterials/detail.html'
    
def companion(request):
	if request.method == 'POST':
		form = CompanionForm(request.POST, extra=request.POST.get('extra_author_count'))
		return HttpResponseRedirect('/supportingmaterials/')
	else:
		form = CompanionForm()
		return render(request, "create.html", { 'form': form })   