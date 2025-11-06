from typing import List, Dict, Any, Tuple
from datetime import datetime
from src.data_manager import load_accounts, save_accounts, get_account
from test_data import get_test_account  # Importado para pruebas


def log_incident(
    account_id: str, description: str, priority: str = "MEDIA"
) -> Tuple[bool, str]:
    """HU 5.2 y 5.4: Añade un nuevo incidente (con prioridad) a la lista 'incidents'."""
    accounts = load_accounts()

    for acc in accounts:
        if acc.get("id") == account_id:
            # Asegurar que exista la lista de incidentes
            if "incidents" not in acc or not isinstance(acc["incidents"], list):
                acc["incidents"] = []

            # Crear identificador simple basado en timestamp
            incident_id = f"INC-{account_id}-{datetime.utcnow().strftime('%Y%m%d%H%M%S') }"

            incident = {
                "id": incident_id,
                "date": datetime.utcnow().isoformat(),
                "description": description,
                "priority": priority,
                "status": "ABIERTA",
            }

            acc["incidents"].append(incident)

            # Persistir cambios
            save_accounts(accounts)

            return True, incident_id

    return False, "Cuenta no encontrada"


def get_incident_history(account_id: str) -> List[Dict[str, Any]]:
    """HU 5.3: Devuelve la lista de incidentes registrados."""
    # El equipo debe implementar la lógica
    pass


if __name__ == "__main__":
    # ZONA DE PRUEBA: Usando el mock para asegurar que el campo 'incidents' existe.

    # mock_account_data = get_test_account("B2002")
    # print(f"Estado de incidentes en mock: {mock_account_data.get('incidents')}")
    # Equipo 5: Aqui hagan sus pruebas, prueben sus funciones y vean que todo funcione bien
    # Prueba en memoria (no toca data/accounts.json):
    # - Crea una cuenta mock con get_test_account
    # - Sustituye temporalmente load_accounts/save_accounts en este módulo
    # - Llama a log_incident y muestra resultados
    mock_acc = get_test_account("B2002")
    accounts = [mock_acc]

    # Guardar referencias originales
    _orig_load = load_accounts
    _orig_save = save_accounts

    try:
        # Monkeypatch local: las funciones usadas por log_incident buscarán
        # los nombres en el namespace global de este módulo.
        globals()["load_accounts"] = lambda: accounts
        globals()["save_accounts"] = lambda a: accounts.clear() or accounts.extend(a)

        print("=== PRUEBA EN MEMORIA: log_incident ===")
        print("Antes, incidents en mock:", mock_acc.get("incidents"))
        ok, res = log_incident("B2002", "Incidente de prueba en memoria", "ALTA")
        print("log_incident ->", ok, res)
        print("Después, incidents en mock:", mock_acc.get("incidents"))

    finally:
        # Restaurar funciones originales
        globals()["load_accounts"] = _orig_load
        globals()["save_accounts"] = _orig_save
