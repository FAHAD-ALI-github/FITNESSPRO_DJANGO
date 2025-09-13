
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', home),
    path('contact', contact_us),
    path('new_registration', new_registration),
    path('login', login),
    path('admin_portal', admin_portal),
    path('all_members', all_members),
    path('attendance', attendance),
    path('userdetails', userdetails),
    path('profile_page', profilePage),
    path('diet_plan', diet_plan),
    path('workout_plan', workout_plan),
    path('workout', workout),
    path('searchPage', searchPage),
    path('upload_profile_image/', views.upload_profile_image, name='upload_profile_image'),
    path('change_admin_password', change_admin_password),
    path('change_user_password', change_user_password),
    path('admin_login', admin_login),
    path("delete",delete_user),
    path("delete_user",delete_profbyuser)

]
