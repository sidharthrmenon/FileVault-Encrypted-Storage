from django.contrib import messages, auth
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


# Create your views here.

def index(request):
    return render(request, "index.html")


def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username == "admin" and password == "admin":
            return redirect('adminhome')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'adminlogin.html')


def adminhome(request):
    return render(request, "adminhome.html")


def user_register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        user_image = request.FILES.get('user_image')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if UserLogin.objects.filter(email=email).exists() or UserLogin.objects.filter(username=username).exists():
            messages.error(request, "Email or Username already exists!")
            return redirect('user_register')

        user = UserLogin(
            name=name,
            email=email,
            gender=gender,
            phone=phone,
            address=address,
            user_image=user_image,
            username=username,
            password=password
        )
        user.save()
        messages.success(request, "Registration Successful!")
        return redirect('userlogin')
    return render(request, 'user_register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = UserLogin.objects.get(username=username)

            if user.password == password:
                request.session['is_logged_in'] = True
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return redirect('userhome')
            else:
                return render(request, 'userlogin.html', {'error': 'Invalid password'})

        except UserLogin.DoesNotExist:
            return render(request, 'userlogin.html', {'error': 'Invalid username'})
    return render(request, 'userlogin.html')


def userhome(request):
    return render(request, "userhome.html")


def user_profile(request):
    if not request.session.get('is_logged_in', False):
        return redirect('userlogin')

    user = UserLogin.objects.get(username=request.session['username'])

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.address = request.POST.get('address')
        user.gender = request.POST.get('gender')
        user.dob = request.POST.get('dob')
        user.branch = request.POST.get('branch')

        if request.FILES.get('user_image'):
            user.user_image = request.FILES['user_image']

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('user_profile')

    return render(request, 'userprofile.html', {'user': user})


def feedback(request):
    if not request.session.get('is_logged_in'):
        return redirect('userlogin')

    if request.method == "POST":
        feedback_text = request.POST.get('feedback')
        rating = request.POST.get('rating')
        try:
            user = UserLogin.objects.get(id=request.session['user_id'])
        except UserLogin.DoesNotExist:
            return redirect('userlogin')

        Feedback.objects.create(user=user, feedback=feedback_text, rating=rating)
        messages.success(request, 'Feedback submitted successfully!')
        return redirect('feedback')

    return render(request, "feedback.html")


def view_feedback(request):
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'admin_view_feedback.html', {'feedbacks': feedbacks})


def delete_feedback(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id)
    feedback.delete()
    return redirect('view_feedback')


def view_users(request):
    users = UserLogin.objects.all()
    return render(request, 'admin_view_user.html', {'users': users})



def delete_user(request, user_id):
    user = get_object_or_404(UserLogin, id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('view_users')


def upload_file(request):
    if not request.session.get('is_logged_in'):
        return redirect('userlogin')

    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')
        file_type = request.POST.get('file_type')
        description = request.POST.get('description')

        try:
            user = UserLogin.objects.get(id=request.session['user_id'])
        except UserLogin.DoesNotExist:
            return redirect('userlogin')

        if uploaded_file:
            UploadedFile.objects.create(
                user=user,
                file=uploaded_file,
                file_type=file_type,
                description=description
            )
            messages.success(request, "File uploaded successfully.")
            return redirect('upload_file')

    return render(request, 'upload_file.html')


def my_files(request):
    if not request.session.get('is_logged_in'):
        return redirect('userlogin')

    try:
        user = UserLogin.objects.get(id=request.session['user_id'])
    except UserLogin.DoesNotExist:
        return redirect('userlogin')

    files = UploadedFile.objects.filter(user=user)
    return render(request, 'my_files.html', {'files': files})


def delete_file(request, file_id):
    if not request.session.get('is_logged_in'):
        return redirect('userlogin')

    try:
        user = UserLogin.objects.get(id=request.session['user_id'])
    except UserLogin.DoesNotExist:
        return redirect('userlogin')

    file = get_object_or_404(UploadedFile, id=file_id, user=user)
    file.delete()
    return redirect('my_files')


def update_file(request, file_id):
    if not request.session.get('is_logged_in'):
        return redirect('userlogin')

    try:
        user = UserLogin.objects.get(id=request.session['user_id'])
    except UserLogin.DoesNotExist:
        return redirect('userlogin')

    file_obj = get_object_or_404(UploadedFile, id=file_id, user=user)
    if request.method == 'POST':
        file_type = request.POST.get('file_type')
        description = request.POST.get('description')
        if file_type:
            file_obj.file_type = file_type
        if description:
            file_obj.description = description
        file_obj.save()
        messages.success(request, "File updated.")
        return redirect('my_files')
    return render(request, 'update_file.html', {'file': file_obj})


def view_all_files(request):
    if not request.session.get('is_logged_in'):
        return redirect('userlogin')

    try:
        user = UserLogin.objects.get(id=request.session['user_id'])
    except UserLogin.DoesNotExist:
        return redirect('userlogin')
    files = UploadedFile.objects.exclude(user=user)
    for file in files:
        file.already_requested = DownloadRequest.objects.filter(file=file, requested_by=user).exists()

    return render(request, 'view_all_files.html', {'files': files})


def send_request(request, file_id):
    if not request.session.get('is_logged_in'):
        return redirect('userlogin')

    user = get_object_or_404(UserLogin, id=request.session['user_id'])
    file_obj = get_object_or_404(UploadedFile, id=file_id)

    if file_obj.user == user:
        messages.warning(request, "You cannot request your own file.")
        return redirect('view_all_files')

    existing = DownloadRequest.objects.filter(file=file_obj, requested_by=user).first()
    if not existing:
        DownloadRequest.objects.create(file=file_obj, requested_by=user)
        messages.success(request, "Download request sent.")

    return redirect('view_all_files')


def view_requests(request):
    if not request.session.get('is_logged_in'):
        return redirect('userlogin')

    user = get_object_or_404(UserLogin, id=request.session['user_id'])

    requests_list = DownloadRequest.objects.filter(file__user=user)
    return render(request, 'requests.html', {'requests': requests_list})


def approve_request(request, req_id):
    req = get_object_or_404(DownloadRequest, id=req_id)
    req.status = 'approved'
    req.save()
    return redirect('view_requests')


def reject_request(request, req_id):
    req = get_object_or_404(DownloadRequest, id=req_id)
    req.status = 'rejected'
    req.save()
    return redirect('view_requests')


def delete_request(request, req_id):
    req = get_object_or_404(DownloadRequest, id=req_id)
    req.delete()
    return redirect('view_requests')


def my_approved_files(request):
    if not request.session.get('is_logged_in'):
        return redirect('userlogin')

    user = get_object_or_404(UserLogin, id=request.session['user_id'])

    approved = DownloadRequest.objects.filter(requested_by=user, status='approved')
    return render(request, 'my_approved_files.html', {'approved': approved})


def admin_view_files(request):
    files = UploadedFile.objects.all().order_by('-id')
    return render(request, 'admin_view_files.html', {'files': files})


def delete_uploaded_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    file.delete()
    messages.success(request, "File deleted successfully.")
    return redirect('admin_view_files')
