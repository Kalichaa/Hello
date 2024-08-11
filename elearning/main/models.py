from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=24, unique=True)


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Certification(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE, default="none")
    certification_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class CourseComment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.course} at {self.created_at}"


class ForumPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ForumComment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.post} at {self.created_at}"