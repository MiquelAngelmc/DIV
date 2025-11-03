import requests
import json # Per a manipular la resposta JSON

def get_emt_stop_times(stop_id: str, bearer_token: str) -> dict:
    """
    Realitza la petició GET a l'API de l'EMT per obtenir els horaris d'una parada.
    
    :param stop_id: L'identificador de la parada (e.g., "34").
    :param bearer_token: El token d'autorització de la teva sessió.
    :return: Un diccionari amb les dades de la resposta (horaris).
    """
    
    url = f"https://www.emtpalma.cat/maas/api/v1/agency/stops/{stop_id}/timestr"
    
    # Defineix totes les capçaleres (headers)
    headers = {
        # El Token d'autorització és la clau de la petició, però és temporal!
        "authorization": f"Bearer {bearer_token}", 
        "accept": "*/*",
        "accept-language": "es-ES,es;q=0.9",
        "priority": "u=1, i",
        "referer": f"https://www.emtpalma.cat/es/paradas/{stop_id}/es_pont_dinca_son_bonet", # Cal adaptar la URL del referer
        "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    }

    # Defineix les cookies (la cadena que hi havia darrere de -b ^)
    cookies = {
        "_ga": "GA1.1.1095588195.1761301745",
        "EmtPalmaCookie": "true",
        "_ga_DR79E3DM4C": "GS2.1.s1761908633$o8$g0$t1761908633$j60$l0$h0"
    }

    try:
        # Realitza la petició GET
        response = requests.get(url, headers=headers, cookies=cookies, timeout=10)
        
        # Comprova si la petició ha estat exitosa (codi 200)
        response.raise_for_status() 
        
        # Retorna el contingut de la resposta en format diccionari (JSON)
        return response.json()
        
    except requests.exceptions.HTTPError as errh:
        print(f"Error HTTP: {errh}")
        return {"error": f"HTTP Error: {errh.response.status_code}"}
    except requests.exceptions.RequestException as err:
        print(f"Error en la petició: {err}")
        return {"error": "No es pot connectar a l'API."}


# token 
CURRENT_BEARER_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJzdWIiOiI3Nzc2MzQiLCJpYXQiOjE3NjEzMDE3NDMsImV4cCI6MzMzOTE4MTc0MywidXNlcm5hbWUiOiIxNzYxMzAxNzQzMjAwSkU4V0VJMlJFWUVLSDUyOVUzTkgiLCJ0b2tlbl9kZXZpY2UiOiJhYWIyZDhmMzI0MDRmOTFjOTJiMjM4ZDMwMTE5OTg4Y2MyYmI0OTViZTY4M2EzMTgwOGNjYzQyMTYxZWIwNmVkIiwiZGV2aWNlX3R5cGVfaWQiOjMsInJvbGVzIjoiQU5PTklNTyJ9.rYih2WaFIFXnCkO-91K81CRoiOcmS0Sq_hw2PF9yvVHoDEJOpOZ0tJd3o1_Xpr-0"

stop_data = get_emt_stop_times("34", CURRENT_BEARER_TOKEN)

print(json.dumps(stop_data, indent=4, ensure_ascii=False))