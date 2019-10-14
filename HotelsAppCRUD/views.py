from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    def create_customer(request):
        if request.method == "POST":
            form=CustomerForm(request.POST)
            if form.is_valid():
               customer_item = form.save(commit=False)
               customer_item.save()
               return redirect('/Customers/'+ str(customer_item.id)+ '/')
        else:
            form = CustomerForm()
            context = {'form': form}
            return render(request, template_name, context)


class CustomerDetail(DetailView):
    template_name = "HotelsAppCRUD/Customers/customer_detail.html"
    pk_url_kwarg = 'id'
    model = Customer
    def get_context_data(self, **kwargs):
        context = super(CustomerDetail, self).get_context_data(**kwargs)
        return context
    def post_detail(request, pk):
        post = get_object_or_404(Customer, pk=pk)
        context = {'post': post}
        return render(request, template_name, context)


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
        context = {'form': form}
        return render(request, template_name, context)


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
            context =  {'form': form}
            return render(request, template_name, context)


class HotelDetail(DetailView):
    template_name = "HotelsAppCRUD/Hotels/hotel_detail.html"
    model = Hotel
    pk_url_kwarg = 'id'
    def get_context_data(self, **kwargs):
        context = super(HotelDetail, self).get_context_data(**kwargs)
        return context
    def post_detail(request, pk):
        post = get_object_or_404(Hotel, pk=pk)
        context = {'post': post}
        return render(request, template_name, context)


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
        context = {'form': form}
        return render(request, template_name, context)


class HotelDelete(DeleteView):
    model = Hotel
    success_url = reverse_lazy('Hotels/index.html')


class RoomCreate(CreateView):
    template_name = "HotelsAppCRUD/Rooms/room_create.html"
    def create_room(request):
        if request.method == "POST":
            form=RoomForm(request.POST)
            if form.is_valid():
               room_item = form.save(commit=False)
               room_item.save()
               return redirect('/Rooms/'+ str(room_item.id)+ '/')
        else:
            form = RoomForm()
            context = {'form': form}
            return render(request, template_name, context)


class RoomDetail(DetailView):
    template_name = "HotelsAppCRUD/Rooms/room_detail.html"
    model = Room
    def get_context_data(self, **kwargs):
        context = super(RoomDetail, self).get_context_data(**kwargs)
        return context
    def post_detail(request, pk):
        post = get_object_or_404(Room, pk=pk)
        context = {'post': post}
        return render(request, template_name, context)

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
        context = {'form': form}
        return render(request, template_name, context)


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
            context = {'form': form}
            return render(request, template_name, context)


class RoomReservationDetail(DetailView):
    template_name = "HotelsAppCRUD/Reservation/room_reservation_detail.html"
    model = RoomReservation
    def get_context_data(self, **kwargs):
        context = super(RoomReservationDetail, self).get_context_data(**kwargs)
        return context
    def post_detail(request, pk):
        post = get_object_or_404(RoomReservation, pk=pk)
        context = {'post': post}
        return render(request, template_name, context)


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
        context = {'form': form}
        return render(request, 'HotelsAppCRUD/Reservation/index.html', context)


class RoomReservationDelete(DeleteView):
    model = RoomReservation
    success_url = reverse_lazy('Reservation/index.html')


class RoomServiceCreate(CreateView):
    template_name = "HotelsAppCRUD/Hotels/hotel_create.html"
    def create_service(request):
        if request.method == "POST":
            form = RoomServiceForm(request.POST)
            if form.is_valid():
               service_item = form.save(commit=False)
               service_item.save()
               return redirect('/Hotels/'+ str(service_item.id)+ '/')
        else:
            form = RoomServiceForm()
            context = {'form': form}
            return render(request, template_name, context)


class RoomServiceDetail(DetailView):
    template_name = "HotelsAppCRUD/Service/room_service_detail.html"
    model = RoomService
    def get_context_data(self, **kwargs):
        context = super(RoomServiceDetail, self).get_context_data(**kwargs)
        return context
    def post_detail(request, pk):
        post = get_object_or_404(RoomService, pk=pk)
        context = {'post': post}
        return render(request, template_name, context)


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
        context = {'form': form}
        return render(request, template_name, context)


class RoomServiceDelete(DeleteView):
    model = RoomReservation
    success_url = reverse_lazy('Service/index.html')


class RoomChargesCreate(CreateView):
    template_name = "HotelsAppCRUD/Charge/room_charge_create.html"
    def create_charges(request):
        if request.method == "POST":
            form=RoomChargesForm(request.POST)
            if form.is_valid():
               charge_item = form.save(commit=False)
               charge_item.save()
               return redirect('/Hotels/'+ str(charge_item.id)+ '/')
        else:
            form = RoomChargesForm()
            context = {'form': form}
            return render(request, template_name, context)

class RoomChargesDetail(DetailView):
    template_name = "HotelsAppCRUD/Charge/room_charge_detail.html"
    model = RoomCharges
    def get_context_data(self, **kwargs):
        context = super(RoomChargesDetail, self).get_context_data(**kwargs)
        return context
    def post_detail(request, pk):
        post = get_object_or_404(RoomCharges, pk=pk)
        context = {'post': post}
        return render(request, template_name, context)


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
        context = {'form': form}
        return render(request, 'HotelsAppCRUD/Charge/index.html', context)


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
            context = {'form': form}
            return render(request, template_name, context)


class RoomBillingDetail(DetailView):
    template_name = "HotelsAppCRUD/Billing/room_billing_detail.html"
    model = RoomBilling
    def get_context_data(self, **kwargs):
        context = super(RoomBillingDetail, self).get_context_data(**kwargs)
        return context
    def post_detail(request, pk):
        post = get_object_or_404(RoomBilling, pk=pk)
        context = {'post': post}
        return render(request, template_name, context)


class RoomBillingUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Billing/room_billing_update.html"
    form_class = RoomBillingForm
    def update_billing(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form =RoomBillingForm(request.POST or None, instance=item)
        if form.is_valid():
            billing_item = form.save(commit=False)
            billing_item.save()
            return redirect('/Hotels/' + str(billing_item.id) + '/')
        context = {'form': form}
        return render(request, template_name, context)


class RoomBillingDelete(DeleteView):
    model = RoomBilling
    success_url = reverse_lazy('Billing/index.html')
