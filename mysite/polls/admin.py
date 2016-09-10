from django.contrib import admin
from django.utils import timezone
from polls.models import Question
# create a Question instance with pub_date 30 days in the future
# Register your models here.
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
# was it published recently?
future_question.was_published_recently()
