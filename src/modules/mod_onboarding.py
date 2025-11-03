from typing import Tuple
from src.data_manager import load_accounts, save_accounts, AccountDict


def create_new_account(owner_name: str, initial_deposit: float) -> Tuple[bool, str]:
    """
    Crea una nueva cuenta e implementa las validaciones de HU 1.1 y 1.2.
    También implementa las estructuras iniciales (HU 3.1, 5.1, 6.1) para otros equipos.
    Retorna (True, account_id) o (False, mensaje_error).
    """
    accounts = load_accounts()

    # HU 1.1: Implementar Validación de Nombre aquí
    # HU 1.2: Implementar Mínimo Inicial aquí

    # Si las validaciones son exitosas, crea la estructura:
    new_id: str = "C" + str(len(accounts) + 100)
    new_account: AccountDict = {
        "id": new_id,
        "owner": owner_name,
        "balance": initial_deposit,
        # HU 1.3: Estado inicial
        "is_active": True,
        # HU 3.1: Campo para Tarjeta Virtual
        "virtual_card_status": "ACTIVA",
        # HU 5.1: Campo para registro de incidentes
        "incidents": [],
        # HU 6.1: Campo para Metas de Ahorro
        "savings_goal": {"target": 0.00, "current": 0.00},
        "transactions": [],
    }

    accounts.append(new_account)
    save_accounts(accounts)
    return True, new_id


def toggle_account_status(account_id: str) -> bool:
    """HU 1.3: Cambia el estado 'is_active' de la cuenta. Retorna True si tiene éxito."""
    # El equipo debe implementar la lógica
    pass


def check_status(account_id: str) -> bool:
    """HU 1.4: Devuelve True si la cuenta está activa, False si está inactiva o no existe."""
    # El equipo debe implementar la lógica
    pass
