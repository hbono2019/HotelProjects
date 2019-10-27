from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
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


def RoomsReservationPub(request):
    data = {}
    return render(request, "HotelsAppCRUD/Reservation/index_pub.html", data)

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
            context = {'form': form}
            return render(request, template_name, context)


class CustomerList(ListView):
    template_name = "HotelsAppCRUD/Customers/customer_list.html"
    form_class = CustomerForm
    model = Customer
    context_object_name = 'customer_list'
    queryset = Customer.objects.all()
    paginate_by = 10
    ordering = ['-customer_id']


class CustomerDetail(DetailView):
    template_name = "HotelsAppCRUD/Customers/customer_detail.html"
    model = Customer


class CustomerUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Customers/customer_update.html"
    form_class = CustomerForm
    model = Customer
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
    success_url = reverse_lazy('HotelsAppCRUD:customer_index')
    template_name = 'HotelsAppCRUD/Customers/customer_delete.html'
    def confirm_delete(request, id=None):
        obj = get_object_or_404(Customer, id=id)
        if request.method == "POST":
           obj.delete()
           context = {'object': obj}
           return render(request, template_name, context)


class HotelCreate(CreateView):
    template_name = "HotelsAppCRUD/Hotels/hotel_create.html"
    form_class = HotelForm
    def create_hotel(request):
        if request.method == "POST":
            form = HotelForm(request.POST)
            if form.is_valid():
               hotel_item = form.save(commit=False)
               hotel_item.save()
               return redirect('/Hotels/'+ str(hotel_item.id)+ '/')
        else:
            form = HotelForm()
            context = {'form': form}
            return render(request, template_name, context)


class HotelList(ListView):
    template_name = "HotelsAppCRUD/Hotels/hotel_list.html"
    form_class = HotelForm
    model = Hotel
    queryset = Hotel.objects.all()
    context_object_name = 'hotel_list'
    paginate_by = 10
    ordering = ['-hotel_id']


class HotelDetail(DetailView):
    template_name = "HotelsAppCRUD/Hotels/hotel_detail.html"
    model = Hotel


class HotelUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Hotels/hotel_update.html"
    form_class = HotelForm
    model = Hotel
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
    success_url = reverse_lazy('HotelsAppCRUD:hotel_index')
    template_name = 'HotelsAppCRUD/Hotels/hotel_delete.html'
    def confirm_delete(request, id=None):
        obj = get_object_or_404(Hotel, id=id)
        if request.method == "POST":
           obj.delete()
           context = {'object': obj}
           return render(request, template_name, context)


class RoomCreate(CreateView):
    template_name = "HotelsAppCRUD/Rooms/room_create.html"
    form_class =  RoomForm
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


class RoomList(ListView):
    template_name = "HotelsAppCRUD/Rooms/room_list.html"
    form_class = RoomForm
    model = Room
    context_object_name = 'room_list'
    queryset = Room.objects.all()
    paginate_by = 10
    ordering = ['-room_id']


class RoomDetail(DetailView):
    template_name = "HotelsAppCRUD/Rooms/room_detail.html"
    model = Room


class RoomUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Rooms/room_update.html"
    form_class = RoomForm
    model = Room
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
    success_url = reverse_lazy('HotelsAppCRUD:room_index')
    template_name = 'HotelsAppCRUD/Rooms/room_delete.html'
    def confirm_delete(request, id=None):
        obj = get_object_or_404(Room, id=id)
        if request.method == "POST":
           obj.delete()
           context = {'object': obj}
           return render(request, template_name, context)


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


class RoomReservationPubCreate(CreateView):
    template_name = "HotelsAppCRUD/Reservation/room_reservation_public_create.html"
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


class RoomReservationList(ListView):
    template_name = "HotelsAppCRUD/Reservation/room_reservation_list.html"
    model = RoomReservation
    context_object_name = 'reservation_list'
    queryset = RoomReservation.objects.all()
    paginate_by = 10
    ordering = ['-reservation_id']

class RoomReservationPubList(ListView):
    template_name = "HotelsAppCRUD/Reservation/room_reservation_public_list.html"
    model = RoomReservation
    context_object_name = 'reservation_list'
    queryset = RoomReservation.objects.all()
    paginate_by = 10
    ordering = ['-reservation_id']


class RoomReservationDetail(DetailView):
    template_name = "HotelsAppCRUD/Reservation/room_reservation_detail.html"
    model = RoomReservation


class RoomReservationPubDetail(DetailView):
    template_name = "HotelsAppCRUD/Reservation/room_reservation_public_detail.html"
    model = RoomReservation


class RoomReservationUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Reservation/room_reservation_update.html"
    form_class = RoomReservationForm
    model = RoomReservation
    def update_reservation(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form = RoomReservationForm(request.POST or None, instance=item)
        if form.is_valid():
            reservation_item = form.save(commit=False)
            reservation_item.save()
            return redirect('/Hotels/' + str(reservation_item.id) + '/')
        context = {'form': form}
        return render(request, template_name, context)


class RoomReservationPubUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Reservation/room_reservation_public_update.html"
    form_class = RoomReservationForm
    model = RoomReservation
    def update_reservation(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form = RoomReservationForm(request.POST or None, instance=item)
        if form.is_valid():
            reservation_item = form.save(commit=False)
            reservation_item.save()
            return redirect('/Hotels/' + str(reservation_item.id) + '/')
        context = {'form': form}
        return render(request, template_name, context)


class RoomReservationDelete(DeleteView):
      model = RoomReservation
      success_url = reverse_lazy('HotelsAppCRUD:rooms_reservation_index')
      template_name = 'HotelsAppCRUD/Reservation/room_reservation_delete.html'
      def confirm_delete(request, id=None):
          obj = get_object_or_404(RoomReservation, id=id)
          if request.method == "POST":
             obj.delete()
             context = {'object': obj}
             return render(request, template_name, context)


class RoomServiceCreate(CreateView):
    template_name = "HotelsAppCRUD/Service/room_service_create.html"
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
            context = {'form': form}
            return render(request, template_name, context)


class RoomServiceList(ListView):
    template_name = "HotelsAppCRUD/Service/room_service_list.html"
    model = RoomReservation
    context_object_name = 'service_list'
    queryset = RoomService.objects.all()
    paginate_by = 10
    ordering = ['-service_id']


class RoomServiceDetail(DetailView):
    template_name = "HotelsAppCRUD/Service/room_service_detail.html"
    model = RoomService


class RoomServiceUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Service/room_service_update.html"
    form_class = RoomServiceForm
    model = RoomService
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
      model = RoomService
      success_url = reverse_lazy('HotelsAppCRUD:rooms_service_index')
      template_name = 'HotelsAppCRUD/Service/room_service_delete.html'
      def confirm_delete(request, id=None):
          obj = get_object_or_404(RoomService, id=id)
          if request.method == "POST":
             obj.delete()
             context = {'object': obj}
             return render(request, template_name, context)


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
            context = {'form': form}
            return render(request, template_name, context)


class RoomChargesList(ListView):
    template_name = "HotelsAppCRUD/Charge/room_charge_list.html"
    model = RoomCharges
    context_object_name = 'charges_list'
    queryset = RoomCharges.objects.all()
    paginate_by = 10
    ordering = ['-room_charge_id']


class RoomChargesDetail(DetailView):
    template_name = "HotelsAppCRUD/Charge/room_charge_detail.html"
    model = RoomCharges


class RoomChargesUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Charge/room_charge_update.html"
    form_class = RoomChargesForm
    model = RoomCharges
    def update_charges(request, id=None):
        item = get_object_or_404(Hotel, id=id)
        form = RoomChargesForm(request.POST or None, instance=item)
        if form.is_valid():
            charge_item = form.save(commit=False)
            charge_item.save()
            return redirect('/Hotels/' + str(charge_item.id) + '/')
        context = {'form': form}
        return render(request, template_name, context)


class RoomChargesDelete(DeleteView):
    model = RoomCharges
    success_url = reverse_lazy('HotelsAppCRUD:rooms_charge_index')
    template_name = 'HotelsAppCRUD/Charge/room_charge_delete.html'
    def confirm_delete(request, id=None):
        obj = get_object_or_404(RoomCharges, id=id)
        if request.method == "POST":
           obj.delete()
           context = {'object': obj}
           return render(request, template_name, context)


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


class RoomBillingList(ListView):
    template_name = "HotelsAppCRUD/Billing/room_billing_list.html"
    model = RoomBilling
    context_object_name = 'charges_list'
    queryset = RoomBilling.objects.all()
    paginate_by = 10
    ordering = ['-reservation_id']


class RoomBillingDetail(DetailView):
    template_name = "HotelsAppCRUD/Billing/room_billing_detail.html"
    model = RoomBilling


class RoomBillingUpdate(UpdateView):
    template_name = "HotelsAppCRUD/Billing/room_billing_update.html"
    form_class = RoomBillingForm
    model = RoomBilling
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
    success_url = reverse_lazy('HotelsAppCRUD:rooms_billing_index')
    template_name = 'HotelsAppCRUD/Billing/room_billing_delete.html'
    def confirm_delete(request, id=None):
        obj = get_object_or_404(RoomBilling, id=id)
        if request.method == "POST":
           obj.delete()
           context = {'object': obj}
           return render(request, template_name, context)
