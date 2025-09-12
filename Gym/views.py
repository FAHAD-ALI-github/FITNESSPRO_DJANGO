from django.shortcuts import render, redirect
from .models import *
import datetime


# Hardcoded admin credentials
ADMIN_CREDENTIALS = {
    'username': 'admin',
    'password': 'admin123',
    'first_name': 'Admin',
    'last_name': 'User',
    'email': 'admin@gym.com',
    'phone_number': '1234567890'
}


def home(request):
    return render(request, "home.html")

def contact_us(request):
    return render(request, 'contact.html')

def new_registration(request):
    data={}
    if request.method=="POST":
        first_name=request.POST.get("firstname")
        last_name=request.POST.get("lastname")
        dob=request.POST.get("dob")
        phone_number=request.POST.get("phone_number")
        height=request.POST.get("height")
        weight=request.POST.get("weight")
        username=request.POST.get("username")
        password=request.POST.get("password")
        c_password=request.POST.get("c_password")
        muscle_strength=request.POST.get("muscle_strength")
        gym_split=request.POST.get("gym_split")
        gender=request.POST.get("gender")
        address=request.POST.get("address")
        email=request.POST.get("email")
        error=""
        msg=""
        result=Gym_user.get_username_authen(username)
        if len(first_name)<2 or len(last_name)<2 or len(dob)<2 or len(phone_number)<2 or len(username)<2:
            error="No field should empty"
        elif len(password) < 5:
            error="Password length should be atleast 5 characters"
        elif password!=c_password:
            error=("Both passwords should match ")
        elif result:
            error="Username already exists"
        else:
            user=Gym_user()
            user.first_name=first_name.strip()
            user.last_name=last_name.strip()
            user.dob=dob.strip()
            user.phone_number=int(phone_number)
            user.weight=weight
            user.height=height
            user.username=username.strip()
            user.password=password
            user.password=c_password
            if address=="township":
                user.address_id=1
            elif address=="johr town":
                user.address_id=2
            elif address=="model town":
                user.address_id=3
            elif address=="faisal town":
                user.address_id=4
            elif address=="green town":
                user.address_id=5
            elif address=="iqbal town":
                user.address_id=6
            elif address=="garden town":
                user.address_id=7
            if gender=="male":
                user.gender_id=1
            else:
                user.gender_id=2
            if gym_split=="5_day_split":
                user.gym_split_id=1
            elif gym_split=="3_day_split":
                user.gym_split_id=2
            if muscle_strength=="beginner":
                user.muscle_strength_id=1
            elif muscle_strength=="intermediate":
                user.muscle_strength_id=2
            elif muscle_strength=="advanced":
                user.muscle_strength_id=3
            user.email=email
            user.save()
            msg="You're Successfully Registered!"
        data["first_name"]=first_name
        data["last_name"]=last_name
        data["dob"]=dob
        data["phone_number"]=phone_number
        data["weight"]=weight
        data["height"]=height
        data["email"]=email
        data["error"]=error
        data["msg"]=msg
        data["username"]=username
        data["password"]=password
        
    return render(request, 'new_registration.html', data)


def login(request):
    data={}
    if request.method=="POST":
        U_name=request.POST.get("u_username")
        passw=request.POST.get("u_password")
        user_data=Gym_user.get_user_by_username(U_name)
        
        today = datetime.datetime.now()
        data['today']=today.strftime("%A")
        error=""
        if user_data:
            if user_data.password==passw:
                height=user_data.height
                weight=user_data.weight
                a=weight/((height/100)**2)
                bmi=round(a,2)
                data['bmi']=bmi
                if bmi < 18.5 :
                    category = "Underweight"
                    data['bmi_status'] = category
                elif bmi < 25 :
                    category = "Normal weight"
                    data['bmi_status'] = category

                elif bmi < 30 :
                    category = "Overweight"
                    data['bmi_status'] = category
                else:
                    category = "Obese"
                data['bmi_status'] = category
                data["user"]=user_data
                return render(request,"profile_page.html", data)
            else:
                error="Password is Incorrect !"
                data["error"] = error
                return render(request, 'login_page.html', data)
        else:
            error="Incorrect Username or password !"
            data["error"] = error
            return render(request, 'login_page.html', data)
    else:
        return render(request, 'login_page.html')



