from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    lists = Memo.objects.all()
    data = {'lists':lists}
    return render(request, 'main.html', data)

def createMemo(request):
    # memo_content = request.GET['memoContent']
    memo_content = request.POST['memoContent']

    # DB 입력
    article = Memo(memo_text = memo_content)
    article.save()

    # return HttpResponse('createMemo : ' + memo_content)
    ## reverse + name > 리다이렉트
    return HttpResponseRedirect(reverse('index'))