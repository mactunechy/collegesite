from django.contrib import admin
from .models import Tutorial, Registered_student ,Course
# Register your models here.

admin.site.register(Tutorial)
admin.site.register(Registered_student)
admin.site.register(Course)