def all_members(request):
    members=Gym_user.get_all_users(self=any)
    all_users_data={}
    all_users_data['users']=members
    return render(request, 'all_members.html',all_users_data)

def attendance(request):
    ids=[]
    if request.method=="GET":
        return render(request, 'attendance.html')
    else:
        ids.append(request.POST.get("1"))
        ids.append(request.POST.get("2"))
        ids.append(request.POST.get("3"))
        ids.append(request.POST.get("4"))
        ids.append(request.POST.get("5"))
        
        for i in range(5):
            try:
                user = Gym_user.get_user_by_id(ids[i])
                user.no_of_days += 1 
                user.save()
            except Gym_user.DoesNotExist:            
                continue
        data={}
        data['msg']="Successfully updated the attendance!"
        return render(request, 'attendance.html', data)    



def admin_portal(request):
    # Check if admin is logged in via session
    if 'admin_logged_in' not in request.session:
        return redirect('/admin_login')
    
    # Pass hardcoded admin data to template
    admin_data = ADMIN_CREDENTIALS.copy()
    return render(request, 'admin_portal.html', {'admin': admin_data})

def change_admin_password(request):   
    global ADMIN_CREDENTIALS
    data={}
    msg=""
    
    # Check if admin is logged in
    if 'admin_logged_in' not in request.session:
        return redirect('/admin_login')
    
    if request.method=="GET":
        # Pass current admin data to template
        data["admin"] = ADMIN_CREDENTIALS.copy()
        return render(request, 'change_admin_password.html', data)
    
    if request.method=="POST":
        new_password = request.POST.get("n_pass")
        # Update the hardcoded password
        ADMIN_CREDENTIALS['password'] = new_password
        msg = "Password Has Changed Successfully!"
        data["msg"] = msg
        data["admin"] = ADMIN_CREDENTIALS.copy()
        return render(request, 'change_admin_password.html', data)


def change_user_password(request):
    data={}
    msg=""  
    id_= request.GET.get("u_id")
    if request.method=="GET":
        user=Gym_user.objects.get(pk=id_)    
        data["user"]=user
        return render(request, 'change_user_password.html', data)
    if request.method=="POST":
        user_id=request.POST.get("user_id")
        n_password=request.POST.get("n_pass")
        user_data = Gym_user.objects.get(id=user_id)
        user_data.password=n_password
        user_data.save()
        msg="Password Has Changed Successfully!"
        data["msg"] = msg
        return render(request, 'change_user_password.html', data)


def admin_login(request):
    data={}
    if request.method=="POST":
        username = request.POST.get("a_username")
        password = request.POST.get("a_password")
        error = ""
        
        # Check against hardcoded credentials
        if username == ADMIN_CREDENTIALS['username'] and password == ADMIN_CREDENTIALS['password']:
            # Set session to mark admin as logged in
            request.session['admin_logged_in'] = True
            request.session['admin_username'] = username
            
            data["admin"] = ADMIN_CREDENTIALS.copy()
            return render(request, "admin_portal.html", data)
        else:
            error = "Incorrect Username or password!"
            data["error"] = error
            return render(request, 'admin_login.html', data)
    else:
        return render(request, 'admin_login.html', data)

def admin_logout(request):
    # Clear admin session
    if 'admin_logged_in' in request.session:
        del request.session['admin_logged_in']
    if 'admin_username' in request.session:
        del request.session['admin_username']
    return redirect('/')


def delete_user(request):
    user_id=request.GET.get("u_id")
    user_=Gym_user.objects.get(id=user_id)
    user_.delete()
    return redirect("/all_members")

def delete_profbyuser(request):
    user_id=request.GET.get("u_id")
    user_=Gym_user.objects.get(id=user_id)
    user_.delete()
    return redirect("/")


def diet_plan(request):
    return render(request, 'diet_plan.html')


def workout_plan(request):
    id_ = request.GET.get("pid")
    user = Gym_user.get_user_by_id(int(id_))
    data={}
    data['user']=user
    today = datetime.datetime.now()
    data['today']=today.strftime("%A")
    return render(request, 'workout_plan.html', data)


