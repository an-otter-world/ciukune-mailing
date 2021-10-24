"""Test plugged view."""
from rest_framework.views import APIView
from rest_framework.response import Response

from ciukune.core.models import User
from ciukune.mailing.models import Mail
from ciukune.core.serializers.user import UserSerializer

class TestView(APIView):
    """User view set, providing standard user endpoints."""
    authentication_classes = ()
    permission_classes = ()

    def get(self, request):
        users = User.objects.all()
        user = users[0]
        #mail, _ = MailAddress.objects.get_or_create(name = 'test@test.test', user=user)
        print(user.mail_set.all())
        #user.mail_address_set.create(name='test@test.test')
        serializer = UserSerializer(instance=users[0], context={'request': request})
        return Response(serializer.data)
