from django.contrib import admin

from .models import About, AdministrativeBody, AdvisoryBoard, BoardOfDirector, History, ServicesAndFacilities, Message

@admin.register(About)
class AdminAbout(admin.ModelAdmin):
    pass


@admin.register(Message)
class AdminMessage(admin.ModelAdmin):
    pass


@admin.register(History)
class AdminHistory(admin.ModelAdmin):
    pass



@admin.register(BoardOfDirector)
class BoardOfDirectorAdmin(admin.ModelAdmin):
    pass


@admin.register(AdministrativeBody)
class AdminBodyAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvisoryBoard)
class AdvisoryBoardAdmin(admin.ModelAdmin):
    pass



@admin.register(ServicesAndFacilities)
class ServiceAndFacilitiesAdmin(admin.ModelAdmin):
    pass







