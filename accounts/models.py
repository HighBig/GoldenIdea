from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from common.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, username, name, department, password=None):
        if not username:
            raise ValueError('Users must have a username')

        if not name:
            raise ValueError('Users must have a name')

        if not department:
            raise ValueError('Users must have a department')

        user = self.model(
            username=username,
            name=name,
            department=department
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, department, password):
        if not username:
            raise ValueError('Users must have a username')

        if not name:
            raise ValueError('Users must have a name')

        if not department:
            raise ValueError('Users must have a department')

        user = self.create_user(
            username=username,
            name=name,
            department=department,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, BaseModel):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    department = models.ForeignKey(
        'accounts.Department',
        on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'department']

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.name


class Department(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
