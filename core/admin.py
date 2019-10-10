from django.contrib import admin
from core.models import *

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('name', 'enrollment', 'percentage_tenth', 'percentage_tenth','percentage_twelfth', 'percentage_graduation')

class SkillsAdmin(admin.ModelAdmin):
    model = Skills
class ComapnyAdmin(admin.ModelAdmin):
    model = Companies
    list_display = ('company_name','packages_range', 'tenth_criteria', 'twelfth_criteria', 'graduation_criteria')

admin.site.register(Student, StudentAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Companies, ComapnyAdmin)