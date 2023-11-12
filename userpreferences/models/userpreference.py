from django.db import models

from userpreferences.models.customusers import CustomUser
from userpreferences.models.sectors import Sector


class UserPreference(models.Model):
    objects = None
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.sector.name}"
