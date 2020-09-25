

# Create your models here.
from uuid import uuid1

from cassandra.cqlengine import models, columns


class Hero(models.Model):
    hero_id = columns.TimeUUID(primary_key=True, default=uuid1())
    name = columns.Text(required=True, max_length=60)
    alias = columns.Text(required=True, max_length=60)
    email = columns.Text(required=True, max_length=60)

