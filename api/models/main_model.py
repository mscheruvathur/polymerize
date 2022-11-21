from djongo import models


class MainModel(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    added_by = models.CharField(max_length=255, null=True, default="Anonymous")

    def active_inactive(self):
        self.is_active = not self.is_active
        self.save()

    def update_added_by(self, added_by):
        self.added_by = added_by
        self.save()

    class Meta:
        abstract = True