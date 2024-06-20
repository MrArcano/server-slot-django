# from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from slot_machine_api.models import SlotMatrix
from slot_machine_api.utils import Slot
import json

def get_reels_slot(request):
    try:
        # Utilizzo della classe e del metodo per ottenere i simboli della slot machine
        symbols_matrix = Slot.generate_slot_symbols()

        # Salva symbols_json nel database
        slot_matrix = SlotMatrix(matrix=symbols_matrix, created_at=timezone.now())
        slot_matrix.save()

        response_data = {
            'status': 'success',
            'data': symbols_matrix,
        }
        return JsonResponse(response_data)

    except Exception as e:
        
        response_data = {
            'status': 'failure',
            'data': [],  
        }
        return JsonResponse(response_data)  

