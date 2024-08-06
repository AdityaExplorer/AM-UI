from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Create_Acc
from .models import UserData
from .forms import UserDataForm
from django.db import IntegrityError
from django.core.files.storage import FileSystemStorage
# Create your views here.


def Home(request):
    return render(request,template_name="home.html")


def Create_Accs(request):
    if request.method == "GET":
        return render(request, "Create_Acc.html")
    else:
        name = request.POST.get('nm')
        email_id = request.POST.get('em')
        password = request.POST.get('ps')
        try:
            obj = Create_Acc(Name=name, Email_id=email_id, Password=password)
            obj.save()
            return render(request, 'Create_Acc.html', {'Result': 'Account Created Successfully'})
        except IntegrityError:
            return render(request, 'Create_Acc.html', {'Result': 'Email ID already exists.'})
        except Exception as ex:
            return render(request, 'Create_Acc.html', {'Result': f'An error occurred: {ex}'})


def add_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        aadhaar = request.POST.get('aadhaar')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        document_f = request.FILES['photo']  
        
        fs = FileSystemStorage()
        filename = fs.save(document_f.name, document_f)
        document_path = fs.url(filename)
        
        # Save to the database
        user_data = UserData(
            name=name,
            email=email,
            aadhaar=aadhaar,
            mobile=mobile,
            address=address,
            document_path=document_path,
            doct_file_name=filename
        )
        user_data.save()
        
        return redirect('view_data')  # Redirect to the view_data page after saving
    return render(request, 'add_data.html')

def view_data(request):
    data = UserData.objects.all()
    return render(request, 'view_data.html', {'data': data})



@user_passes_test(lambda u: u.is_staff)
def edit_data(request, user_id):
    user = get_object_or_404(UserData, id=user_id)
    if request.method == 'POST':
        form = UserDataForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('view_data')
    else:
        form = UserDataForm(instance=user)
    return render(request, 'edit_data.html', {'form': form})


# Search
def view_data(request):
    query = request.GET.get('search')
    if query:
        data = UserData.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(aadhaar__icontains=query) |
            Q(mobile__icontains=query)
        )
    else:
        data = UserData.objects.all()
    return render(request, 'view_data.html', {'data': data, 'query': query})
