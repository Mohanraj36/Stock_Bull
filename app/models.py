from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100, null=True, blank=True)
    reset_email_otp = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reset_email_otp_created_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Predictioncount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    predictions_count = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.username

class Usersaved(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    stock_ticker_value = models.CharField(max_length=20, blank=True)
    stock_number_of_days = models.IntegerField(null=True)
    stock_confidence = models.FloatField(null=True)
    stock_data = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.user.username

class Userprediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    graph_id = models.PositiveIntegerField(default=0, blank=True)
    profit_loss = models.CharField(max_length=10, choices=[('profit', 'Profit'), ('loss', 'Loss')], blank=True)
    button_clicked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
