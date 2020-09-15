from django.db import models

# Has a SQLite DB with a table named `requests` that has the following columns:
# id (viz. autoincrementing int)
# type of request (e.g. GET, POST, PUT, DELETE)
# time of request (datetime)
# comment (text, NULL by default)

class Request(models.Model):
  # id = models.AutoField(primary_key=True)
  requestType = models.CharField(max_length=10)
  requestTime = models.DateTimeField('date created')
  comment = models.CharField(None, max_length=250)
