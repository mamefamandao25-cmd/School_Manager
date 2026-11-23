from django.core.exceptions import ValidationError
from django.test import TestCase

from .models import Grade, Student, Subject, Teacher


class StudentSearchTests(TestCase):
    def setUp(self):
        Student.objects.create(first_name='Mame Fama', last_name='Ndao', email='mame@example.com', classe='L1', active=True)
        Student.objects.create(first_name='Moustapha', last_name='Ndiaye', email='moustapha@example.com', classe='L2', active=False)
        Student.objects.create(first_name='Fatou Binetou', last_name='Ladiane', email='fatou@example.com', classe='L1', active=False)

    def test_search_by_last_name_filters_results(self):
        response = self.client.get('/students/?q=ndi')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Moustapha')
        self.assertNotContains(response, 'Mame Fama')
        self.assertNotContains(response, 'Fatou Binetou')

    def test_search_by_first_name_filters_results(self):
        response = self.client.get('/students/?q=fatou')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Fatou Binetou')
        self.assertNotContains(response, 'Mame Fama')


class StudentGradeTests(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            first_name='Aminata',
            last_name='Faye',
            email='aminata@example.com',
            classe='L1',
        )
        self.subject = Subject.objects.create(name='Mathématiques')

    def test_detail_displays_grade_and_average(self):
        Grade.objects.create(student=self.student, subject=self.subject, title='Devoir', score=16)

        response = self.client.get(f'/students/{self.student.pk}/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mathématiques')
        self.assertContains(response, '16.00/20')

    def test_grade_is_limited_to_twenty(self):
        grade = Grade(student=self.student, subject=self.subject, score=21)

        with self.assertRaises(ValidationError):
            grade.full_clean()

    def test_teacher_can_be_associated_with_subject(self):
        teacher = Teacher.objects.create(
            first_name='Awa',
            last_name='Diop',
            email='awa@example.com',
        )
        teacher.subjects.add(self.subject)

        self.assertEqual(list(teacher.subjects.all()), [self.subject])
