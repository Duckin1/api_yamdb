from enum import Enum

from rest_framework import serializers


class UserRoles(Enum):
    '''Классы выбора ролей для пользователей'''

    admin = 'admin'
    moderator = 'moderator'
    user = 'user'

    @classmethod
    def choices(cls):
        return tuple((attribute.name, attribute.value) for attribute in cls)

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError(
                'Использовать имя me в качестве username запрещено'
            )
        return data
