from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    # Yetki seviyesini ekledik
    authority_level = models.IntegerField(default=1)  # 1: Normal kullanıcı, 2: Yönetici gibi.
    
    # Çakışmaları önlemek için related_name ekleniyor
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True,
    )

    def __str__(self):
        return self.username



class Voices(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey("Users", on_delete=models.CASCADE, related_name="voices")
    word = models.CharField(max_length=255, blank=True, null=True)  # Sesin başlığı veya açıklaması
    file = models.FileField(upload_to="voices/")  # Ses dosyasının yolu
    duration = models.FloatField(blank=True, null=True)  # Sesin süresi (saniye)
    owner_name = models.CharField(max_length=255)  # İsmi "Ad Soyad" formatında
    owner_gender = models.CharField(
        max_length=10,
        choices=[("male", "Erkek"), ("female", "Kadın")],
    )  # Cinsiyet
    language = models.CharField(
        max_length=20,
        choices=[("Turkish", "Türkçe"), ("English", "İngilizce")],
    )  # Dil bilgisi
    created_at = models.DateTimeField(auto_now_add=True)  # Oluşturulma tarihi

    def __str__(self):
        return f"{self.word or 'Kayıtsız Ses'} by {self.created_by.username}"
