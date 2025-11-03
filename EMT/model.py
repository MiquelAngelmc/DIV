# Importar llibreríes

from libraries import *

from api import get_emt_stop_times, CURRENT_BEARER_TOKEN

def get_emt_line_colors_mock() -> dict:
    """Retorna un diccionari amb LineCode -> Color HEX (Simulació)."""
    return {
        '1': '#6B21A8',  # Morat 
        '3': '#0099FF',  # Blau clar 
        '7': '#CC0000',  # Vermell 
        '10': '#FF9900', # Taronja
        '25': '#00CC66', # Verd
        'N4': '#333333', # Nit (Negre/Gris)
    }

class EmtModel:
    def __init__(self, view):
        self.view = view
        self.line_colors = get_emt_line_colors_mock() 
        
        self._connectSignals()
        self.num_button = 2 

    def _connectSignals(self):
        # Connexió del botó principal de consulta
        self.view.pushButton.clicked.connect(self.handle_consult_stop)

        # Connexió dels botons d'historial 
        self.view.pushButton_2.clicked.connect(lambda: self._execute_stop_query_from_history(self.view.pushButton_2.text()))
        self.view.pushButton_3.clicked.connect(lambda: self._execute_stop_query_from_history(self.view.pushButton_3.text()))
        self.view.pushButton_4.clicked.connect(lambda: self._execute_stop_query_from_history(self.view.pushButton_4.text()))
        self.view.pushButton_5.clicked.connect(lambda: self._execute_stop_query_from_history(self.view.pushButton_5.text()))
        self.view.pushButton_6.clicked.connect(lambda: self._execute_stop_query_from_history(self.view.pushButton_6.text()))
        self.view.pushButton_7.clicked.connect(lambda: self._execute_stop_query_from_history(self.view.pushButton_7.text()))
    
    def handle_consult_stop(self):
        """Punt d'entrada principal de consulta (des del camp de text)."""
        text_Stop = self.view.lineEdit.text().strip()
        self._execute_stop_query(text_Stop, update_history=True)

    def _execute_stop_query_from_history(self, stop_text: str):
        """Executa la consulta."""
        if not stop_text.isdigit() or not stop_text.strip():
            self.view.display_warning("Historial Buit", "Aquest botó de l'historial encara no té cap parada assignada.")
            return

        self._execute_stop_query(stop_text, update_history=False)

    def _execute_stop_query(self, stop_id: str, update_history: bool):
        """
        Lògica principal de consulta d'una parada.
        """
        
        # Validació d'entrada
        if not stop_id.isdigit() or not (1 <= len(stop_id) <= 3):
            self.view.display_warning("Entrada Invàlida", "Si us plau, introdueix un número de parada que tingui entre 1 i 3 dígits (només números).")
            return
        
        

        # Crida al Model
        result = self.fetch_stop_times(stop_id)
        
        if result.get('status') == "error":
            # Si l'API retorna error, ho mostrem i acabem
            self.view.display_warning("Error de Consulta", result['message'])
            return
            
        if update_history:
            button_name = f"pushButton_{self.num_button}"
            self.num_button = 2 if self.num_button == 7 else self.num_button + 1 
            self.view.stopHistory(button_name, stop_id)
        
        arrivals_found = False
        
        for line_data in result.get('data', []):
            line_code = line_data.get('lineCode')
            
            for vehicle in line_data.get('vehicles', []):
                
                destination = vehicle.get('destination', 'Desconeguda')
                seconds = vehicle.get('seconds', 0)
                minutes = round(seconds / 60)
                
                # Obtenció del color de la línia, per defecte gris
                line_color = self.line_colors.get(line_code, '#888888')

                colored_line = f'<span style="background-color: {line_color}; color: white; padding: 2px 6px; border-radius: 4px; font-weight: bold;">{line_code}</span>'
                
                formatted_html = f"<b>Parada {stop_id}:</b> {colored_line} dir. {destination} - <span style='font-weight: bold; color: {line_color};'>{minutes} minuts</span>"
                 
                self.view.add_scroll_label(formatted_html)
                arrivals_found = True
                
                return 

        # 7. Missatge si no es troba cap autobús
        if not arrivals_found:
            self.view.add_scroll_label(f"Parada {stop_id}: No hi ha busos programats o les dades són buides.")


    def fetch_stop_times(self, stop_id: str) -> dict:
        """
        Gestiona la petició d'API per obtenir els temps d'arribada (utilitzant la funció API real/simulada)
        """
        # 1. Crida la funció de l'API
        raw_data = get_emt_stop_times(stop_id, CURRENT_BEARER_TOKEN)

        if isinstance(raw_data, dict) and "error" in raw_data:
            error_msg = raw_data.get("message", raw_data["error"])
            return {"status": "error", "message": f"Error EMT API: {error_msg}"}

        return {"status": "ok", "data": raw_data}
