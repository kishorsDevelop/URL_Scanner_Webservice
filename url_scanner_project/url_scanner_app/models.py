from django.db import models

# Create your models here.

from django.db import models

class ScanResult(models.Model):
    url = models.URLField()
    screenshot = models.ImageField(upload_to='screenshots/')
    ip_address = models.CharField(max_length=50)
    source_url = models.URLField()
    destination_url = models.URLField()
    asn_information = models.CharField(max_length=100)
    ssl_certificate_details = models.TextField()
    page_source = models.TextField()
    natural_language_content = models.TextField()
    extracted_information = models.JSONField(null=True, blank=True)
