from starlette import status
from starlette.responses import Response


def database_connection_error_handler() -> Response:
    return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
