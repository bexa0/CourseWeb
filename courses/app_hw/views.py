from django.shortcuts import render, redirect
from .forms import *


def course_list_view(request):
    course = Course.objects.all()
    context = {'course_list': course}

    return render(request, 'app/course_list.html', context)


def course_detail_view(request, pk):
    course = Course.objects.get(pk=pk)
    module = Module.objects.all()
    context = {'course': course, 'module_list': module}

    return render(request, 'app/course_detail.html', context)


def course_create_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    context = {'form': form}

    return render(request, 'app/course_create.html', context)


def course_delete_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        Course.objects.filter(title=title).delete()

        return redirect('course_list')

    return render(request, 'app/course_delete.html')


def course_update_view(request, pk):
    course = Course.objects.get(pk=pk)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)

    context = {'form': form}

    return render(request, 'app/course_update.html', context)


def module_list_view(request):
    module = Module.objects.all()
    context = {'module_list': module}

    return render(request, 'app/module_list.html', context)


def module_detail_view(request, pk):
    module = Module.objects.get(pk=pk)
    lesson = Lesson.objects.all()
    context = {'module': module, 'lesson_list': lesson}

    return render(request, 'app/module_detail.html', context)


def module_create_view(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = ModuleForm()
    context = {'form': form}

    return render(request, 'app/module_create.html', context)


def module_delete_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        Module.objects.filter(title=title).delete()

        return redirect('module_list')

    return render(request, 'app/module_delete.html')


def module_update_view(request, pk):
    module = Module.objects.get(pk=pk)

    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        if form.is_valid():
            form.save()
            return redirect('module_list')
    else:
        form = ModuleForm(instance=module)

    context = {'form': form}

    return render(request, 'app/module_update.html', context)


def lesson_list_view(request):
    lesson = Lesson.objects.all()
    context = {'lesson_list': lesson}

    return render(request, 'app/lesson_list.html', context)


def lesson_detail_view(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    context = {'lesson': lesson}

    return render(request, 'app/lesson_detail.html', context)


def lesson_create_view(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm()
    context = {'form': form}

    return render(request, 'app/lesson_create.html', context)


def lesson_delete_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')

        Lesson.objects.filter(title=title).delete()

        return redirect('lesson_list')

    return render(request, 'app/lesson_delete.html')


def lesson_update_view(request, pk):
    lesson = Lesson.objects.get(pk=pk)

    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')
    else:
        form = LessonForm(instance=lesson)

    context = {'form': form}

    return render(request, 'app/lesson_update.html', context)