from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    processed = models.BooleanField(default=False)

# Signal receiver function that updates the `processed` field
@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print("Inside signal receiver, setting `processed` to True.")
    instance.processed = True
    instance.save()

# Function to create an instance within a transaction and roll it back
def create_instance_with_transaction_rollback():
    try:
        with transaction.atomic():
            print("Creating a new instance of MyModel within a transaction...")
            instance = MyModel.objects.create(name="Test Instance")
            print("Instance created with `processed` set to:", instance.processed)

            # Fetch the instance to check if the signal changed `processed`
            instance.refresh_from_db()
            print("After signal, `processed` field is:", instance.processed)

            # Simulate an error to trigger a rollback
            raise Exception("Simulated error to rollback transaction")
    except Exception as e:
        print("Transaction rolled back due to:", e)

    # Check if the instance exists after rollback
    if MyModel.objects.filter(name="Test Instance").exists():
        print("Instance was not rolled back.")
    else:
        print("Instance was rolled back.")

# Run the function
create_instance_with_transaction_rollback()
