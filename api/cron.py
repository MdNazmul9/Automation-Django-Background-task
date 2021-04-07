from .models import Test

def my_scheduled_job():
    Test.objects.create(name='testUser')
  