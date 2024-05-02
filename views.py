from django.shortcuts import render
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


def reservation_history(request):
    search_query = request.GET.get('search', '')
    equipments = Equipment.objects.filter(name__icontains=search_query)

    if 'generate_pdf' in request.GET:
        return generate_pdf_report(equipments)

    return render(request, 'reservation_history.html', {'equipments': equipments})



def generate_pdf_report(request,):
    equipments = Equipment.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="equipments_report.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "Equipment Report")
    p.setFont("Helvetica", 12)
    y = 780
    p.drawString(30, y, "ID")
    p.drawString(80, y, "Name")
    p.drawString(220, y, "Type")
    p.drawString(360, y, "Quantity")
    p.drawString(460, y, "Status")
    for equipment in equipments:
        y -= 20
        if y < 100:
            p.showPage()
            y = 780
        p.drawString(30, y, str(equipment.equipmentID))
        p.drawString(80, y, equipment.equipmentName)
        p.drawString(220, y, equipment.equipmentType)
        p.drawString(360, y, str(equipment.quantity))
        p.drawString(460, y, equipment.status)
    p.showPage()
    p.save()
    return response
