# import time
# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# class MyModel(models.Model):
#     name = models.CharField(max_length=100)

# # Signal receiver function
# @receiver(post_save, sender=MyModel)
# def my_signal_receiver(sender, instance, **kwargs):
#     print("Signal receiver started...")
#     # Simulate a delay to observe the synchronous behavior
#     time.sleep(5)
#     print("Signal receiver completed.")

# # Trigger function to save the model
# def create_instance_and_check_signal():
#     print("Creating a new instance of MyModel...")
#     instance = MyModel.objects.create(name="Test Instance")
#     print("Instance created.")

# # Execute the function to observe signal behavior
# create_instance_and_check_signal()


import time
from django.db import models