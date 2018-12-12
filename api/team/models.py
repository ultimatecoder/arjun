from django.db import models


class Member(models.Model):
    """Stores details of a team member"""

    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('regular', 'regular')
    )

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __repr__(self):
        return "<{}-{}>".format(self.firstname, self.id)
