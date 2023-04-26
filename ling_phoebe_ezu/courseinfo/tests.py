from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Semester, Section, Course, Instructor, Student, Registration, Period, Year


class EZUTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='test@email.com',
            password='{iSchoolUI}'
        )

        self.student = Student.objects.create(
            first_name='stu_f',
            last_name='stu_l',
            disambiguator='stu'
        )

        self.instructor = Instructor.objects.create(
            first_name='ins_f',
            last_name='ins_l',
            disambiguator='ins'
        )

        self.year = Year.objects.create(
            year=2023
        )

        self.course = Course.objects.create(
            course_number='198',
            course_name='course_test'
        )

        self.period = Period.objects.create(
            period_sequence=1,
            period_name='Fall'
        )

        self.semester = Semester.objects.create(
            year=self.year,
            period=self.period
        )

        self.section = Section.objects.create(
            section_name='test_sec',
            semester=self.semester,
            course=self.course,
            instructor=self.instructor
        )

        self.registration = Registration.objects.create(
            student=self.student,
            section=self.section
        )
    ''' 
    # Controller Assignment

    def test_course_detail_view(self):
        response = self.client.get('/course/1')
        no_response = self.client.get('/course/10000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'course_test')
        self.assertTemplateUsed(response, 'courseinfo/course_detail.html')

    def test_instructor_detail_view(self):
        response = self.client.get('/instructor/1')
        no_response = self.client.get('/instructor/10000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'ins_f')
        self.assertTemplateUsed(response, 'courseinfo/instructor_detail.html')

    def test_registration_detail_view(self):
        response = self.client.get('/registration/1')
        no_response = self.client.get('/registration/10000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'stu_f')
        self.assertTemplateUsed(response, 'courseinfo/registration_detail.html')

    def test_section_detail_view(self):
        response = self.client.get('/section/1')
        no_response = self.client.get('/section/10000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test_sec')
        self.assertTemplateUsed(response, 'courseinfo/section_detail.html')

    def test_semester_detail_view(self):
        response = self.client.get('/semester/1')
        no_response = self.client.get('/semester/10000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Fall')
        self.assertTemplateUsed(response, 'courseinfo/semester_detail.html')

    def test_student_detail_view(self):
        response = self.client.get('/student/1')
        no_response = self.client.get('/student/10000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'stu_f')
        self.assertTemplateUsed(response, 'courseinfo/student_detail.html')
    '''

# Link Pages Assignment

    def test_course_list_link(self):
        response = self.client.get(reverse('courseinfo_course_list_urlpattern'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Course List')
        self.assertTemplateUsed(response, 'courseinfo/course_list.html')

    def test_instructor_list_link(self):
        response = self.client.get(reverse('courseinfo_instructor_list_urlpattern'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Instructor List')
        self.assertTemplateUsed(response, 'courseinfo/instructor_list.html')

    def test_registration_list_link(self):
        response = self.client.get(reverse('courseinfo_registration_list_urlpattern'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Registration List')
        self.assertTemplateUsed(response, 'courseinfo/registration_list.html')

    def test_section_list_link(self):
        response = self.client.get(reverse('courseinfo_section_list_urlpattern'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Section List')
        self.assertTemplateUsed(response, 'courseinfo/section_list.html')

    def test_semester_list_link(self):
        response = self.client.get(reverse('courseinfo_semester_list_urlpattern'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Semester List')
        self.assertTemplateUsed(response, 'courseinfo/semester_list.html')

    def test_student_list_link(self):
        response = self.client.get(reverse('courseinfo_student_list_urlpattern'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student List')
        self.assertTemplateUsed(response, 'courseinfo/student_list.html')
