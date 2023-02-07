from rest_framework.decorators import action
from rest_framework.authentication import authenticate

from base_services.auth_jwt.jwt_helper import JWTRefreshTokenHelper, AuthJwtTokenService
from base_services.customized.exception import CustomException
from base_services.customized.validation_error import ValidationErr
from base_services.customized.view_mixin import GenericViewMixin
from users.mixins import UserLoginMixin
from users.models import User
from users.serializer.user import UserSerializer, UserLoginSerializer


class AuthViewSet(GenericViewMixin, UserLoginMixin):
    view_set = "auth"
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

    def create(self, request):
        data = request.data.copy()
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            kwargs = {
                "id": user.id,
                "request": request,
            }
            return self.response_login(**kwargs)

    @action(detail=False, methods=["POST"], permission_classes=())
    def login(self, request):
        """
        @apiVersion 1
        @api {post} /auth/login
        @apiName Login
        @apiGroup Auth

        @apiSuccess 200
        """
        data = request.data.copy()
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.filter(email=data.get('email')).first()
            if not user:
                raise CustomException(error=ValidationErr.DOES_NOT_EXIST, params=["user"])

            user = authenticate(email=user.email, password=data.get('password'))
            kwargs = {
                "id": user.id,
                "request": request,
            }
            return self.response_login(**kwargs)

    @action(detail=False, methods=["POST"], permission_classes=())
    def refresh_jwt_token(self, request):
        """
        @apiVersion 1
        @api {post} /auth/refresh_jwt_token Refresh jwt token
        @apiName RefreshJwtToken
        @apiGroup Auth

        @apiParam {String} refresh_token The refresh token is used to obtain a new token

        @apiSuccess 200
        """
        data = request.data.copy()
        jwt_refresh_token = data.get("refresh_token", None)
        if not jwt_refresh_token:
            raise CustomException(error=ValidationErr.REQUIRED, params=["refresh_token"])
        payload = JWTRefreshTokenHelper.decrypt(jwt_refresh_token)
        if not AuthJwtTokenService.validate_refresh_token(request, payload.get('uuid_token')):
            raise CustomException(error=ValidationErr.INVALID, params=["refresh_token"])

        return self.response_login(user=request.user, request=request)