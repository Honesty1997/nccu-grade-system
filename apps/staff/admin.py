from django.contrib import admin

# TODO(5): Register Teacher model to the admin, so you can 
# see a Teacher panel when you open django admin.
from .models import Professor
admin.site.register(Professor)