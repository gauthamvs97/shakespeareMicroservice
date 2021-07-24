from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .python_Programs.analyse_Shake import count_Shakespeare
from .python_Programs.handle_upload import handle_uploaded_file


def uploadfile(request):
    if request.method == 'POST':
        print("Checking")
        print(request)
        print(request.FILES)
        the_file = request.FILES['myfile']
        file_path = handle_uploaded_file(the_file)
        response = count_Shakespeare(file_path)
        return JsonResponse(response)


def index(request):
    return render(request, 'shakespeare/main_page.html', {})
