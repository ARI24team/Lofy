from django.db import models
from accounts.models import User

# ─── Django Field Common Arguments Cheat Sheet ───
#
# max_length       : Max allowed characters (required for CharField, etc.)
# null             : True stores NULL in DB (database-level)
# blank            : True allows form field to be empty (validation-level)
# default          : Sets a default value if none is given
# unique           : Ensures all values in this field are unique
# choices          : Limits valid values to predefined options (list of tuples)
# db_index         : Adds an index in DB for faster search
# verbose_name     : Human-readable name for field (used in admin, forms, etc.)
# help_text        : Extra text shown in forms (tooltips, admin)
# editable         : If False, field won’t show up in admin or modelforms
# auto_now         : Updates field to now() every time the object is saved (used with DateTimeField)
# auto_now_add     : Sets the field to now() when object is first created
# primary_key      : If True, this field becomes the primary key of the model
# validators       : List of custom validation functions
# upload_to        : Directory to upload files (for FileField/ImageField)
# related_name     : Name to access reverse relation (e.g., user.todos.all())
# on_delete        : Behavior for FK when related object is deleted (CASCADE, SET_NULL, etc.)
# choices          : Tuple list of allowed values: [(value, display), ...]
