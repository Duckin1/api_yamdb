from enum import Enum


class UserRoles(Enum):
    '''Классы выбора ролей для пользователей'''

    admin = 'admin'
    moderator = 'moderator'
    user = 'user'

    @classmethod
    def choices(cls):
        