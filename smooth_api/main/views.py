import html

from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView
# from smooth_api.main.authentications import Authentication
from rest_framework.response import Response
from smooth_api.main.models import Job
from smooth_api.main.serializers import JobSerializer
from smooth_api.smooth_auth.models import SmoothSession, SmoothUser
from smooth_api.smooth_auth.serializers import SmoothUserSerializer

UserModel = get_user_model()


class GeneralOps:
    def get_and_escape_data(self, request):
        owner = self.authenticate(request)
        try:
            title = html.escape(request.data['title'])
            description = html.escape(request.data['description'])
            job_type = html.escape(request.data['type'])
            status = html.escape(request.data['status'])
        except KeyError:
            raise ValidationError('All fields are mandatory!')

        return {
            'owner': owner,
            'title': title,
            'description': description,
            'job_type': job_type,
            'status': status
        }

    @staticmethod
    def authenticate(request):
        key = request.query_params.get('AUTH_TOKEN')

        try:
            user = SmoothSession.objects.get(token=key).user
        except:
            raise exceptions.AuthenticationFailed('Not Authorized!')

        return user


class JobList(GeneralOps, ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get(self, request, *args, **kwargs):
        owner_pk = request.query_params.get('owner_id')
        if owner_pk:
            try:
                queryset = Job.objects.filter(
                    owner=SmoothUser.objects.get(
                        pk=owner_pk
                    )
                )
            except:
                raise ValidationError('User not found!')
        else:
            queryset = Job.objects.all()

        # queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        escaped_data = self.get_and_escape_data(request)

        job = Job.objects.create(
            owner=escaped_data['owner'],
            title=escaped_data['title'],
            description=escaped_data['description'],
            type=escaped_data['job_type'],
            status=escaped_data['status']
        )

        return Response(
            JobSerializer(job, context=self.get_serializer_context()).data
        )

    # def put(self, request):
    #     escaped_data = self.get_and_escape_data(request)
    #     primary_key = request.data['pk']
    #
    #     job = Job.objects.get(pk=primary_key)
    #
    #     job.title = escaped_data['title'],
    #     job.description = escaped_data['description'],
    #     job.type = str(escaped_data['job_type']),
    #     job.status = escaped_data['status']
    #
    #     job.save()
    #
    #     return Response(
    #         JobSerializer(job, context=self.get_serializer_context()).data
    #     )


class JobDetail(GeneralOps, RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # permission_classes = [
        # permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
    # ]

    def put(self, request, *args, **kwargs):
        escaped_data = self.get_and_escape_data(request)
        primary_key = kwargs['pk']

        job = Job.objects.get(pk=primary_key)

        job.title = escaped_data['title']
        # job.title = job.title[0]
        job.description = escaped_data['description']
        # job.description = job.description[0]
        job.type = escaped_data['job_type']
        # job.type = job.type[0]
        job.status = escaped_data['status']
        # job.status = job.status[0]

        job.save()

        return Response(
            JobSerializer(job, context=self.get_serializer_context()).data
        )
