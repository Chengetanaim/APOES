from django.db import models
from django.conf import settings

EXAM_TYPES = (
    ("Multiple Choice", "Multiple Choice"),
    # ("Structured", "Structured")
)


class Exam(models.Model):
    name = models.CharField(max_length=100)
    exam_type = models.CharField(max_length=100, choices=EXAM_TYPES)
    start_time = models.CharField(max_length=100)
    endtime = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.TextField()
    answer1 = models.TextField()
    answer2 = models.TextField()
    answer3 = models.TextField()
    answer4 = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "Multiple Choice Exam Questions"


class StructuredQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "Structured Exam Questions"

class Alert(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " - " + str(self.date)


# class UserAnswer(models.Model):
#     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     answers = models.CharField()
#
#
class Answer(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return f"{self.exam} - {self.question} - {self.answer}"

    class Meta:
        verbose_name_plural = "Multiple Choice Answers"


class ExamDuration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    time_started = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.time_started)


class Disqualified(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Disqualified'

    def __str__(self):
        return self.user.username

