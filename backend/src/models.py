from pydantic import BaseModel, EmailStr, field_validator


class Account(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("Name is required")
        return value.strip()

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        if not value:
            raise ValueError("Password is required")
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters")
        return value
