import psycopg2

from config import PostgresSettings
from models import UserInDB
from postgres.accessor import PostgresAccessor


class PostgresAuthenticationAccessor(PostgresAccessor):
    TABLE_NAME = "users"

    def __init__(self, host: str = PostgresSettings.HOST,
                 port: int = PostgresSettings.PORT,
                 database: str = PostgresSettings.DATABASE_NAME,
                 username: str = PostgresSettings.POSTGRES_USERNAME,
                 password: str = PostgresSettings.POSTGRES_PASSWORD):
        super().__init__(host, port, database, username, password)
        self.table = self.TABLE_NAME

    def get_user(self, username: str) -> UserInDB | None:
        query = f"SELECT user_id, username, hashed_password FROM {self.TABLE_NAME} WHERE username = '{username}' LIMIT 1"
        self.cursor.execute(query)
        fetched_user = self.cursor.fetchone()
        if fetched_user is None:
            return None

        user_id, username, hashed_password = fetched_user
        return UserInDB(user_id=user_id, username=username, hashed_password=hashed_password)

    def insert_new_user(self, username: str, hashed_password: str) -> bool:
        query = f"INSERT INTO {self.TABLE_NAME} (username, hashed_password) VALUES ('{username}', '{hashed_password}')"
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except psycopg2.DatabaseError:
            self.connection.rollback()
            return False
        else:
            return True
