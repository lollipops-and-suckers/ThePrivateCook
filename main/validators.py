from django.core.exceptions import ValidationError

def validate_num_of_stars(number):
    if (number < 1 or number > 5):
        raise ValidationError(f"The number of {number} stars is not between 1 and 5")