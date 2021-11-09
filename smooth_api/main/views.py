from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

from smooth_api.main.models import Job
from smooth_api.main.permissions import IsOwnerOrReadOnly
from smooth_api.main.serializers import JobSerializer
from smooth_api.smooth_auth.serializers import SmoothUserSerializer


# @csrf_exempt
# def job_list(request):
#     """
#     List all jobs, or create a new snippet.
#     """
#
#     if request.method == 'GET':
#         snippets = Job.objects.all()
#         serializer = JobSerializer(snippets, many=True)
#
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         serializer = JobSerializer(data=request.POST)
#
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return JsonResponse(serializer.data, status=201)
#
#         return JsonResponse(serializer.errors, status=400)


class JobList(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class JobDetail(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = SmoothUserSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
