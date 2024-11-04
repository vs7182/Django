import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver function
@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal receiver thread:", threading.current_thread().ident)
    print("Signal receiver executed.")

# Function to create a model instance and observe the thread behavior
def create_instance_and_check_thread():
    print("Caller thread:", threading.current_thread().ident)
    instance = MyModel.objects.create(name="Test Instance")
    print("Instance created.")

# Execute the function to observe thread behavior
create_instance_and_check_thread()
