import rest_framework.viewsets
import rest_framework.authentication
import rest_framework.permissions
import rest_framework.status
import rest_framework.response


class Api(rest_framework.viewsets.ViewSet):
    """
    Default API Class
    """
    authentication_classes = (rest_framework.authentication.TokenAuthentication,
                              rest_framework.authentication.CsrfViewMiddleware)
    permission_classes = (rest_framework.permissions.AllowAny, )
    http = rest_framework.status

    def post_check(self):
        return {}, self.http.HTTP_401_UNAUTHORIZED

    def post(self, *args, **kwargs):
        data, status = self.post_check()
        return rest_framework.response.Response(data=data, status=status)

    def get_check(self):
        return {}, self.http.HTTP_401_UNAUTHORIZED

    def get(self, *args, **kwargs):
        data, status = self.get_check()
        return rest_framework.response.Response(data=data, status=status)

