from django.db import models


class News(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	created_at = models.DateTimeField(null=True)

	def __str__(self):
		return self.title


	class Meta:
		ordering = ['-created_at']

		verbose_name_plural = 'News'
