# views.py
from django.shortcuts import render
from .forms import CodeForm

def index(request):
    form = CodeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        code = form.cleaned_data['code']
    else:
        code = 'Default Code'  # Provide a default value if needed

    context = {
        'code': code,
        'form': form
    }
    return render(request, 'home/index.html', context)
