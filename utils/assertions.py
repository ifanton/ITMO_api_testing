from jsonschema import validate
from pydantic import BaseModel


class Assert:
    @staticmethod
    def validate_schema(instance: dict) -> None:  # метод принимает атрибут instance тип dict и ничего не возвращает
        validate(instance=instance, schema=BaseModel.schema())  # вызываем ф-ю validate для проверки json на валидность
