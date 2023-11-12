from userpreferences.models import CustomUser
from userpreferences.serializers import CustomUserSerializer


class CustomUserService:
    @staticmethod
    def create_user(user_data):
        serializer = CustomUserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    @staticmethod
    def list_users():
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return serializer.data

    @staticmethod
    def update_user(user_id, updated_data):
        try:
            user = CustomUser.objects.get(pk=user_id)
            serializer = CustomUserSerializer(instance=user, data=updated_data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data
        except CustomUser.DoesNotExist:
            return None

    @staticmethod
    def delete_user(user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            user.delete()
            return True
        except CustomUser.DoesNotExist:
            return False
