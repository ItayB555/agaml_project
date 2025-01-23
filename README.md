# Agam leaderim project
Itay Berger

.env does not hold sensitive data, it builds the DB locally.
.csv files inside /project_data are being ignored as an LFS

## How to run
```shell
docker-compose build
docker-compose up -d
```

```http request
GET /health
POST /auth/register body {username: X password: Y}
POST /auth/login form data username=X password=Y

GET /employees/?filter_text=...&page=...
POST /employees/ body new_employee

GET /employers/?filter_text=...&page=...
POST /employers/ body new_employer
```