from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ViewSet):
    def list(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        job = get_object_or_404(Job, pk=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='experience/(?P<years>\d+)')
    def jobs_by_experience(self, request, years=None):
        jobs = Job.objects.filter(years_of_experience=years)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='grouped-by-experience')
    def group_jobs_by_experience(self, request):
        grouped_jobs = {}
        for job in Job.objects.all():
            grouped_jobs.setdefault(job.years_of_experience, []).append(JobSerializer(job).data)
        return Response(grouped_jobs)