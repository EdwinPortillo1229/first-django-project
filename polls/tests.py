import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    time = timezone.now() + datetime.timedelta(days=30)
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in the future.
        """
        future_question = Question(pub_date=self.time)
        self.assertIs(future_question.was_published_recently(), False)