# from django.shortcuts import render
import json
from django.http import JsonResponse
from slot_machine_api.models import Slot

def get_reels_slot(request):
    try:
        # Utilizzo della classe e del metodo per ottenere i simboli della slot machine
        symbols_matrix = Slot.generate_slot_symbols()

        # Converti symbols_matrix in formato JSON
        symbols_json = json.dumps(symbols_matrix)

        # Salva symbols_json nel database
        # slot_data = SlotData(data_json=symbols_json)
        # slot_data.save()

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

