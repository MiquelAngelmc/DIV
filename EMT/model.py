#Importar llibreríes

from libraries import*

from api import get_emt_stop_times, CURRENT_BEARER_TOKEN

# controller.py

class EmtModel:
    def __init__(self, view):
        self.view = view
        self._connectSignals()
        self.num_button = 2

    def _connectSignals(self):
        #self.view.pushButton.clicked.connect( self.model.consultStop)
        self.view.pushButton.clicked.connect( self.handle_consult_stop)


    def handle_consult_stop(self):
        text_Stop = self.view.lineEdit.text() 
        
        self.handle_consult_stop(self.num_button, text_Stop)
        
    
    def handle_consult_stop(self):
        text_Stop = self.view.lineEdit.text()
        # 1. Validació d'entrada INICIAL (sense cridar al Model)
        if not text_Stop.isdigit() or not text_Stop:
             self.view.display_warning("Entrada Invàlida", "Si us plau, introdueix un número de parada que sigui només d'un a 3 dígits.")
             return

        if len(text_Stop) < 1 or len(text_Stop) > 3:
            self.view.display_warning("Entrada Invàlida", "Si us plau, introdueix un número de parada que tingui entre 1 i 3 dígits.")
            return

        # 2. Crida al Model
        result = self.fetch_stop_times(text_Stop)
        
        # 3. Gestió de la resposta del Model
        if result['status'] == "error":
            # Mostra els errors retornats (Servidor, No Dades, etc.)
            self.view.display_warning("Error de Consulta", result['message'])
        

        match self.num_button:
            case 2:
                button_name = "pushButton_2"
            case 3:
                button_name = "pushButton_3"
            case 4:
                button_name = "pushButton_4"
            case 5:
                button_name = "pushButton_5"
            case 6:
                button_name = "pushButton_6"
            case 7:
                button_name = "pushButton_7"
                self.num_button = 1
            
        self.num_button += 1
        self.view.stopHistory(button_name, text_Stop)
        self.view.update_scroll_labels("label_7", text_Stop, "textStop", "timeStop")

    def fetch_stop_times(self, stop_id: str) -> dict:
        """
        Gestiona la petició d'API per obtenir els temps d'arribada
        """
        
        # 1. Crida la funció de l'API
        raw_data = get_emt_stop_times(stop_id, CURRENT_BEARER_TOKEN)

        # 2. Gestió d'errors de connexió/servidor (API ha retornat {'error': ...})
        """
        if "error" in raw_data:
            return {"status": "error", "message": raw_data["error"]}
        """
        # 3. Gestió de 'No hi ha dades disponibles'
        """
        if not raw_data.get('timeResult', {}).get('times'):
             return {"status": "error", "message": "No s'han trobat dades d'arribada per aquesta parada."}
        """
        # 4. Si tot és OK, retorna les dades i actualitza l'historial
        """
        if stop_id not in self.stop_history:
            self.stop_history.append(stop_id)
            self.stop_history = self.stop_history[-6:] # Mantenir un historial de 6
        """
        return {"status": "ok", "data": raw_data}

    # Mètode per obtenir el color 
    def get_line_color(self, line_number):
        return self.line_colors.get(str(line_number), '#000000')