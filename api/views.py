from push_notifications.models import GCMDevice
from rest_framework import generics
from .serializers import FaceSerializer
from .models import Face

fcm_device_id = 'fw39kG0b6jI:APA91bFDNmjaToqLCoUHPIicISZ2EM_N8Og2oe7s1BmrAotV976dFIJ6B-_Wkycczjnk19NP61yFb7YguqRpd-AIk7u2wJMU1wGGxfdivyBnxSa1RqFaSkvlsZf1ZC4HMCEgjunLycPi'

class CreateView(generics.ListCreateAPIView):
    queryset = Face.objects.all()
    serializer_class = FaceSerializer

    def perform_create(self, serializer):
        fcm_device = GCMDevice.objects.create(registration_id=fcm_device_id, cloud_message_type="FCM")
        fcm_device.send_message("Nie rozpoznano twarzy")


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Face.objects.all()
    serializer_class = FaceSerializer

