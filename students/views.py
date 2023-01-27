# from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# from django.views.decorators.csrf import csrf_exempt
from webargs.fields import Str
from webargs.djangoparser import use_args
from django.db.models import Q

from .forms import CreateStudentForm, UpdateStudentForm
from .models import Student
# from .utils import format_list_students


# HttpRequest
# HttpResponse


# CRUD - Create Read Update Delete

@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query',
)
def get_students(request, args):
    students = Student.objects.all().order_by('birthday')

    # if 'first_name' in args:
    #     students = students.filter(first_name=args['first_name'])
    #
    # if 'last_name' in args:
    #     students = students.filter(last_name=args['last_name'])

    if len(args) and (args.get('first_name') or args.get('last_name')):
        students = students.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    # form = '''
    #     <form method="get">
    #       <label for="fname">First name:</label>
    #       <input type="text" id="fname" name="first_name"><br><br>
    #       <label for="lname">Last name:</label>
    #       <input type="text" id="lname" name="last_name"><br><br>
    #       <input type="submit" value="Submit"><br>
    #     </form>
    # '''

    # string = form + format_list_students(students)
    # response = HttpResponse(string)
    # return response
    return render(
        request=request,
        template_name='students/list.html',
        context={'title': 'List of Students', 'students': students}
    )


def detail_student(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'title': 'Detail of student', 'student': student})


# @csrf_exempt
def create_student_view(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))

    return render(request, 'students/create.html', {'form': form})


def update_student(request, pk):
    # student = Student.objects.get(pk=pk)
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'GET':
        form = UpdateStudentForm(instance=student)
    elif request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))

    return render(request, 'students/update.html', {'form': form})


def delete_student(request, pk):
    # st = Student.objects.get(pk=pk)
    st = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('list'))

    return render(request, 'students/delete.html', {'student': st})
