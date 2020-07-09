from django.db import models

# Create your models here.





class DataHolder(models.Model):
    """
    {
            "users": [
                    {"first_name": "test", "last_name": "testend"},
                    {"first_name": "test", "last_name": "testend"}
                ],
            "booking_start_date":"2020-07-09T07:24:44.300Z",
            "booking_end_date": "2020-07-09T07:25:11.788Z"
    }

    """
    data = models.TextField(null=True)

    def __str__(self):
        return str(self.id)
