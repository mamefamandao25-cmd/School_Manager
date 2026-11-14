from django.test import TestCase

from students.models import Student, Teacher


class AccueilPageTests(TestCase):
    def test_homepage_displays_welcome_content(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'students/home.html')
        self.assertContains(response, 'School Manager')
        self.assertContains(response, 'Étudiants inscrits')

    def test_dashboard_displays_database_counts(self):
        Student.objects.create(first_name='Awa', last_name='Diop', classe='L1', active=True)
        Student.objects.create(first_name='Moussa', last_name='Fall', classe='L2', active=False)
        Teacher.objects.create(first_name='Fatou', last_name='Sow', subject='Mathématiques')

        response = self.client.get('/')

        self.assertEqual(response.context['student_count'], Student.objects.count())
        self.assertEqual(response.context['active_student_count'], Student.objects.filter(active=True).count())
        self.assertEqual(response.context['class_count'], Student.objects.values('classe').distinct().count())
        self.assertEqual(response.context['teacher_count'], Teacher.objects.count())
