from tempfile import \
    template

from django.http import \
    HttpResponse
from django.shortcuts import render
from django.template import \
    loader
from .models import Member


# Create your views here.
from django.shortcuts import render
from .models import Member

# members
def members(request):
    mymembers = Member.objects.all().values()

    context = {
        'mymembers': mymembers,
        'value':36
    }
    return render(request, 'all_members.html', context)

# details
def details(request, id):
    mymember= Member.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'mymember': mymember,
    }
    return HttpResponse(template.render(context,request))
