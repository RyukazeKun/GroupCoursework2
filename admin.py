from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.urls import reverse
from django.utils.html import format_html
from .models import Device, Order, Customer, Equipment, Admin

@admin.register(Admin,Customer,Order,Device,Equipment)
class ViewAdmin(ImportExportModelAdmin):
    pass


class AdminDevices(admin.ModelAdmin):  # Device model it creates a database in the Admin Panel
    list_display = ('deviceSerialNo', 'deviceName', 'deviceType')


class AdminCustomers(admin.ModelAdmin):  # Device model it creates a database in the Admin Panel
    list_display = ('customerID', 'customerUsername', 'customer')

# Device model it creates a database in the Admin Panel, you also can download the report for equipments
class AdminEquipment(admin.ModelAdmin):
    list_display = ('equipmentID', 'equipmentName', 'equipmentType', 'quantity', 'status', 'bookingHistory', 'location',
                    'inventory_report_link')

    def inventory_report_link(self, obj):   # It allows the admin users to generate the report in equipments
        url = reverse('studentapp:generate_pdf_report')
        return format_html('<a href="{}">Download Inventory Report</a>', url)

    inventory_report_link.short_description = 'Inventory Report'


class AdminBoss(admin.ModelAdmin):  # Information about the admin and the username/password
    list_display = ('adminID', 'adminUsername', 'adminFirstName')


admin.site.register(Device, AdminDevices)
admin.site.register(Order, )
admin.site.register(Customer, AdminCustomers)
admin.site.register(Equipment, AdminEquipment)
admin.site.register(Admin, AdminBoss)
