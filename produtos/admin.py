from django.contrib import admin
from .models import *

# Register your models here.

#none login admin/:
#flaviano, senha: qwerty
admin.site.register(categoria)
admin.site.register(produto)