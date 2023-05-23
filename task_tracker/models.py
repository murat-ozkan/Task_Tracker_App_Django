from django.db import models

class TaskTracker(models.Model):

    PRIORITY = ( # Burada büyük harf kullanıldı. Benden sonraki yazılımcı buna dokunma demek.
        (1, "HIGH"),
        (2, "MEDIUM"),
        (3, "LOW")
    )

    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    priority = models.SmallIntegerField(choices=PRIORITY, default=2)
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.title

# dunder method or magic method. Bu özel metotlar, Python üzerinde önceden tanımlı ve görevi olan metotlardır. Ortak özellikleri ise iki alt çizgi ile başlayıp bitiyor olmalar, isimlerini de buradan alıyorlar. (dunder: double underscore).