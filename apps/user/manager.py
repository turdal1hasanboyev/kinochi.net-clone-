from django.contrib.auth.models import UserManager

import re


class CustomUserManager(UserManager):
    """
    Custom user manager class.
    """

    def create_user(self, email, first_name=None, last_name=None, image=None, phone_number=None, description=None, password=None, **extra_fields):
        """
        Creates a new user instance.
        """

        if not email:
            raise ValueError('Users must have an email address')
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError('Users must have a valid email address')

        """
        if phone_number:
            uzb_phone_pattern = r"^\+998 (33|55|77|88|90|91|93|94|95|97|98|99) \d{3} \d{2} \d{2}$" # O'zbekiston raqami kiritilishi
            if not re.match(uzb_phone_pattern, phone_number):
                raise ValueError('Users must have a valid phone number')"
        """

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          image=image, phone_number=phone_number, description=description, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name=None, last_name=None, image=None, phone_number=None, description=None, password=None, **extra_fields):
        """
        Creates a new superuser instance.
        """

        user = self.create_user(email=email, first_name=first_name, last_name=last_name, image=image,
                                phone_number=phone_number, description=description, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
