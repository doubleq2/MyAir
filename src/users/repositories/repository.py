# from dataclasses import dataclass

from rest_framework.generics import get_object_or_404

from users.api.serializers import UserCrudSerializer, UserSerializer
from users.models import User
from users.repositories.interface import BaseUser
from users.services.email import is_valid_email


class UserRepository(BaseUser):

    def get_all() -> list[dict]:
        users_list = User.objects.values(
            'id',
            'username',
            'first_name',
            'last_name',
            'link',
            'email',
        )
        return users_list

    def get(id) -> dict[str, any]:
        user = get_object_or_404(User, pk=id)
        serializer = UserCrudSerializer(user)
        return {
            'username': serializer.data['username'],
            'first_name': serializer.data['first_name'],
            'last_name': serializer.data['last_name'],
            'link': serializer.data['link'],
            'email': serializer.data['email'],
        }

    def post(request) -> dict[str, any]:
        if is_valid_email(request.data['email']):

            serializer = UserCrudSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save()

            return {
                'username': request.data['username'],
                'first_name': request.data['first_name'],
                'last_name': request.data['last_name'],
                'link': request.data['link'],
                'email': request.data['email'],
            }
        return

    def update(request, user_id) -> dict[str, any]:
        user = get_object_or_404(User, pk=user_id)
        serializer = UserCrudSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return {'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'link': user.link,
                'email': user.email,
                }

    def delete(user_id) -> dict[str]:
        user = get_object_or_404(User, pk=user_id)
        user_serializer = UserSerializer(user)
        user.delete()
        return {'id': user_serializer.data['id'],
                'username': user_serializer.data['username'],
                'first_name': user_serializer.data['first_name'],
                'last_name': user_serializer.data['last_name'],
                'link': user_serializer.data['link'],
                'email': user_serializer.data['email'],
                }
