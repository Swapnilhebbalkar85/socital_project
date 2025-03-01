from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import mgt, date as DateModel
from . models import vendor,User
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import mgt, date as DateModel, vendor
from django.shortcuts import render, redirect
from .models import Register  
from django.contrib.auth.hashers import check_password 
from django.shortcuts import render, redirect
from .models import Register  
from django.contrib.auth.hashers import make_password 


def save_order(request):

    if request.method == "POST":
        dates = request.POST.getlist("date[]")
        vendors = request.POST.getlist("vendor[]")  # Get vendor names
        vehicle_numbers = request.POST.getlist("vehicle_number[]")
        vegetable_names = request.POST.getlist("vegetable_name[]")
        prices = request.POST.getlist("price[]")
        quantities = request.POST.getlist("quantity[]")
        totals = request.POST.getlist("total[]")

        for i in range(len(dates)):
           
            date_obj = DateModel.objects.filter(date=dates[i]).first()
            if not date_obj:
                date_obj = DateModel.objects.create(date=dates[i])

            
            try:
                vendor_obj = vendor.objects.get(name=vendors[i])
            except vendor.DoesNotExist:
                return HttpResponseRedirect("/index2/")  # Redirect if vendor not found

            
            mgt.objects.create(
                date=date_obj,
                vendor=vendor_obj,
                vehicle_number=vehicle_numbers[i],
                vegetable_name=vegetable_names[i],
                price=int(prices[i]),
                quantity=int(quantities[i]),
                total=int(totals[i])
            )

        return HttpResponseRedirect("/home/index.html")  # Redirect after saving orders

    return render(request, "index.html", {"orders": mgt.objects.all()})



def index(request):
    # Pass vendors to the index.html template for the dropdown
    vendors_list = vendor.objects.all() # Fetch all vendors
    return render(request, 'index.html', {'save_vendor': vendors_list})





def filter_orders(request):
    selected_date = request.GET.get("date")
    orders = []

    if selected_date:
        orders = mgt.objects.filter(date__date=selected_date)

    return render(request, "filter_orders.html", {"orders": orders})

def save_vendor(request):
    if request.method == "POST": 
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        vegetable_name = request.POST.get("v_vegetable_name")
        price = int(request.POST.get("v_price"))
        quantity = int(request.POST.get("v_quantity"))

        total = price * quantity

        # Save the vendor and get the generated id
        vendor_obj = vendor.objects.create(
            name=name,
            contact=contact,
            v_vegetable_name=vegetable_name,
            v_price=price,
            v_quantity=quantity,
            v_total=total
        )

        return redirect("vendors")  # Refresh the page to show updated data

    return render(request, "vendors.html", {"vendors": vendor.objects.all()})


def vendors(request):
    return render(request, "vendors.html", {"vendors": vendor.objects.all()})





def home(request):
    return render(request,"home.html")

def login2(request):
    return render (request,"login2.html")


def login2(request):
    return render(request,"login2.html")

def registration(request):
    return render(request,"registration.html")


def dashboard(request):
    orders = mgt.objects.all()
    vendors = vendor.objects.all()  

    total_orders = orders.count()
    total_sales = sum(order.total for order in orders)  # Total Sales from Orders
    total_vendor_amount = sum(vendor.v_total for vendor in vendors)  # Total Vendor Amount
    balance = total_sales - total_vendor_amount  # Calculate Balance

    return render(request, "dashboard.html", {
        "orders": orders,
        "vendors": vendors,
        "total_orders": total_orders,
        "total_sales": total_sales,
        "total_vendor_amount": total_vendor_amount,
        "balance": balance
    })



def delete_vendor(request, vendor_id):
    vendor_obj = get_object_or_404(vendor, id=vendor_id)
    vendor_obj.delete()
    return redirect("vendors")


def update_payment_status(request, vendor_id):
    vendor_obj = get_object_or_404(vendor, id=vendor_id)
    
    # Toggle payment status
    if vendor_obj.payment_status == "Unpaid":
        vendor_obj.payment_status = "Paid"
    else:
        vendor_obj.payment_status = "Unpaid"

    vendor_obj.save()  # Save changes in the database
    return redirect("vendors")  # Reload the page


 # For password validation

def login2(request):
    error = None  # Initialize error message
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user exists in the database
        user = Register.objects.filter(username=username).first()

        if not user:
            error = "User not registered. Please register first!"
        elif not check_password(password, user.password):  # Verify password
            error = "Invalid username or password!"
        else:
            hashed_password = make_password(password)  # Securely hash the password
           
            return redirect('home')  # Redirect if login successful

    return render(request, 'login2.html', {'error': error})



 # Secure password storage

def registration(request):
    error_message = None  

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not password or not confirm_password:
            error_message = "All fields are required!"
        elif Register.objects.filter(username=username).exists():
            error_message = "Username already taken!"
        elif password != confirm_password:
            error_message = "Passwords do not match!"
        else:
            hashed_password = make_password(password)  
            Register.objects.create(username=username, password=hashed_password)
            return redirect('login2')  
    return render(request, 'registration.html', {'error_message': error_message})
