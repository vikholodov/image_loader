from django.db import models
from django.template.defaultfilters import floatformat
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Image(models.Model):
    image = models.ImageField(upload_to='uploads')
    thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(200, 200)],
                                      format='JPEG',
                                      options={'quality': 80})

    @property
    def width(self):
        return self.image.width

    @property
    def height(self):
        return self.image.height

    @property
    def size(self):
        return floatformat(self.image.size / 1048576, 2)