from django.test import TestCase
import pytest
from django.utils import timezone

from .models import Course

# Create your tests here.

class TestCourse(TestCase):
    
    def test_example(self):
        assert 1 == 1
    
    def test_create_course(self):
        
        course = Course.objects.create(
            name="Intensive German",
            description="It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.",
            level="A2",
            schedule="It is a long established fact that",
            duration_course="It is a long established fact that",
            quantity_persons=12,
            price="It is a long established fact that",
            initial_date=timezone.now(),
            final_date=timezone.now(),
            registration_deadline=timezone.now(),
            goal="Learn German",
        )    
        
        self.assertEqual(course.id, 1)
        self.assertEqual(course.name, "Intensive German")