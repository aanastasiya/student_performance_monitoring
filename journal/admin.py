from django.contrib import admin

from . models import Student, Subject, Grade, Professor, Department


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "patronymic", "surname", "faculty", "specialty", "group", "show_summary")
    list_filter = ("name", "group", "faculty", "specialty", "group")

    def show_summary(self, student):
        from django.db.models import Sum
        result = Grade.objects.filter(student=student).aggregate(Sum("value"))
        return result["value__sum"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("title", "assessment", "hours", "department")
    list_filter = ("title", "assessment", "department")


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("value", "subject", "student", "date")
    list_filter = ("date", "value", "subject", "student")


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("name", "patronymic", "surname", "department")
    list_filter = ("name", "surname", "department")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("title",)
