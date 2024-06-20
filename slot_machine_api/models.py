from django.db import models
from django.utils import timezone

# Create your models here.
class SlotMatrix(models.Model):
    slot_id = models.AutoField(primary_key=True) 
    matrix = models.JSONField()  
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        managed = False  # Indica a Django di non gestire questa tabella
        db_table = 'slot_matrices'  # Nome della tabella esistente

    def __str__(self):
        return f"SlotMatrix {self.slot_id}"


