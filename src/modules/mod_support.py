from typing import List, Dict, Any, Tuple
from datetime import datetime, timezone
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
            incident_id = f"INC-{account_id}-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}"

            incident = {
                "id": incident_id,
                "date": datetime.now(timezone.utc).isoformat(),
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
    # Cargar todas las cuentas
    accounts = load_accounts()

    for acc in accounts: 
        if acc.get("id") == account_id:
            # Verificar que tenga incidentes
            incidents = acc.get("incidents", [])
            # Retorna la lista de incidentes vacia si no hay alguna
            return incidents
    # En caso de que no se encuentra la cuenta
    return []

if __name__ == "__main__":
    # ZONA DE PRUEBA: Usando el mock para asegurar que el campo 'incidents' existe.
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
        #globals()["save_accounts"] = lambda a: accounts.clear() or accounts.extend(a)
        globals()["save_accounts"] = lambda a: None  # No hace nada en memoria

        print("=" * 50)
        print("PRUEBA EN MEMORIA: log_incident con test_data")
        print("=" * 50)
        
        # Prueba 1: Crear un incidente con prioridad MEDIA (por defecto)
        print("\n[Prueba 1] Incidente con prioridad MEDIA:")
        print(f"Antes, incidents: {mock_acc.get('incidents')}")
        ok, res = log_incident("B2002", "Error al acceder a cuenta", "MEDIA")
        print(f"log_incident -> Éxito: {ok}, ID: {res}")
        print(f"Después, incidents: {mock_acc.get('incidents')}\n")
        
        # Prueba 2: Crear un incidente con prioridad ALTA
        print("[Prueba 2] Incidente con prioridad ALTA:")
        ok, res = log_incident("B2002", "No puedo hacer transferencias", "ALTA")
        print(f"log_incident -> Éxito: {ok}, ID: {res}")
        print(f"Total incidents registrados: {len(mock_acc.get('incidents'))}")
        print(f"Contenido: {mock_acc.get('incidents')}\n")
        
        # Prueba 3: Intentar registrar en una cuenta inexistente
        print("[Prueba 3] Incidente en cuenta inexistente:")
        ok, res = log_incident("NOEXISTE", "Test", "ALTA")
        print(f"log_incident -> Éxito: {ok}, Mensaje: {res}\n")

        # Prueba 4: Obtener el historial de incidentes de una cuenta existente
        print("[Prueba 4] Historia de incidentes para cuentas existentes:")
        history = get_incident_history("B2002")
        print(f"get_incident_history -> Total incidentes: {len(history)} incidentes encontrados")
        for i, inc in enumerate(history, 1):
            print(f" Incidente {i}: {inc['description']} | (Prioridad: {inc['priority']}, Estado: {inc['status']})\n")

        # Prueba 5: Obtener el historial de incidentes de una cuenta inexistente
        print("[Prueba 5] Historia de incidentes para cuenta inexistente:")
        history = get_incident_history("NOEXISTE")
        print(f"get_incident_history -> Total incidentes: {len(history)} incidentes encontrados\n")

    finally:
        # Restaurar funciones originales
        globals()["load_accounts"] = _orig_load
        globals()["save_accounts"] = _orig_save
