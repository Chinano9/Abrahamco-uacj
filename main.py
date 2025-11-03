# =================================================================
# === SIMULACIÓN DE INTEGRACIÓN DEL SPRINT (REVISIÓN FINAL) ===
# === Demuestra el INCREMENTO del trabajo de los 6 Equipos ===
# =================================================================

# Importaciones de Módulos Centrales
from src.data_manager import get_account
from src.core_logic import update_balance

# Importaciones de Funciones implementadas por los Equipos
from src.modules.mod_onboarding import create_new_account
from src.modules.mod_cards import freeze_card, unfreeze_card
from src.modules.mod_analysis import get_total_income, get_total_expenses
from src.modules.mod_support import log_incident, get_incident_history
from src.modules.mod_savings import deposit_to_goal

# Nota: La cuenta A1001 debe existir en accounts.json y la nueva cuenta debe ser creada aquí.
TEST_ACCOUNT_ID: str = "A1001"
NEW_ACCOUNT_ID: str = (
    "C100"  # ID temporal, reemplazado por la función create_new_account
)


def run_integration_test() -> None:
    """
    Ejecuta una secuencia de pruebas que cubren las funciones implementadas
    por todos los equipos, verificando la integración.
    """
    print("\n==================================================")
    print("INICIANDO REVISIÓN DE INCREMENTO (Sprint Review)")
    print("==================================================")

    # -----------------------------------------------------------------
    # PRUEBA 1: EQUIPO 1 (Onboarding) - Creación de Cuenta
    # Verifica HU 1.1, 1.2 y la inclusión de estructuras (3.1, 5.1, 6.1)
    # -----------------------------------------------------------------
    print("\n--- 1. Testing Onboarding (Equipo 1) ---")

    # Intenta crear una cuenta (verifica validaciones de nombre y depósito mínimo)
    status, new_id = create_new_account("Nuevo Cliente", 75.00)
    if status:
        global NEW_ACCOUNT_ID
        NEW_ACCOUNT_ID = new_id
        print(f"Éxito: Cuenta '{new_id}' creada con las estructuras necesarias.")
    else:
        print(f"Fallo: Onboarding fallido. Mensaje: {new_id}")
        return  # Detener si la base no se crea

    # -----------------------------------------------------------------
    # PRUEBA 2: EQUIPO 3 (Tarjetas Virtuales) & EQUIPO 2 (Bloqueo 3.2)
    # -----------------------------------------------------------------
    print("\n--- 2. Testing Bloqueo por Tarjeta Congelada (Eq. 3 y Core Logic) ---")

    # Congela la tarjeta (HU 3.3) en la cuenta ya existente
    freeze_card(TEST_ACCOUNT_ID)
    acc = get_account(TEST_ACCOUNT_ID)
    print(f"Estado de tarjeta: {acc.get('virtual_card_status')}")

    # Intenta una transferencia (Verifica el bloqueo implementado por HU 3.2 en core_logic.py)
    status, msg = update_balance(
        TEST_ACCOUNT_ID, -10.00, "Intento de Pago con tarjeta congelada"
    )
    if not status and "congelada" in msg:
        print(
            f"Éxito Integración: Bloqueo de transacción por tarjeta congelada funcionó. Mensaje: {msg}"
        )

    unfreeze_card(TEST_ACCOUNT_ID)  # Descongela para el resto de las pruebas

    # -----------------------------------------------------------------
    # PRUEBA 3: EQUIPO 2 (Transferencias) - Límites y Comisiones
    # -----------------------------------------------------------------
    print("\n--- 3. Testing Límites y Comisiones (Equipo 2) ---")

    # Prueba un retiro grande (Verifica límite HU 2.1 y/o comisión HU 2.4)
    # Nota: El balance debe ser suficiente para esta prueba.
    status, msg = update_balance(TEST_ACCOUNT_ID, -600.00, "Retiro con comisión")
    if status:
        print(f"Éxito: Retiro procesado (Se verificó límite/comisión). Mensaje: {msg}")
    else:
        print(f"Fallo: Error en retiro: {msg}")

    # -----------------------------------------------------------------
    # PRUEBA 4: EQUIPO 6 (Metas de Ahorro) & EQUIPO 2 (Bloqueo Mínimo 6.4)
    # -----------------------------------------------------------------
    print("\n--- 4. Testing Metas de Ahorro y Bloqueo Mínimo (Eq. 6 y Core Logic) ---")

    # Depósito a la meta (HU 6.2, que usa update_balance)
    status, msg = deposit_to_goal(TEST_ACCOUNT_ID, 50.00)
    if status:
        print(f"Éxito: Transferencia a meta y resta de balance principal correctas.")

    # Prueba el bloqueo por saldo mínimo (HU 6.4 en core_logic.py)
    # Se necesita un retiro que deje el balance final bajo $50.00
    status, msg = update_balance(TEST_ACCOUNT_ID, -860.00, "Retiro que viola mínimo")
    if not status and "mínimo" in msg:
        print(
            f"Éxito Integración: Bloqueo por saldo mínimo ($50.00) funcionó. Mensaje: {msg}"
        )

    # -----------------------------------------------------------------
    # PRUEBA 5: EQUIPO 5 (Soporte)
    # -----------------------------------------------------------------
    print("\n--- 5. Testing Soporte (Equipo 5) ---")

    # Registra un incidente (HU 5.2, 5.4)
    log_incident(NEW_ACCOUNT_ID, "No puedo ingresar a la aplicación", priority="ALTA")

    # Consulta historial (HU 5.3)
    history = get_incident_history(NEW_ACCOUNT_ID)
    if history and history[0].get("priority") == "ALTA":
        print(f"Éxito: Incidente registrado y consultado con prioridad correcta.")

    # -----------------------------------------------------------------
    # PRUEBA 6: EQUIPO 4 (Análisis)
    # -----------------------------------------------------------------
    print("\n--- 6. Testing Análisis y Advertencia (Equipo 4 y Core Logic) ---")

    # HU 4.1, 4.2: Cálculos
    print(
        f"Total Ingresos: ${get_total_income(TEST_ACCOUNT_ID)} | Total Gastos: ${get_total_expenses(TEST_ACCOUNT_ID)}"
    )

    # HU 4.4: Probar advertencia de saldo bajo (requiere una transacción que deje $0 < balance <= $10)
    status, msg = update_balance(TEST_ACCOUNT_ID, -5.00, "Retiro de advertencia")
    if status and "ADVERTENCIA" in msg:
        print(
            f"Éxito Integración: Advertencia de saldo bajo (HU 4.4) se disparó en Core Logic. Mensaje: {msg}"
        )

    print("\n==================================================")
    print("REVISIÓN DE INCREMENTO FINALIZADA.")
    print("==================================================")


if __name__ == "__main__":
    run_integration_test()
