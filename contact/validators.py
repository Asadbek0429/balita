from django.core.validators import ValidationError


def validator_phone_number(number):
    if len(number) != 13:
        raise ValidationError("Telefon raqam uzunligi 13 ga teng bo'lishi kerak!")
    elif not number.startswith('+998'):
        raise ValidationError("Telefon raqam +998 bilan boshlanishi kerak!")
    elif not number[1:].isdigit():
        raise ValidationError("Telefon raqam faqat raqamlardan tashkil topgan bo'lishi kerak")
