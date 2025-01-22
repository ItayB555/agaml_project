from starlette import status
from starlette.responses import JSONResponse


def database_connection_error_handler() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content=dict(message="Database connection error"))
