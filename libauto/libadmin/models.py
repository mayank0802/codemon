from django.db import models

class books_info(models.Model):
	book_id = models.AutoField(primary_key = True)
	book_no = models.IntegerField()
	book_author = models.CharField(max_length = 50)
	book_publication = models.CharField(max_length = 50)
	book_title = models.CharField(max_length = 40)
	def __str__(self):
		return self.book_title
