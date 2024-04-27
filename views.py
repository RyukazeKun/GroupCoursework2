from django.shortcuts import render
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    return render(request, 'userLogin.html')

def register(request):              # function for create user account page
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('userLogin.html')
    else:
        form = UserRegisterForm()
    return render(request, 'CreateUserAccount.html', {'form': form})
