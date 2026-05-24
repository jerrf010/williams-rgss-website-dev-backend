from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Calendar
from clubs.models import Club

#@receiver(post_save, sender=Club)
#def create_calendar(sender, instance, created, **kwargs):
    # Temporary workaround: Calendar model does not currently define a club relation,
    # so creating a Calendar here raises TypeError when a Club is added via admin.
    # TODO: restore this behavior after adding Calendar.club to the model.
    # if created:
    #     Calendar.objects.create(
    #         name = instance.name,
    #         club=instance
    #     )
