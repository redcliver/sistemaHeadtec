from django.shortcuts import render

# Create your views here.
def home(request):
    colabRegistrados = 23244
    colabTrabalhando = 12323
    trabRealizado = 9856
    return render(request, 'site/home.html', {'title':'Home',
                                              'colabRegistrados':colabRegistrados,
                                              'colabTrabalhando':colabTrabalhando,
                                              'trabRealizado':trabRealizado})