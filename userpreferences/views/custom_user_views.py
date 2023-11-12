from django.http import JsonResponse
from rest_framework import generics
from userpreferences.services.custom_user_services import CustomUserService


class CustomUserCreateView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        user_data = request.data
        created_user_data = CustomUserService.create_user(user_data)
        return JsonResponse({
            "message": "Kullanıcı oluşturacak",
            "user_data": created_user_data
        })


class CustomUserListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        users = CustomUserService.list_users()
        return JsonResponse({
            "message": "Kullanıcıları listeleyecek",
            "users": users
        })


class CustomUserUpdateView(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        updated_data = request.data
        updated_user_data = CustomUserService.update_user(user_id, updated_data)
        if updated_user_data:
            return JsonResponse({
                "message": "Kullanıcı güncellenecek",
                "user_data": updated_user_data
            })
        else:
            return JsonResponse({
                "message": f"Kullanıcı {user_id} bulunamadı"
            }, status=404)


class CustomUserDeleteView(generics.DestroyAPIView):
    lookup_url_kwarg = 'user_id'

    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get(self.lookup_url_kwarg)
        if CustomUserService.delete_user(user_id):
            return JsonResponse({
                "message": f"Kullanıcı {user_id} silindi"
            })
        else:
            return JsonResponse({
                "message": f"Kullanıcı {user_id} bulunamadı"
            }, status=404)

