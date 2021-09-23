from django.contrib import admin
from .models import Subject, Point, Group, Scoresummary

admin.site.register(Scoresummary)
admin.site.register(Subject)
admin.site.register(Point)
admin.site.register(Group)
