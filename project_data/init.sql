
CREATE TABLE users (
    user_id SERIAL,
    username TEXT,
    hashed_password TEXT
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    position TEXT NOT NULL,
    government_id TEXT NOT NULL
);

CREATE TABLE employers (
    employer_id SERIAL PRIMARY KEY,
    employer_name TEXT NOT NULL,
    government_id TEXT NOT NULL
);

COPY employees (first_name, last_name, position, government_id)
FROM '/docker-entrypoint-initdb.d/employees.csv'
DELIMITER ','
CSV HEADER;

COPY employers (employer_name, government_id)
FROM '/docker-entrypoint-initdb.d/employers.csv'
DELIMITER ','
CSV HEADER;
