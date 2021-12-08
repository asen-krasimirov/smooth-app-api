import html

from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from smooth_api.main.models import Job, AppliedJob
from smooth_api.main.serializers import JobSerializer, AppliedJobSerializer
from smooth_api.smooth_auth.models import SmoothSession, SmoothUser, BusinessProfile, ApplicantProfile
from smooth_api.smooth_auth.serializers import BusinessProfileSerializer, ApplicantProfileSerializer

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
            raise ValidationError({'error_message': 'All fields are mandatory!'})

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
            raise exceptions.AuthenticationFailed({'error_message': 'Not Authorized!'})

        return user


class JobList(GeneralOps, ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get(self, request, *args, **kwargs):
        owner_pk = request.query_params.get('owner_id')
        # serialized_profiles = []
        if owner_pk:
            try:
                jobs = Job.objects.filter(
                    owner=SmoothUser.objects.get(
                        pk=owner_pk
                    )
                )
            except:
                raise ValidationError({'error_message': 'User not found!'})
        else:
            # jobs = Job.objects.all()
            jobs = Job.objects.all()

        job_owner_ids = owner_pk if owner_pk else [
            job.owner.pk
            for job in jobs
        ]

        owner_profiles = BusinessProfile.objects.filter(
            pk__in=job_owner_ids
        )

        serialized_profiles = BusinessProfileSerializer(owner_profiles, many=True)

        page = self.paginate_queryset(jobs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(jobs, many=True)
        return Response({
            'jobs': serializer.data,
            'profiles': serialized_profiles.data
        })

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


class JobDetail(GeneralOps, RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get(self, request, *args, **kwargs):
        job = Job.objects.get(
            pk=kwargs['pk']
        )

        owner_profile = BusinessProfile.objects.get(
            pk=job.owner.pk
        )

        serialized_profile = BusinessProfileSerializer(owner_profile)

        serializer = self.get_serializer(job)

        return Response({
            'job': serializer.data,
            'profile': serialized_profile.data
        })

    def put(self, request, *args, **kwargs):
        escaped_data = self.get_and_escape_data(request)
        primary_key = kwargs['pk']

        job = Job.objects.get(pk=primary_key)

        job.title = escaped_data['title']
        job.description = escaped_data['description']
        job.type = escaped_data['job_type']
        job.status = escaped_data['status']

        job.save()

        owner_profile = BusinessProfile.objects.get(
            pk=job.owner.pk
        )

        return Response(
            {
                'job': JobSerializer(job, context=self.get_serializer_context()).data,
                'profile': BusinessProfileSerializer(owner_profile).data
            }
        )

    def delete(self, request, *args, **kwargs):
        owner = self.authenticate(request)
        job = Job.objects.get(pk=kwargs.get('pk'))

        if job and job.owner.pk == owner.pk:
            job.delete()
            return Response({'message': 'Successfully deleted!'})
        else:
            raise ValidationError({'error_message': 'Job not found!'})

# def test_view(request):
#     return HttpResponse(request)


class AppliedJobs(GeneralOps, ListAPIView):
    queryset = AppliedJob.objects.all()
    serializer_class = AppliedJobSerializer

    def get_and_escape_data(self, request):
        user = self.authenticate(request)

        try:
            job_pk = html.escape(request.data['job_id'])
            job = Job.objects.get(pk=job_pk)

            if AppliedJob.objects.filter(user=user, job=job).first():
                raise Exception('Job already applied to!')

        except Exception as error:
            raise ValidationError({'error_message': error})

        return {
            'job': job,
            'user': user,
        }

    def get(self, request, *args, **kwargs):
        user_pk = request.query_params.get('user_id')
        # serialized_profiles = []
        try:
            jobs = AppliedJob.objects.filter(
                user=SmoothUser.objects.get(
                    pk=user_pk
                )
            )
        except:
            raise ValidationError({'error_message': 'User not found!'})

        owner_profile = ApplicantProfile.objects.get(pk=user_pk)

        serialized_profile = ApplicantProfileSerializer(owner_profile)

        page = self.paginate_queryset(jobs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(jobs, many=True)
        return Response({
            'jobs': serializer.data,
            'profile': serialized_profile.data
        })

    def post(self, request):
        escaped_data = self.get_and_escape_data(request)

        applied_job = AppliedJob.objects.create(
            job=escaped_data['job'],
            user=escaped_data['user'],
        )

        return Response(
            AppliedJobSerializer(applied_job, context=self.get_serializer_context()).data
        )


class AppliedJobDetail(GeneralOps, RetrieveAPIView):
    queryset = AppliedJob.objects.all()
    serializer_class = AppliedJobSerializer

    def get(self, request, *args, **kwargs):
        job = Job.objects.get(
            pk=kwargs['pk']
        )

        applied_job = AppliedJob.objects.filter(
            job=job
        ).first()

        owner_profile = ApplicantProfile.objects.get(
            pk=applied_job.user.pk
        )

        serialized_profile = ApplicantProfileSerializer(owner_profile)

        serializer = self.get_serializer(applied_job)

        return Response({
            'job': serializer.data,
            'profile': serialized_profile.data
        })

    def delete(self, request, *args, **kwargs):
        user = self.authenticate(request)
        applied_job = AppliedJob.objects.get(pk=kwargs.get('pk'))

        if applied_job and applied_job.user.pk == user.pk:
            applied_job.delete()
            return Response({'message': 'Successfully unapplied!'})
        else:
            raise ValidationError({'error_message': 'Have not applied to this job!'})
