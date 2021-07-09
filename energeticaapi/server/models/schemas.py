from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum


class Address(BaseModel):
    street: str
    number: str
    floor: Optional[str] = None
    door: Optional[str] = None
    postal_code = int
    province = str
    province_code = int
    city = str
    city_code = int

    class Config:
        schema_extra = {
            "example": {
                "street": "c/ Melancolía",
                "number": "7",
                "floor": "1",
                "door": "A",
                "postal_code": 47013,
                "province": "Palencia",
                "province_code": 36,  # https://api.somenergia.coop/data/provincies
                "city": "Villerías de Campos",
                # https://api.somenergia.coop/data/municipis/{provinceId}
                "city_code": 3765
            }
        }


class User(BaseModel):
    user_id: Optional[int]
    nif: str
    name: str
    first_surname: str
    second_surname: Optional[str] = None
    address: Address
    email: str
    phone_number: int
    alternative_phone_number: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "nif": "12345678A",
                "name": "Rick",
                "first_surname": "Sánchez",
                "second_surname": "Sánchez",
                "address": {
                    "street": "c/ Mahler",
                    "number": "5",
                    "floor": "entreplanta",
                    "door": "B",
                    "postal_code": 47009,
                    "province": "Valladolid",
                    "province_code": 49,
                    "city": "Valladolid",
                    "city_code": 4709
                },
                "email": "rick@rick.com",
                "phone_number": "654321987",
                "alternative_phone_number": "983660112"
            }
        }


class ContractRequestType(str, Enum):
    switching = "switching"
    new = "new"


class Tariff(str, Enum):
    tariff_20A = "2.0A"
    tariff_21A = "2.1A",
    tariff_20DHA = "2.0DHA"
    tariff_20DHS = "2.0DHS"
    tariff_21DHA = "2.1DHA"
    tariff_21DHS = "2.1DHS"
    tariff_30A = "3.0A"
    tariff_31A = "3.1A"
    tariff_31A_LB = "3.1A-LB"
    tariff_61 = "6.1"
    tariff_61A = "6.1A"
    tariff_61B = "6.1B"


class SupplyPoint(BaseModel):
    cups: str = Field(
        ..., title="Supply point identification code"
    )
    cnae: int = 9820
    tariff: Tariff
    power: float
    address: Address


class Contract(BaseModel):
    contract_id: Optional[int]
    contract_request_type: ContractRequestType
    supply_point: SupplyPoint
    change_holder: bool
    holder: User
    gives_donation: bool
    iban: str
