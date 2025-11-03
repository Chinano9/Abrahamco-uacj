from typing import Dict, Any

AccountDict = Dict[str, Any]


def get_test_account(account_id: str = "A1001") -> AccountDict:
    """
    Retorna la estructura de una cuenta de prueba para que los equipos prueben
    sus funciones sin dependencia del archivo accounts.json o de mod_onboarding.
    """
    return {
        "id": account_id,
        "owner": "Cuenta de Prueba",
        "balance": 1500.00,
        "is_active": True,
        "transactions": [
            {"date": "2025-10-25", "amount": -200.00, "description": "Gasto"},
            {"date": "2025-10-28", "amount": 500.00, "description": "Ingreso"},
        ],
        "virtual_card_status": "ACTIVA",  # Necesario para Equipo 3
        "incidents": [],  # Necesario para Equipo 5
        "savings_goal": {
            "target": 1000.00,
            "current": 100.00,
        },  # Necesario para Equipo 6
    }
