from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from HotelsAppCRUD.forms import *
from HotelsAppCRUD.models import *


# Create your views here.
def index(request):
    data = {}
    return render(request, "HotelsAppCRUD/index.html", data)


def Customers(request):
    data = {}
    return render(request, "HotelsAppCRUD/Customers/index.html", data)


def Hotels(request):
    data = {}
    return render(request, "HotelsAppCRUD/Hotels/index.html", data)


def Rooms(request):
    data = {}
    return render(request, "HotelsAppCRUD/Rooms/index.html", data)


def RoomsBilling(request):
    data = {}
    return render(request, "HotelsAppCRUD/Billing/index.html", data)


def RoomsCharge(request):
    data = {}
    return render(request, "HotelsAppCRUD/Charge/index.html", data)


def RoomsReservation(request):
    data = {}
    return render(request, "HotelsAppCRUD/Reservation/index.html", data)


def RoomsService(request):
    data = {}
    return render(request, "HotelsAppCRUD/Service/index.html", data)


class CustomerCreate(CreateView):
    template_name = "HotelsAppCRUD/Customers/customer_create.html"
    form_class = CustomerForm
    def create_customer(request):
        if request.method == "POST":
            form=CustomerForm(request.POST)
            if form.is_valid():
               customer_item = form.save(commit=False)
               customer_item.save()
               return redirect('/Customers/'+ str(customer_item.id)+ '/')
        else:
            form = CustomerForm()
            return render(request, 'HotelsAppCRUD/Customers/index.html', {'form': form})


class CustomerList(ListView):
    template_name = "HotelsAppCRUD/Customers/customer_create.html"
    form_class = CustomerForm
    def list_customer(request):
        if request.method == "POST":
            form=HotelForm(request.POST)
            if form.is_valid():
               hotel_item = form.save(commit=False)
               hotel_item.save()
        else:
            form = HotelForm()
            return render(request, 'HotelsAppCRUD/Customers/index.html', {'form': form})


class CustomerUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Customers/customer_update.html"
    form_class = CustomerForm
    def update_customer(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form = HotelForm(request.POST or None, instance=item)
        if form.is_valid():
           customer_item = form.save(commit=False)
           customer_item.save()
           return redirect('/Customers/' + str(customer_item.id) + '/')
        return render(request, 'HotelsAppCRUD/Customers/index.html', {'form': form})


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('Customers/index.html')


class HotelCreate(CreateView):
    template_name = "HotelsAppCRUD/Hotels/hotel_create.html"
    form_class = HotelForm
    def create_hotel(request):
        if request.method == "POST":
            form=HotelForm(request.POST)
            if form.is_valid():
               hotel_item = form.save(commit=False)
               hotel_item.save()
               return redirect('/Hotels/'+ str(hotel_item.id)+ '/')
        else:
            form = HotelForm()
            return render(request, 'HotelsAppCRUD/Hotels/index.html', {'form': form})

class HotelList(ListView):
    template_name = "HotelsAppCRUD/Hotels/hotel_create.html"
    form_class = HotelForm
    def list_hotel(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form = HotelForm(request.POST or None, instance=item)
        if form.is_valid():
           hotel_item = form.save(commit=False)
           hotel_item.save()
           return render(request, 'HotelsAppCRUD/Hotels/index.html', {'form': form})


class HotelUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Hotels/hotel_update.html"
    form_class = HotelForm
    def update_hotel(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form = HotelForm(request.POST or None, instance=item)
        if form.is_valid():
            hotel_item = form.save(commit=False)
            hotel_item.save()
            return redirect('/Hotels/' + str(hotel_item.id) + '/')
        return render(request, 'HotelsAppCRUD/Hotels/index.html', {'form': form})


class HotelDelete(DeleteView):
    model = Hotel
    success_url = reverse_lazy('Hotels/index.html')


class RoomCreate(CreateView):
    template_name = "HotelsAppCRUD/Rooms/room_create.html"
    form_class =RoomForm
    def create_room(request):
        if request.method == "POST":
            form=RoomForm(request.POST)
            if form.is_valid():
               room_item = form.save(commit=False)
               room_item.save()
               return redirect('/Rooms/'+ str(room_item.id)+ '/')
        else:
            form = RoomForm()
            return render(request, 'HotelsAppCRUD/Rooms/index.html', {'form': form})


class RoomList(ListView):
    model = Room
    fields = ['hotel_id', 'room_number', 'room_type', 'type', 'beds', 'max_occupancy', 'cost_per_night']


class RoomUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Rooms/room_update.html"
    form_class = RoomForm
    def update_room(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form = RoomForm(request.POST or None, instance=item)
        if form.is_valid():
            room_item = form.save(commit=False)
            room_item.save()
            return redirect('/Hotels/' + str(room_item.id) + '/')
        return render(request, 'HotelsAppCRUD/Rooms/index.html', {'form': form})


class RoomDelete(DeleteView):
    model = Room
    success_url = reverse_lazy('Rooms/index.html')


class RoomReservationCreate(CreateView):
    template_name = "HotelsAppCRUD/Reservation/room_reservation_create.html"
    form_class = RoomReservationForm
    def create_reservation(request):
        if request.method == "POST":
            form=RoomReservationForm(request.POST)
            if form.is_valid():
               reservation_item = form.save(commit=False)
               reservation_item.save()
               return redirect('/Hotels/'+ str(reservation_item.id)+ '/')
        else:
            form =RoomReservationForm()
            return render(request, 'HotelsAppCRUD/Reservation/index.html', {'form': form})


class RoomReservationList(ListView):
    model = RoomReservation
    fields = ['hotel_id', 'customer_id', 'room_id', 'room_number', 'from_date, to_date']


class RoomReservationUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Reservation/room_reservation_update.html"
    form_class = RoomReservationForm
    def update_reservation(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form = RoomReservationForm(request.POST or None, instance=item)
        if form.is_valid():
            reservation_item = form.save(commit=False)
            reservation_item.save()
            return redirect('/Hotels/' + str(reservation_item.id) + '/')
        return render(request, 'HotelsAppCRUD/Reservation/index.html', {'form': form})


class RoomReservationDelete(DeleteView):
    model = RoomReservation
    success_url = reverse_lazy('Reservation/index.html')


class RoomServiceCreate(CreateView):
    template_name = "HotelsAppCRUD/Hotels/hotel_create.html"
    form_class = RoomServiceForm
    def create_service(request):
        if request.method == "POST":
            form = RoomServiceForm(request.POST)
            if form.is_valid():
               service_item = form.save(commit=False)
               service_item.save()
               return redirect('/Hotels/'+ str(service_item.id)+ '/')
        else:
            form = RoomServiceForm()
            return render(request, 'HotelsAppCRUD/Service/index.html', {'form': form})


class RoomServiceList(ListView):
    model = RoomService
    fields = ['service_description', 'service_price']


class RoomServiceUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Service/room_service_update.html"
    form_class = RoomServiceForm
    def update_service(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form = RoomServiceForm(request.POST or None, instance=item)
        if form.is_valid():
            service_item = form.save(commit=False)
            service_item.save()
            return redirect('/Hotels/' + str(service_item.id) + '/')
        return render(request, 'HotelsAppCRUD/Service/index.html', {'form': form})


class RoomServiceDelete(DeleteView):
    model = RoomReservation
    success_url = reverse_lazy('Service/index.html')


class RoomChargesCreate(CreateView):
    template_name = "HotelsAppCRUD/Charge/room_charge_create.html"
    form_class = RoomChargesForm
    def create_charges(request):
        if request.method == "POST":
            form=RoomChargesForm(request.POST)
            if form.is_valid():
               charge_item = form.save(commit=False)
               charge_item.save()
               return redirect('/Hotels/'+ str(charge_item.id)+ '/')
        else:
            form = RoomChargesForm()
            return render(request, 'HotelsAppCRUD/Charge/index.html', {'form': form})

class RoomChargesList(ListView):
    model = RoomCharges
    fields = ['reservation_id', 'service_id']


class RoomChargesUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Charge/room_charge_update.html"
    form_class = RoomChargesForm
    def update_charges(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form = RoomChargesForm(request.POST or None, instance=item)
        if form.is_valid():
            charge_item = form.save(commit=False)
            charge_item.save()
            return redirect('/Hotels/' + str(charge_item.id) + '/')
        return render(request, 'HotelsAppCRUD/Charge/index.html', {'form': form})


class RoomChargesDelete(DeleteView):
    model = RoomCharges
    success_url = reverse_lazy('Charge/index.html')


class RoomBillingCreate(CreateView):
    template_name = "HotelsAppCRUD/Billing/room_billing_create.html"
    form_class = RoomBillingForm
    def create_billing(request):
        if request.method == "POST":
            form=RoomBillingForm(request.POST)
            if form.is_valid():
               billing_item = form.save(commit=False)
               billing_item.save()
               return redirect('/Hotels/'+ str(billing_item.id)+ '/')
        else:
            form = RoomBillingForm()
            return render(request, 'HotelsAppCRUD/Billing/index.html', {'form': form})


class RoomBillingList(ListView):
    model = RoomBilling
    fields = ['customer_id', 'room_charge_id', 'billing_address1', 'billing_address2', 'county', 'postal_code',
              'country', 'total_invoice']


class RoomBillingUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Billing/room_billing_update.html.html"
    form_class = RoomBillingForm
    def update_billing(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form =RoomBillingForm(request.POST or None, instance=item)
        if form.is_valid():
            billing_item = form.save(commit=False)
            billing_item.save()
            return redirect('/Hotels/' + str(billing_item.id) + '/')
        return render(request, 'HotelsAppCRUD/Billing/index.html', {'form': form})


class RoomBillingDelete(DeleteView):
    model = RoomBilling
    success_url = reverse_lazy('Billing/index.html')
