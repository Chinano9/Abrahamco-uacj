from typing import Optional, Tuple
from datetime import datetime
from src.data_manager import load_accounts, save_accounts, get_account, AccountDict

# Importar las funciones de soporte de los módulos
from src.modules import mod_cards  # Para HU 3.2
from src.modules import mod_analysis  # Para HU 4.4
from src.modules import mod_savings  # Para HU 6.4

# EL EQUIPO 2 ES EL UNICO QUE DEBE MODIFICAR ESTE ARCHIVO, SI NO ERES DEL EQUIPO 2 ABSTENTE DE ENTRAR AQUI! NO TOQUES NADA!!!


def update_balance(
    account_id: str, amount: float, description: str
) -> Tuple[bool, str]:
    """
    Realiza una transacción, implementando la lógica de balance, límites y seguridad.
    """
    accounts = load_accounts()
    account = get_account(account_id)

    # ... Verificación inicial de existencia/actividad ...

    # === CONEXIÓN CON EQUIPO 3 (HU 3.2: Bloqueo de Tarjeta Congelada) ===
    # if mod_cards.is_card_frozen(account): ...

    # >>> START: ZONA DE TRABAJO PRINCIPAL DEL EQUIPO 2 (HU 2.1, 2.2, 2.3, 2.4)

    # HU 2.1: Implementar Límite Diario aquí
    # HU 2.4: Implementar Comisión por Retiro aquí

    # >>> END: ZONA DE TRABAJO PRINCIPAL DEL EQUIPO 2

    new_balance: float = account["balance"] + amount

    # === CONEXIÓN CON EQUIPO 6 (HU 6.4: Requisito de Balance Mínimo) ===
    # Si es un retiro (amount < 0), llamar a la verificación del Equipo 6.
    # is_valid, error_msg = mod_savings.check_minimum_balance_rule(new_balance)
    # if not is_valid: return False, error_msg

    if new_balance < 0:
        # HU 2.2: Implementar registro de error por fondos insuficientes aquí
        return False, "Fondos insuficientes para la transacción."

    # 2. Actualizar y guardar
    for acc in accounts:
        if acc["id"] == account_id:
            acc["balance"] = new_balance

            # HU 2.3: Implementar fecha dinámica aquí
            transaction_date: str = "FECHA-DINÁMICA-AQUÍ"

            acc["transactions"].append(
                {
                    "date": transaction_date,
                    "amount": amount,
                    "description": description,
                    "category": "Sin Asignar",
                }
            )
            save_accounts(accounts)

            # === CONEXIÓN CON EQUIPO 4 (HU 4.4: Alerta de Sobregiro) ===
            warning_msg: Optional[str] = mod_analysis.check_low_balance_warning(new_balance)
            if warning_msg: return True, f"Transacción exitosa. {warning_msg} Nuevo balance: {new_balance}"

            return True, "Transacción exitosa. Nuevo balance: {}".format(new_balance)

    return False, "Error desconocido al actualizar."
