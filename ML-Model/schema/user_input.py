
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities

# Pydantic model  to validate incoming data

class UserInput(BaseModel):

    age: Annotated[int, Field(...,gt=0, lt=120, description='Age of the User')]
    weight: Annotated[float, Field(...,gt=0, description='Weight of the User')]
    height: Annotated[float, Field(...,gt=0, description='Height of the User')]
    income_lpa: Annotated[float, Field(...,gt=0, description='Income LPA of the User')]
    smoker: Annotated[str, Field(..., description='User do smoke or not')]
    city: Annotated[str, Field(..., description='User belongs from City')]
    occupation: Annotated[Literal['Software Engineer','Data Scientist','Teacher',
            'Doctor','Student','Architect','Manager','Analyst','Consultant',
          'Engineer'], Field(..., description='Occupation of the user')]


    @field_validator('city')
    @classmethod
    def titlecase_city(cls, val: str) -> str:
        val = val.strip().title()
        return val

    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height **2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
                return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "Young"
        elif self.age < 45:
            return "Adult"
        elif self.age < 60:
            return "middle_aged"
        else:
            return "senior" 

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3     