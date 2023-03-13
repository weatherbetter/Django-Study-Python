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

def methodMemo(request):
    if request.method == "GET":
        return HttpResponse('GET')
    if request.method == "POST":
        return HttpResponse('POST')
    
def edit(request, idx):
    article = Memo.objects.get(id=idx)
    data = {'article' : article}
    return render(request, 'edit.html', data)

def update(request):
    idx = request.POST['id']
    memoContent = request.POST['memoContent']

    db_article = Memo.objects.get(id=idx)
    db_article.memo_text = memoContent
    db_article.save()

    return HttpResponseRedirect(reverse('index'))