from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from api_request import views,forms
from api_request.models import Entry
from utils import main
# Create your views here.
def index(request):
    #return render(request,'api_request/index.html')
    return HttpResponseRedirect('/login/')

def form_view(request):
    form=forms.Form()
    return render(request,'api_request/form.html',{'form':form})

def after(request):
    if request.method == 'POST':
        form = forms.Form(request.POST)

        if form.is_valid():
            u=form.cleaned_data['url']
            t=form.cleaned_data['template']
            c=form.cleaned_data['currency']
            l = list(Entry.objects.all().values_list('store_url', flat=True))
            if u in l:
                obj = Entry.objects.get(store_url = u)
                output = obj.vid_url
                error = None
            else:
                output,error = main.fetch_url(t,u,c)
        if(output != None and error == None):
            entry = Entry.objects.get_or_create(store_url = u,vid_url = output)[0]
            return render(request,'api_request/after.html',{'output':output})
        else:
            return HttpResponse("<h1>" + str(error) + "</h1>")

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
