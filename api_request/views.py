from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from api_request import views,forms
from api_request.models import Entry
from utils import main
from django.utils import timezone
# Create your views here.
def index(request):
    return HttpResponseRedirect('/home/')

def home(request):
    return render(request,'api_request/home.html')

def create(request):
    form=forms.Form()
    return render(request,'api_request/form.html',{'form':form})

def after(request):
    flag=False
    if request.method == 'POST':
        form = forms.Form(request.POST)
        x = request.body.decode()
        oth = x[x.index('curr_other')+11:]

        if form.is_valid():

            u=form.cleaned_data['url']
            t=form.cleaned_data['template']
            c=form.cleaned_data['currency']
            if c == "other":
                if oth != "" and oth != "+":
                    c = oth
                else:
                    return HttpResponse("<h1>" + "Currency not entered!" + "</h1>")

            # l = list(Entry.objects.all())
            # for i in l:
            #     if i.store_url == u and i.template == t:
            #         flag=True
            #
            # if flag:
            #     obj = Entry.objects.get(store_url = u, template = t)
            #     output = obj.vid_url
            #     error = None
            # else:
            output,error = main.fetch_url(t,u,c)

            if(output != None and error == None):
                entry = Entry.objects.create(store_url = u,template = t,vid_url = output,timestamp=timezone.now())
                return render(request,'api_request/after.html',{'output':output})
            else:
                return HttpResponse("<h1>" + str(error) + "</h1>")

def view_all(request):
    urls_list = Entry.objects.order_by('timestamp')
    my_dict={'urls': urls_list}
    return render(request,'api_request/view.html',context=my_dict)

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
