from typing import Optional
from src.data_manager import load_accounts, save_accounts, get_account, AccountDict
from test_data import get_test_account  # Importado para pruebas


def is_card_frozen(account: AccountDict) -> bool:
    """HU 3.2: Verifica si la tarjeta está congelada. Llamada por core_logic."""
    # El equipo debe implementar la lógica
    pass


def freeze_card(account_id: str) -> bool:
    """HU 3.3: Cambia el 'virtual_card_status' a 'CONGELADA'. Retorna True si tiene éxito."""
    # El equipo debe implementar la lógica
    pass


def unfreeze_card(account_id: str) -> bool:
    """HU 3.4: Cambia el 'virtual_card_status' a 'ACTIVA'. Retorna True si tiene éxito."""
    # El equipo debe implementar la lógica
    pass


if __name__ == "__main__":
    # ZONA DE PRUEBA: Usando el mock para asegurar que el campo 'virtual_card_status' existe.

    # mock_account_data = get_test_account("A1001")
    # print(f"Estado de tarjeta en mock (inicial): {mock_account_data.get('virtual_card_status')}")

    # Nota: Para una prueba completa, el equipo deberá implementar primero freeze_card
    # y luego verificar que el valor en el JSON haya cambiado.

    # 1. Probar freeze_card("A1001")
    # 2. Verificar el valor en el JSON (o en el objeto mock guardado/recargado)
    # 3. Probar unfreeze_card("A1001")

    pass
