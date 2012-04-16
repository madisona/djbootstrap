from django.db import models

class SampleModel(models.Model):
    what = models.CharField(max_length=25, help_text="What do you like?")
    when = models.DateField(help_text="When would you like it?")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.what)
