from typing import Tuple
from src.data_manager import load_accounts, save_accounts, get_account
from test_data import get_test_account  # Importado para pruebas

# from src.core_logic import update_balance as core_update_balance


def deposit_to_goal(account_id: str, amount: float) -> Tuple[bool, str]:
    """
    HU 6.2: Mueve dinero del balance principal al 'savings_goal.current'.
    Debe llamar a core_update_balance para la resta.
    """
    # El equipo debe implementar la lógica
    pass


def check_goal_achieved(account_id: str) -> bool:
    """HU 6.3: Devuelve True si el ahorro actual es >= el objetivo."""
    # El equipo debe implementar la lógica
    pass


def check_minimum_balance_rule(new_balance: float) -> Tuple[bool, str]:
    """
    HU 6.4: Verifica si el nuevo balance cumple con la regla de mínimo $50.00.
    Retorna (True, "") si es válido o (False, "mensaje de error"). Llamada por core_logic.
    """
    # El equipo debe implementar la lógica
    pass


if __name__ == "__main__":
    # ZONA DE PRUEBA: Usando el mock para asegurar que el campo 'savings_goal' existe.
    # El equipo 6 prueba su lógica de esta forma antes de interactuar con el JSON real.

    # mock_account_data = get_test_account("B2002")
    # goal_info = mock_account_data.get('savings_goal')
    # print(f"Meta de ahorro en mock: {goal_info.get('target')}")

    pass
