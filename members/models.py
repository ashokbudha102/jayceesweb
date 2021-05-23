from django.db import models

# Create your models here.


class customDateField(models.DateField):
	def value_to_string(self, obj):
		val = self.value_from_object(obj)
		if val:
			val.replace(day=0, month=0)
			return val.isoformat()
		return ''


class yearTeam(models.Model):
	year=customDateField(auto_now=False)
	def __str__(self):
		return f'{self.id}-{self.year}'


statusJaycees = (("President", "President"),
                  ("Vice-President", "Vice-President"),
                  ("General Secretriat", "General Secretriat"),
                  ("Treasurer", "Treasurer"),
                  ("Member", "Member"))


class membersRobo(models.Model):
	photo = models.ImageField(default='profile_pics/default.png', null=True, blank=True,upload_to='profile_pics')
	name = models.CharField(max_length=100)
	yearMembership = models.ForeignKey(yearTeam, on_delete=models.CASCADE)
	status = models.CharField(
		max_length=30, choices=statusJaycees, default='General Member')

	def __str__(self):
		return f'{self.name}-{self.status}'

	class Meta:
		ordering = ['status']
