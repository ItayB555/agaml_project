import psycopg2

from config import PostgresSettings
from models import Employee
from postgres.consts import PAGE_SIZE
from postgres.accessor import PostgresAccessor


class PostgresEmployeesAccessor(PostgresAccessor):
    TABLE_NAME = "employees"

    def __init__(self, host: str = PostgresSettings.HOST,
                 port: int = PostgresSettings.PORT,
                 database: str = PostgresSettings.DATABASE_NAME,
                 username: str = PostgresSettings.POSTGRES_USERNAME,
                 password: str = PostgresSettings.POSTGRES_PASSWORD):
        super().__init__(host, port, database, username, password)
        self.table = self.TABLE_NAME

    def search(self, filter_text: str, page: int = 1) -> list:

        offset = (page - 1) * PAGE_SIZE
        query = f"SELECT * FROM {self.TABLE_NAME} WHERE first_name LIKE '%{filter_text}%' OR last_name LIKE '%{filter_text}%' OR position LIKE '%{filter_text}%' OR government_id LIKE '%{filter_text}%' LIMIT {PAGE_SIZE} OFFSET {offset}"
        self.cursor.execute(query)
        fetched_employees = self.cursor.fetchall()
        return fetched_employees

    def insert(self, new_employee: Employee) -> bool:
        first_name, last_name, position, government_id = new_employee.dict().values()

        query = f"INSERT INTO {self.TABLE_NAME} (first_name, last_name, position, government_id) VALUES ('{first_name}', '{last_name}', '{position}', '{government_id}')"
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except psycopg2.DatabaseError:
            self.connection.rollback()
            return False
        else:
            return True
