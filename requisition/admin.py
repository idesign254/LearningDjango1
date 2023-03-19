from django.contrib import admin
from .models import Document
from .models import School
from .models import BlogPost
from .models import Application
from .models import User


# Register your models here.
admin.site.register (Document)
admin.site.register (School)
admin.site.register(BlogPost)
admin.site.register(Application)
admin.site.register(User)
