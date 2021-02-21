from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, staff_id, first_name, last_name, password=None, **extra_fields):
        if not staff_id:
            raise ValueError('Staff ID is required')
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=staff_id,
            staff_id=staff_id,
        )

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, staff_id, first_name, last_name, password):
        user = self.create_user(staff_id=staff_id, first_name=first_name,last_name=last_name,password=password)

        user.is_supervisor = True
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.username = staff_id
        user.save(using=self.db)

        return user


USER_TYPE = {
    ('MG', 'Manager'),
    ('EM', 'Employee'),

}

USER_STATUS = {
    ('AC', 'Active'),
    ('IN', 'Inactive'),
}


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, blank=True, null=True)
    staff_id = models.CharField(max_length=255, unique=True)
    user_type = models.CharField(max_length=255, blank=True, null=True, choices=USER_TYPE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    status = models.CharField(max_length=100, blank=True, null=True, choices=USER_STATUS)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'staff_id'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def user_kind(self):
        return self.get_user_type_display()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('staff_id', 'date_joined')
        db_table = 'user'

    def __str__(self):
        return self.full_name()