def workout(request):
    id_ = request.GET.get("pid")
    user = Gym_user.get_user_by_id(int(id_))
    data={}
    data['user']=user
    today_ = datetime.datetime.now()
    today=today_.weekday()
    data['today']=today_.strftime("%A")
    date_time_=user.date_of_joining
    year = int(date_time_.year)
    month = int(date_time_.month)
    day = int(date_time_.day)

    date_ = datetime.datetime(year, month, day)
    joining_day = date_.strftime('%A')
    split_ = user.gym_split_id
    print(split_, type(split_), joining_day)
    splits_1 = ["chest", "back", "shoulder", "bicep_tricep", "leg", "rest", "chest", "back", "shoulder", "bicep_tricep", "leg", "rest"]
    splits_2 = ["push", "pull", "leg", "push", "pull", "leg", "push", "pull", "leg", "push", "pull", "leg"]
    if split_ == 1:
        if joining_day == 'Monday':
            exercise = splits_1[6 + today]
            data['exercise'] = exercise
        if joining_day == 'Tuesday':
            exercise = splits_1[5 + today]
            data['exercise'] = exercise
        if joining_day == 'Wednesday':
            exercise = splits_1[4 + today]
            data['exercise'] = exercise
        if joining_day == 'Thursday':
            exercise = splits_1[3 + today]
            data['exercise'] = exercise
        if joining_day == 'Friday':
            exercise = splits_1[2 + today]
            print(exercise)
            data['exercise'] = exercise
        if joining_day == 'Saturday':
            exercise = splits_1[1 + today]
            data['exercise'] = exercise
    if split_ == 2:
        if joining_day == 'Monday':
            exercise = splits_2[6 + today]
            data['exercise'] = exercise
        elif joining_day == 'Tuesday':
            exercise = splits_2[5 + today]
            data['exercise'] = exercise
        elif joining_day == 'Wednesday':
            exercise = splits_2[4 + today]
            data['exercise'] = exercise
        elif joining_day == 'Thursday':
            exercise = splits_2[3 + today]
            data['exercise'] = exercise
        elif joining_day == 'Friday':
            exercise = splits_2[2 + today]
            data['exercise'] = exercise
        elif joining_day == 'Saturday':
            exercise = splits_2[1 + today]
            data['exercise'] = exercise

    return render(request, 'workout.html', data)


def userdetails(request):
    _id_ = request.GET.get("u_id")
    singleuser = Gym_user.get_user_by_id(int(_id_))
    user_data = {}
    user_data["a_user"] = singleuser
    height=singleuser.height
    weight=singleuser.weight
    a=weight/((height/100)**2)
    bmi=round(a,2)
    user_data['bmi']=bmi
    if bmi < 18.5 :
        category = "Underweight"
        user_data['bmi_status'] = category
    elif bmi < 25 :
        category = "Normal weight"
        user_data['bmi_status'] = category

    elif bmi < 30 :
        category = "Overweight"
        user_data['bmi_status'] = category
    else:
        category = "Obese"
        user_data['bmi_status'] = category

    return render(request, 'userdetails.html', user_data)

def profilePage(request):
    id_ = request.GET.get("u_id")
    singleuser = Gym_user.get_user_by_id(int(id_))
    user_data = {}
    user_data["a_user"] = singleuser
    height=singleuser.height
    weight=singleuser.weight
    a=weight/((height/100)**2)
    bmi=round(a,2)
    user_data['bmi']=bmi
    if bmi < 18.5 :
        category = "Underweight"
        user_data['bmi_status'] = category
    elif bmi < 25 :
        category = "Normal weight"
        user_data['bmi_status'] = category

    elif bmi < 30 :
        category = "Overweight"
        user_data['bmi_status'] = category
    else:
        category = "Obese"
        user_data['bmi_status'] = category

    return render(request, 'profile_page.html', user_data)


def searchPage(request):
    query = request.POST.get("searchedMember")
    searchedMember = Gym_user.get_searched_members(query)
    if not searchedMember:
        searchedMember = Gym_user.by_lastName(query)
        if not searchedMember:
            searchedMember = Gym_user.by_id(query)
            if not searchedMember:
                searchedMember = Gym_user.by_username(query)
                if not searchedMember:
                    searchedMember = Gym_user.by_dob(query)
    data = {}
    data["members"] = searchedMember
    return render(request, 'searchPage.html', data)