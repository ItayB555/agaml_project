from pydantic import BaseModel


class Employer(BaseModel):
    employer_name: str
    government_id: str
