from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main.html')

def createMemo(request):
    # memo_content = request.GET['memoContent']
    memo_content = request.POST['memoContent']

    return HttpResponse('createMemo : ' + memo_content)