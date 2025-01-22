import psycopg2

from config import PostgresSettings
from exceptions import DatabaseConnectionError


class PostgresAccessor:
    def __init__(self,
                 host: str = PostgresSettings.HOST,
                 port: int = PostgresSettings.PORT,
                 database: str = PostgresSettings.DATABASE_NAME,
                 username: str = PostgresSettings.POSTGRES_USERNAME,
                 password: str = PostgresSettings.POSTGRES_PASSWORD
                 ):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        try:
            self.connection = psycopg2.connect(
                host=self.host, port=self.port,
                database=self.database,
                user=self.username, password=self.password
            )
            self.cursor = self.connection.cursor()
        except psycopg2.OperationalError:
            raise DatabaseConnectionError(self.host, self.port)
