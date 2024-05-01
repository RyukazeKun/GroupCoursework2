from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import UserRegisterForm

# Create your views here.

def homePage(request):
    return render(request, 'studentapp/home.html')

def accountPage(request):
    return render(request, 'studentapp/AccountSection/account.html')

def updateAccountPage(request):
    return render(request, 'studentapp/AccountSection/update.html')

def updateConfirmPage(request):
    return render(request, 'studentapp/AccountSection/confirmed.html')

def equipmentsPage(request):
    return render(request, 'studentapp/equipment.html')

def reservationsPage(request):
    return render(request, 'studentapp/ReservationsSection/reservation.html')

def bookEquipmentPage(request):
    return render(request, 'studentapp/ReservationsSection/bookequipment.html')

def notificationsPage(request):
    return render(request, 'studentapp/notification.html')

def register(request):              # function for create user account page
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('userLogin.html')
    else:
        form = UserRegisterForm()
    return render(request, 'CreateUserAccount.html', {'form': form})