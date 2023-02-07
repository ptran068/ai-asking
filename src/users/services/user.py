from authtools.forms import User


class UserService:
    @classmethod
    def get_user(cls, user_id):
        user = User.objects.filter(id=user_id).first()
        return user