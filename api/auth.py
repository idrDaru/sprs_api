import environ, jwt, os
from datetime import datetime, timedelta

class Auth():
    global env
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

    def create_token(self, data):
        """
        Create JWT Token
        """
        payload = {
            'data': data,
            'exp': datetime.now() + timedelta(days=1)
        }
        token = jwt.encode(payload, env('SECRET_KEY'), algorithm="HS256")

        return token
    
    def extract_token(self, token):
        """
        Extract JWT Token
        """
        return jwt.decode(token, env('SECRET_KEY'), algorithms="HS2567").get('data')

    