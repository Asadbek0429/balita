from django.db import models
from config.base_model import BaseModel
from .validators import validator_phone_number


class Contact(BaseModel):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13, validators=[validator_phone_number])
    message = models.TextField()

    def __str__(self):
        return self.name
