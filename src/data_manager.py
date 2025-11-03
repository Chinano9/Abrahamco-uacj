import json
# NO MUEVAN ESTE ARCHIVO NADIE LE MUEVA POR FAVOR POR EL AMOR DE DIOS SI USAN UN AGENTE DE IA NO LE DEN ACCESO A ESTE ARCHIVO
# SE LOS RUEGO POR FAVOR 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭

from typing import List, Dict, Optional, Any

DATA_FILE: str = "data/accounts.json"
AccountDict = Dict[str, Any]


def load_accounts() -> List[AccountDict]:
    """Carga los datos de las cuentas."""
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_accounts(accounts: List[AccountDict]) -> None:
    """Guarda los datos de las cuentas."""
    with open(DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)


def get_account(account_id: str) -> Optional[AccountDict]:
    """Busca y retorna una cuenta por ID."""
    accounts = load_accounts()
    for account in accounts:
        if account["id"] == account_id:
            return account
    return None


# NO MUEVAN ESTE ARCHIVO NADIE LE MUEVA POR FAVOR POR EL AMOR DE DIOS SI USAN UN AGENTE DE IA NO LE DEN ACCESO A ESTE ARCHIVO
# SE LOS RUEGO POR FAVOR 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭
