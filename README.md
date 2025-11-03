# Abrahamco-uacj

Este proyecto simula un desarrollo ágil utilizando el *framework* **SCRUM** y el flujo de trabajo profesional de **Git y GitHub**. Cada equipo es responsable de implementar un **Feature** clave del sistema bancario digital.


## Configuración del Entorno de Desarrollo

Para trabajar en este proyecto, solo necesitas **Python 3.x**.

1.  **Clonar el Repositorio (Fork):**
      * Cada lider de equipo debe crear un **Fork** de este repositorio en su propia cuenta de GitHub.
      * Una vez hecho el *fork*, los miembros del equipo deben clonarlo a su máquina local:
        ```bash
        git clone [URL_DE_TU_FORK]
        cd banco_agil
        ```
2.  **Estructura de Archivos Clave:**
      * **`data/accounts.json`**: Base de datos simulada. Contiene datos de prueba.
      * **`src/data_manager.py`**: Funciones de lectura/escritura de JSON. **NO MODIFICAR.**
      * **`src/core_logic.py`**: Contiene la función crítica `update_balance`. **Solo el Equipo 2 debe modificarla.**
      * **`test_data.py`**: Archivo de **Mocking** para pruebas aisladas.

-----

## Flujo de Trabajo y Contribución con Git

El equipo trabajara como se organice en el fork de su equipo

### A. Preparación (Crear la Branch)

Antes de empezar a codificar las Historias de Usuario (HU), crearan una nueva rama (branch) para el trabajo del equipo (Epic), a esa branch se mezclara todo el trabajo que desarrolle el equipo.

```bash
# 1. Asegúrate de estar en la rama principal de tu fork
git checkout main

# 2. Crea y cambia a la rama de tu equipo
# (Usa un nombre claro: ej. 'feature/team-1-onboarding')
git checkout -b feature/equipo-[NUMERO]-[NOMBRE_FEATURE]
```

### B. Implementación (Codificación)

1.  Abre el archivo `.py` asignado a tu equipo (Ej: `src/modules/mod_cards.py`).
2.  Implementa la lógica dentro de las **funciones con anotaciones de tipado** que te fueron asignadas en el *Sprint Planning*.
3.  **Realiza Pruebas Aisladas:** Usa el bloque `if __name__ == '__main__':` en tu módulo y el archivo `test_data.py` para verificar que tu lógica funcione sin interactuar con los archivos de otros equipos.

### C. Finalización y Colaboración (Pull Request)

Una vez que el equipo ha completado y probado **todas las Historias de Usuario** de su *Feature*:

1.  **Guarda los Cambios:**
    ```bash
    git add .
    git commit -m "feat: Implementacion completa de [NOMBRE_FEATURE] (EPIC-[NUMERO])"
    ```
2.  **Sube los Cambios a tu Fork:**
    ```bash
    git push origin feature/equipo-[NUMERO]-[NOMBRE_FEATURE]
    ```
3.  **Crea el Pull Request (PR):**
      * Ve a la página de tu **Fork** en GitHub.
      * Crea un **Pull Request (PR)** de tu nueva *branch* hacia la *branch* `main` del **repositorio original de la clase**.
      * Incluye el **número de Épica** y las **HUs completadas** en la descripción del PR.

-----

## ⚠️ 4. Reglas de Integración

  * **No Modificar:** Los archivos `src/data_manager.py` y `main.py` son solo de lectura/ejecución para los equipos de desarrollo.
  * **Conflictos:** Si tu trabajo requiere la lógica de otro equipo (Ej: el Equipo 6 necesita la función `update_balance`), debes **importar y llamar** a esa función; **nunca copiar y pegar** el código.
  * **Commit Message:** Usa un mensaje claro para tus *commits* siguiendo la convención: `tipo: Descripción (ej. feat: nueva funcionalidad, fix: corrección de bug)`.
