users_db = {
    [
  {
    "id": "A1001",
    "owner": "Maria Garcia",
    "balance": 1500.5,
    "transactions": [
      {
        "date": "2025-10-25",
        "amount": -200.0,
        "description": "Compra Amazon"
      },
      {
        "date": "2025-10-28",
        "amount": 500.0,
        "description": "Deposito Salario"
      }
    ]
  },
  {
    "id": "B2002",
    "owner": "Juan Perez",
    "balance": 50.0,
    "transactions": []
  }
]
}

MIN_BALANCE = 50.0



#  FUNCIONES BASE


def get_user(user_id):
    """Obtiene un usuario o devuelve None si no existe."""
    return users_db.get(user_id)


def update_balance(user_id, new_balance):
    """Actualiza el balance principal."""
    users_db[user_id]["balance"] = new_balance

#  DEPOSITAR A META DE AHORRO

def deposit_to_goal(user_id, amount):
    user = get_user(user_id)
    if not user:
        return {"error": "Usuario no encontrado"}
    if amount <= 0:
        return {"error": "El monto debe ser mayor a 0"}
    if user["balance"] < amount:
        return {"error": "Fondos insuficientes"}

    goal = user["savings_goal"]
    restante = goal["target"] - goal["current"]
    if amount > restante:
        return {"error": f"El monto excede la meta. Máximo: ${restante:.2f}"}

    # Actualizar datos
    goal["current"] += amount
    update_balance(user_id, user["balance"] - amount)
    return {"ok": f"Depositaste ${amount:.2f} a tu meta", "ahorro": goal["current"], "balance": user["balance"]}



#  VERIFICAR META DE AHORRO


def check_goal_achieved(user_id):
    user = get_user(user_id)
    if not user:
        return {"error": "Usuario no encontrado"}
    goal = user["savings_goal"]
    return goal["current"] >= goal["target"]



#  REGLA DE BALANCE MÍNIMO


def check_minimum_balance_rule(balance, amount):
    """Valida que el retiro no deje el balance menor al mínimo permitido."""
    new_balance = balance - amount
    if new_balance < MIN_BALANCE:
        return {"error": f"El balance no puede ser menor a ${MIN_BALANCE:.2f} (quedaría en ${new_balance:.2f})"}
    return {"ok": new_balance}


#  RETIRO

def withdraw_money(user_id, amount):
    user = get_user(user_id)
    if not user:
        return {"error": "Usuario no encontrado"}
    if amount <= 0:
        return {"error": "El monto debe ser mayor a 0"}
    if user["balance"] < amount:
        return {"error": "Fondos insuficientes"}

    # Aplicar regla de saldo mínimo
    rule = check_minimum_balance_rule(user["balance"], amount)
    if "error" in rule:
        return rule

    update_balance(user_id, rule["ok"])
    return {"ok": f"Retiro de ${amount:.2f} exitoso", "balance": rule["ok"]}

