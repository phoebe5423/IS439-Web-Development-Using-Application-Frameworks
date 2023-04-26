from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from courseinfo.forms import InstructorForm, SectionForm, CourseForm, SemesterForm, StudentForm, RegistrationForm
from courseinfo.models import (
    Instructor,
    Section,
    Course,
    Semester,
    Student,
    Registration
)
from courseinfo.utils import PageLinksMixin


class InstructorList(PageLinksMixin, ListView, LoginRequiredMixin, PermissionRequiredMixin):
    paginate_by = 25
    model = Instructor
    permission_required = 'courseinfo.view_instructor'


class InstructorDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Instructor
    permission_required = 'courseinfo.view_instructor'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        instructor = self.get_object()
        section_list = instructor.sections.all()
        context['section_list'] = section_list
        return context


class InstructorCreate(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = InstructorForm
    model = Instructor
    permission_required = 'courseinfo.add_instructor'


class InstructorUpdate(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = InstructorForm
    model = Instructor
    template_name = 'courseinfo/instructor_form_update.html'
    permission_required = 'courseinfo.change_instructor'


class InstructorDelete(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Instructor
    success_url = reverse_lazy('courseinfo_instructor_list_urlpattern')
    permission_required = 'courseinfo.delete_instructor'

    def get(self, request, pk):
        instructor = get_object_or_404(Instructor, pk=pk)
        sections = instructor.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/instructor_refuse_delete.html',
                {'instructor': instructor,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/instructor_confirm_delete.html',
                {'instructor': instructor}
            )


class SectionList(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Section
    permission_required = 'courseinfo.view_section'


class SectionDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Section
    permission_required = 'courseinfo.view_section'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        section = self.get_object()
        instructor = section.instructor
        semester = section.semester
        course = section.course
        registration_list = section.registrations.all()
        context['semester'] = semester
        context['course'] = course
        context['registration_list'] = registration_list
        context['instructor'] = instructor
        return context


class SectionCreate(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = SectionForm
    model = Section
    permission_required = 'courseinfo.add_section'


class SectionUpdate(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = SectionForm
    model = Section
    template_name = 'courseinfo/section_form_update.html'
    permission_required = 'courseinfo.change_section'


class SectionDelete(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Section
    success_url = reverse_lazy('courseinfo_section_list_urlpattern')
    permission_required = 'courseinfo.delete_section'

    def get(self, request, pk):
        section = get_object_or_404(Section, pk=pk)
        registrations = section.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/section_refuse_delete.html',
                {'section': section,
                 'registrations': registrations}
            )
        else:
            return render(
                request,
                'courseinfo/section_confirm_delete.html',
                {'section': section}
            )


class CourseList(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    permission_required = 'courseinfo.view_course'


class CourseDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    permission_required = 'courseinfo.view_course'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        course = self.get_object()
        section_list = course.sections.all()
        context['course'] = course
        context['section_list'] = section_list
        return context


class CourseCreate(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = CourseForm
    model = Course
    permission_required = 'courseinfo.add_course'


class CourseUpdate(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = CourseForm
    model = Course
    template_name = 'courseinfo/course_form_update.html'
    permission_required = 'courseinfo.change_course'


class CourseDelete(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Course
    success_url = reverse_lazy('courseinfo_course_list_urlpattern')
    permission_required = 'courseinfo.delete_course'

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        sections = course.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/course_refuse_delete.html',
                {'course': course,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/course_confirm_delete.html',
                {'course': course}
            )


class SemesterList(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Semester
    permission_required = 'courseinfo.view_semester'


class SemesterDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Semester
    permission_required = 'courseinfo.view_semester'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        semester = self.get_object()
        section_list = semester.sections.all()
        context['course'] = semester
        context['section_list'] = section_list
        return context


class SemesterCreate(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = SemesterForm
    model = Semester
    permission_required = 'courseinfo.add_semester'


class SemesterUpdate(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = SemesterForm
    model = Semester
    template_name = 'courseinfo/semester_form_update.html'
    permission_required = 'courseinfo.change_semester'


class SemesterDelete(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Semester
    success_url = reverse_lazy('courseinfo_semester_list_urlpattern')
    permission_required = 'courseinfo.delete_semester'

    def get(self, request, pk):
        semester = get_object_or_404(Semester, pk=pk)
        sections = semester.sections.all()
        if sections.count() > 0:
            return render(
                request,
                'courseinfo/semester_refuse_delete.html',
                {'semester': semester,
                 'sections': sections,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/semester_confirm_delete.html',
                {'semester': semester}
            )


class StudentList(PageLinksMixin, ListView, LoginRequiredMixin, PermissionRequiredMixin):
    paginate_by = 25
    model = Student
    permission_required = 'courseinfo.view_student'


class StudentDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Student
    permission_required = 'courseinfo.view_student'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        student = self.get_object()
        registration_list = student.registrations.all()
        context['student'] = student
        context['registration_list'] = registration_list
        return context


class StudentCreate(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = StudentForm
    model = Student
    permission_required = 'courseinfo.add_student'


class StudentUpdate(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = StudentForm
    model = Student
    template_name = 'courseinfo/student_form_update.html'
    permission_required = 'courseinfo.change_student'


class StudentDelete(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Student
    success_url = reverse_lazy('courseinfo_student_list_urlpattern')
    permission_required = 'courseinfo.delete_student'

    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        registrations = student.registrations.all()
        if registrations.count() > 0:
            return render(
                request,
                'courseinfo/student_refuse_delete.html',
                {'student': student,
                 'registrations': registrations,
                 }
            )
        else:
            return render(
                request,
                'courseinfo/student_confirm_delete.html',
                {'student': student}
            )


class RegistrationList(ListView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Registration
    permission_required = 'courseinfo.view_registration'


class RegistrationDetail(DetailView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Registration
    permission_required = 'courseinfo.view_registration'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        registration = self.get_object()
        student = registration.student
        section = registration.section
        context['registration'] = registration
        context['student'] = student
        context['section'] = section
        return context


class RegistrationCreate(CreateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = RegistrationForm
    model = Registration
    permission_required = 'courseinfo.add_registration'


class RegistrationUpdate(UpdateView, LoginRequiredMixin, PermissionRequiredMixin):
    form_class = RegistrationForm
    model = Registration
    template_name = 'courseinfo/registration_form_update.html'
    permission_required = 'courseinfo.change_registration'


class RegistrationDelete(DeleteView, LoginRequiredMixin, PermissionRequiredMixin):
    model = Registration
    success_url = reverse_lazy('courseinfo_registration_list_urlpattern')
    permission_required = 'courseinfo.delete_registration'
