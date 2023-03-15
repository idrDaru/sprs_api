from api.models.users import User

class UserController():
    def get_a_user(self, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return ""
