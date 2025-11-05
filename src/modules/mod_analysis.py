from typing import Optional
from src.data_manager import get_account


def get_total_income(account_id: str) -> float:
    """HU 4.1: Suma solo las transacciones positivas (ingresos)."""
    pass


def get_total_expenses(account_id: str) -> float:
    """HU 4.2: Suma solo las transacciones negativas (gastos). Retorna un valor positivo."""
    pass


def count_transactions(account_id: str) -> int:
    """HU 4.3: Devuelve el número total de transacciones."""
    account = get_account(account_id)
    if account:
        return len(account.get("transactions", []))
    return 0


def check_low_balance_warning(new_balance: float) -> Optional[str]:
    """
    HU 4.4: Verifica si el nuevo balance está entre $0.01 y $10.00.
    Retorna el mensaje de advertencia si se cumple, None si no. Llamada por core_logic.
    """
    pass
