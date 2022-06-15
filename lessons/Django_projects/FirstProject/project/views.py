from rest_framework import generics
from project.models import Group, Student, Teacher
from project.serializers import GroupSerializer, GroupDetailSerializer, StudentsSerializer, TeachersSerializer


class GroupListView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetailView(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer


class StudentsListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


class TeachersListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer
