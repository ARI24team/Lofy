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


# ─────────────────────────────────────────────────────────────
# 📘 Django Model Fields Cheat Sheet
# Drop this at the top of your models.py for quick reference
# ─────────────────────────────────────────────────────────────


# ─── FIELD TYPES ─────────────────────────────────────────────

# CharField(max_length=N)                 # Short text, must set max_length
# TextField()                             # Long text (no max_length needed)
# IntegerField()                          # Whole numbers (also: PositiveIntegerField, BigIntegerField, SmallIntegerField)
# FloatField()                            # Decimal numbers (less precise than DecimalField)
# DecimalField(max_digits, decimal_places)  # Precise decimals (e.g. for prices)

# BooleanField()                          # True / False
# NullBooleanField()                      # True / False / None (deprecated, use BooleanField(null=True))

# DateField()                             # Date only (yyyy-mm-dd)
# TimeField()                             # Time only (hh:mm[:ss])
# DateTimeField()                         # Date + time
# DurationField()                         # Time delta (e.g. for measuring durations)

# EmailField()                            # Validates email format
# URLField()                              # Validates URL format
# SlugField()                             # Short labels for URLs (like blog titles)
# FileField(upload_to='path/')            # File uploads
# ImageField(upload_to='path/')           # Requires Pillow

# UUIDField()                             # Universally Unique ID
# JSONField()                             # Stores structured data as JSON

# ─── RELATIONSHIP FIELDS ────────────────

# ForeignKey(OtherModel, on_delete=models.CASCADE)
# ManyToManyField(OtherModel)
# OneToOneField(OtherModel, on_delete=models.CASCADE)

# on_delete options:
#   - CASCADE: delete related objects too
#   - PROTECT: raise error if referenced
#   - SET_NULL: set to NULL if related object deleted (requires null=True)
#   - SET_DEFAULT: set to default value
#   - DO_NOTHING: leave as-is (can cause integrity errors)

# ─────────────────────────────────────────────────────────────
# 🧠 Pro Tips:
# - Use auto_now_add for creation timestamps, auto_now for updates
# - Use related_name to avoid clashes and improve readability in reverse lookups
# - Choices = [('draft', 'Draft'), ('pub', 'Published')], etc.
# - Keep phone numbers and such as CharField (clean & format in logic)

# 🚀 Ready to code like a pro! Now back to work, king.
# ─────────────────────────────────────────────────────────────

VISIBILITY_CHOICES = [
    ('PUBLIC', 'Everyone'),
    ('FRIENDS', 'Only friends'),
    ('PRIVATE', 'Only me')
]

POST_TYPE = [
    ('TEXT', 'Text'),
    ('IMAGE', 'Image'),
    ('CAROUSEL', 'carousel'),
    ('REEL', 'Reel'),
    ('VIDEO', 'Video')
]
class Post(models.Model):
        #Generel post info
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    caption = models.TextField(null=True, blank=True)
    media = models.FileField(upload_to='post_media/', null=True, blank=True)
    song = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    post_type = models.CharField(max_length=15, choices=POST_TYPE, default='TEXT')

        #User interaction
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    shares_count = models.PositiveIntegerField(default=0)
    saves_count = models.PositiveIntegerField(default=0)

        # Meta and controle
    tagged_users = models.ManyToManyField(User, related_name='posts_taged_in', blank=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='PUBLIC')
    is_archived = models.BooleanField(default=False)
    is_reported = models.BooleanField(default=False)

        # Timestamps
    date_published = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.publisher.username}'s post at {self.date_published}"
    

class Comment(models.Model):
    # The user who wrote the comment
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    
    # The post this comment belongs to
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    # The actual text content of the comment
    content = models.TextField()

    # Parent comment if this is a reply; null if it's a top-level comment
    # Replies can be accessed using `comment.replies.all()`
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='replies'
    )

    # Total number of likes this comment has received
    likes_count = models.PositiveSmallIntegerField(default=0)

    # Total number of replies to this comment
    replies_count = models.PositiveSmallIntegerField(default=0)

    # Indicates whether the comment was edited after publishing
    edited = models.BooleanField(default=False)

    # Timestamp for when the comment was created
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.publisher.username}: {self.content[:30]}"

