from django.db import models

# Create your models here.
class Customer(models.Model):                           # customer model
    customerID = models.AutoField(primary_key = True)
    customerUsername = models.CharField(max_length = 100, unique = True)
    customerPassword = models.CharField(max_length = 100)
    customerFirstName = models.CharField(max_length = 100)
    customerLastName = models.CharField(max_length = 100)
    customer = models.ForeignKey(Order, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.customerFirstName} {self.customerLastName}'

class Order(models.Model):                              # Order model
    orderID = models.AutoField(primary_key = True)
    orderDate = models.DateField()
    orderReturnDate = models.DateField()
    orderDeviceName = models.CharField(max_length = 100)
    orderQuantity = models.PositiveIntegerField()
    orderStatus = models.CharField(max_length = 50)
    order = models.ForeignKey(Admin, on_delete = models.CASCADE)
    def __str__(self):
        return f'{self.orderID} : {self.orderDeviceName} ({self.orderStatus})'

class Admin(models.Model):                              # Admin model
    adminID = models.AutoField(primary_key = True)
    adminUsername = models.CharField(max_length = 100, unique = True)
    adminPassword = models.CharField(max_length = 100)
    adminFirstName = models.CharField(max_length = 100)
    adminLastName = models.CharField(max_length = 100)

    def __str__(self):
        return f'{self.adminFirstName} {self.adminLastName}'

class Equipment(models.Model):                          # Equipment model
    equipmentID = models.AutoField(primary_key = True)
    equipmentName = models.CharField(max_length = 100)
    equipmentType = models.CharField(max_length = 100)
    quantity = models.PositiveIntegerField()
    audit = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100)
    bookingHistory = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    admin = models.ForeignKey(Admin, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    deviceSerialNo = models.ForeignKey(Device, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.equipmentName} ({self.equipmentType})'

class Device(models.Model):                         # Device model
    deviceSerialNo = models.AutoField(primary_key = True)
    deviceName = models.CharField(max_length = 100)
    deviceType = models.CharField(max_length = 100)
    CPU = models.CharField(max_length = 100)
    GPU = models.CharField(max_length = 100)
    RAM = models.CharField(max_length = 100)

    def __str__(self):
        return self.deviceName
