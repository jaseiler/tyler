# Create your views here.
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from BeautifulSoup import BeautifulSoup
import urllib2, re
from xml import etree
from xml.etree import ElementTree as ET
from xml.parsers.expat import ExpatError
from io import BytesIO

from .forms import CompanionForm, Article

class CompanionArticleListView(generic.ListView):
    model = Article
    template_name = 'supportingmaterials/index.html'
    context_object_name = 'companion_article_list'

class CompanionArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'supportingmaterials/detail.html'
    
#def companion(request):
#	if request.method == 'POST':
#		form = CompanionForm(request.POST, extra=request.POST.get('extra_author_count'))
#		return HttpResponseRedirect('/supportingmaterials/')
#	else:
#		form = CompanionForm()
#		return render(request, "create.html", { 'form': form })   

class CreateView(TemplateView):
	template_name='supportingmaterials/create.html'
	model = Article

def search(request):
	template_name='supportingmaterials/create.html'
	model = Article
	if 'doi' in request.GET:
		doi = request.GET['doi']
		form = CompanionForm()
		form.fields["doi"].initial = doi
		path = urllib2.urlopen("http://doi.crossref.org/servlet/query?pid=jas2385@columbia.edu&format=info&id="+doi)
		#path = open("http://doi.crossref.org/servlet/query?pid=jas2385@columbia.edu&format=info&id="+doi)
		#xmlDoc = open(path, 'rt')
		xmlDocData = path.read()
		xmlDoc = BytesIO(xmlDocData)
		namespaces = {
		"":"http://www.crossref.org/qrschema/3.0",
		"":"http://www.crossref.org/xschema/1.1",
		}	
		for prefix, uri in namespaces.iteritems():
		    ET.register_namespace(prefix, uri)
		month = ''
		tree = ET.parse(xmlDoc)
		#tree = etree.XML(xmlDocData)
		#tree=ET.fromstring(xmlDocData)
		ns0 = 'http://www.crossref.org/qrschema/3.0'
		ns2 = 'http://www.crossref.org/xschema/1.1'
		#print ET.tostring(tree)
		record ='./*/*/*/{%s}doi-record'%ns0
		journal = record+'./*/{%s}journal'%ns2
		authors = ''
		article_url = ''
		for node in tree.getiterator():
			#print node.tag, node.attrib
			if node.tag == '{%s}full_title'%ns2:
				print node.text
				form.fields['journal'].initial= node.text
			elif node.tag =='{%s}issn'%ns2:
				print node.text
				form.fields['pages'].initial = node.text
			elif node.tag =='{%s}issue'%ns2:
				print node.text
				form.fields['issue'].initial = node.text
			elif node.tag =='{%s}volume'%ns2:
				print node.text
				form.fields['volume'].initial = node.text
			elif node.tag =='{%s}month'%ns2:
				print node.text
				month = node.text
			#elif node.tag =='{%s}year'%ns2:
			#	print node.text
			#	form.data['pub_date'].initial = month +" "+ node.text
			elif node.tag =='{%s}title'%ns2:
				print node.text
				form.fields['title'].initial = node.text
			elif node.tag =='{%s}given_name'%ns2:
				print node.text
				authors += node.text
			elif node.tag =='{%s}surname'%ns2:
				print node.text
				authors += ' %s , '%node.text
			elif node.tag =='{%s}resource'%ns2:
				print node.text
				article_url = node.text
				form.fields['article_url'].initial= node.text
		content = urllib2.urlopen(article_url).read()
		abstract = re.search("class='aps-abstractbox'.*?><p>(.*?)</p></div>", content).group(1)
		print abstract
		form.fields['abstract_text'].initial= abstract.replace('<span style="font-style: italic;">','').replace('</span>','').replace('<sub>','_').replace('</sub>','')
		#print(tree.find('./*/*/*/{%s}crm-item'% ns0).text )
		#form.data['pub_date'] = issue.find('publication_date/month').text + ' ' + issue.find('publication_date/year').text
		#for author in tree.iter('{%s}person_name'%ns2):
		#	authors.append(author.find('{%s}given_name'%ns2).text+' '+author.find('{%s}surname'%ns2).text)
		form.fields['authors'].initial = authors
		#form.save(commit=False)
		#return render_to_string('supportingmaterials/create.html', {'form': form})
		return render(request,'supportingmaterials/create.html', {'form': form})