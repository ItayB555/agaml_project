import psycopg2

from config import PostgresSettings


class PostgresAccessor:
    def __init__(self,
                 host: str = PostgresSettings.HOST,
                 port: int = PostgresSettings.PORT,
                 database: str = PostgresSettings.DATABASE_NAME,
                 username: str = PostgresSettings.USERNAME,
                 password: str = PostgresSettings.PASSWORD
                 ):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password

        self.connection = psycopg2.connect(
            host=self.host, port=self.port,
            database=self.database,
            user=self.username, password=self.password
        )
        self.cursor = self.connection.cursor()
