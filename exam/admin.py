from django.contrib import admin
from .models import Alert, Exam, ExamQuestion, Answer, StructuredQuestion, ExamDuration, Disqualified


admin.site.register(Alert)
admin.site.register(Exam)
admin.site.register(ExamQuestion)
# admin.site.register(StructuredQuestion)
admin.site.register(Answer)
# admin.site.register(ExamDuration)
# admin.site.register(Disqualified)
