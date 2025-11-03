from typing import List, Dict, Any, Tuple
from datetime import datetime
from src.data_manager import load_accounts, save_accounts, get_account
from test_data import get_test_account  # Importado para pruebas


def log_incident(
    account_id: str, description: str, priority: str = "MEDIA"
) -> Tuple[bool, str]:
    """HU 5.2 y 5.4: Añade un nuevo incidente (con prioridad) a la lista 'incidents'."""
    # El equipo debe implementar la lógica
    pass


def get_incident_history(account_id: str) -> List[Dict[str, Any]]:
    """HU 5.3: Devuelve la lista de incidentes registrados."""
    # El equipo debe implementar la lógica
    pass


if __name__ == "__main__":
    # ZONA DE PRUEBA: Usando el mock para asegurar que el campo 'incidents' existe.

    # mock_account_data = get_test_account("B2002")
    # print(f"Estado de incidentes en mock: {mock_account_data.get('incidents')}")
    # Equipo 5: Aqui hagan sus pruebas, prueben sus funciones y vean que todo funcione bien
    pass
