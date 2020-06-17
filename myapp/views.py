from django.shortcuts import render

from myapp import admin
from .models import CustomUser
from .forms import MailForm, MetricForm

from django.core.mail import send_mail
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils import timezone

# View to show metric
def metrics(request): 

    # Fetching User Metrics by date
    def get_user_by_date(day):
        day = int(day)
        users = CustomUser.objects.all().filter(date_joined__lte=datetime.now(tz=timezone.utc))
        if day > 0 and day < 31:
            users = CustomUser.objects.all().filter(date_joined__gte=datetime.now(tz=timezone.utc) - timedelta(days=day))
        return users
    
    # Getting the number of active user
    def get_active_user_count():
        user = []
        for usr in CustomUser.objects.all():
            if usr.is_active:
                user.append(usr)
        return len(user)
    
    # Form for filtering users by date
    user_dt = get_user_by_date(0).count
    if request.method == "POST":
        form = MetricForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data['day']
            user_dt = get_user_by_date(cd).count()
    else:
        form = MetricForm()
            
    return render(request,'admin/metric.html', {
        'user': request.user,
        'has_permission': admin.admin_site.has_permission(request),
        'users': user_dt , 'active_user': get_active_user_count(), 'form': form
        })

# View for sending mail page
def sendmail(request): 

    # get email of all existing user
    def getMail():
        mail = []
        for usr in CustomUser.objects.all():
            if usr.email:
                mail.append(usr.email)
        return mail

    # Form for sending the mail message
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail( cd['subject'], cd['content'], request.user.email, getMail(),fail_silently=False)
            messages.success(request, "message sent succesfully")
    else:
        form = MailForm()

    return render(request,'admin/sendmail.html', {
        'user': request.user,
        'has_permission': admin.admin_site.has_permission(request),
        'form': form
    })

