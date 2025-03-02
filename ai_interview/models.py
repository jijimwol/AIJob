# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# class InterviewPractice(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # ✅ Add this field

#     domain = models.CharField(max_length=100)
#     job_description = models.TextField()
#     question = models.TextField()
#     user_answer = models.TextField(blank=True, null=True)
#     feedback = models.TextField(blank=True, null=True)
#     suggested_answer = models.TextField(blank=True, null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.domain} - {self.question[:50]}"
# class PersonalityAnalysis(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     openness = models.IntegerField()
#     conscientiousness = models.IntegerField()
#     extraversion = models.IntegerField()
#     agreeableness = models.IntegerField()
#     neuroticism = models.IntegerField()


from django.db import models
from django.contrib.auth.models import User

# ✅ Job Model for Storing Predefined Job Descriptions
class Job(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    industry = models.CharField(max_length=255, blank=True, null=True)  # Optional

    def __str__(self):
        return self.title

# ✅ Interview Practice Model
class InterviewPractice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)  # Link job descriptions
    domain = models.CharField(max_length=100)
    job_description = models.TextField()
    question = models.TextField()
    user_answer = models.TextField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    suggested_answer = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.domain} - {self.question[:50]}"

# ✅ Personality Analysis Model
class PersonalityAnalysis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    openness = models.IntegerField()
    conscientiousness = models.IntegerField()
    extraversion = models.IntegerField()
    agreeableness = models.IntegerField()
    neuroticism = models.IntegerField()
