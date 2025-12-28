from django.db import models


class Person(models.Model):
    person = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.person


class Place(models.Model):
    place = models.CharField(max_length=15)
    is_active = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.place


class Booking(models.Model):
    person = models.ForeignKey(
        Person, 
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    place = models.ForeignKey(
        Place, 
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    booked_date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # Чтобы один пользователь не мог забронировать одно место дважды
        constraints = [
            models.UniqueConstraint(
                fields=['person', 'place'],
                name='unique_person_place_booking'
            )
        ]
    
    def __str__(self):
        return f'{self.person} - {self.place}'