from django.db import models
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 2:
            errors["name"] = "Course's name should be at least 5 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Description should be at least 5 characters"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
class Book(models.Model):
    title = models.CharField(max_length = 60)
    user = models.ForeignKey(User, related_name = 'books', on_delete = models.CASCADE )
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at= models.DateTimeField(auto_now = True)
class Author(models.Model):
    book = models.ManyToManyField(Book,related_name="authors")
    name = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Review(models.Model):
    user = models.ForeignKey(User, related_name = 'reviews', on_delete = models.CASCADE )
    rate = models.IntegerField()
    book = models.ForeignKey(Book, related_name = 'reviews', on_delete = models.CASCADE )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)