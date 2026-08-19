# 🌙 Tsukuyomi Master System

![Tsukuyomi](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
![Clean Architecture](https://img.shields.io/badge/Architecture-Clean-orange.svg)

Tsukuyomi es una aplicación web diseñada para la **Sincronización Multidía de Actividades**. Actúa como un santuario personal y planificador de "rituales" (tareas, universidad, deportes, etc.) permitiendo organizar rutinas semanales de manera visual y estructurada.

## ✨ Características Principales

*   **Sincronización Multidía:** Programa una misma actividad para múltiples días de la semana de una sola vez.
*   **Visualización Intuitiva:** Interfaz organizada por pestañas para cada día de la semana, con tarjetas de colores basadas en categorías.
*   **Seguridad:** Acceso protegido mediante contraseña maestra.
*   **Almacenamiento Híbrido:** Soporte dual para bases de datos:
    *   `SQLite` (Ideal para desarrollo local).
    *   `Supabase` (PostgreSQL) para entornos en producción.
*   **Balance de Energías:** Gráfico analítico para visualizar en qué categorías inviertes más tu tiempo.
*   **Notificaciones:** Integración con servicios de Telegram para recordatorios (infraestructura lista).

## 🏗️ Arquitectura

El proyecto está diseñado bajo los principios de **Clean Architecture**, dividiendo las responsabilidades en capas claras para favorecer la escalabilidad y el testing:

```text
src/
├── domain/           # Entidades centrales y puertos (Interfaces)
├── application/      # Casos de uso (Lógica de negocio)
└── infrastructure/   # Implementaciones concretas (Adapters de BD, APIs externas)
```

## 🚀 Instalación y Uso Local

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. **Clonar el repositorio** (si aplica) o ubicarse en la carpeta del proyecto.
2. **Crear un entorno virtual** (Opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```
3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configurar variables de entorno:**
   Copia el archivo `.env.example` a `.env` y configura tus variables:
   ```env
   APP_PASSWORD=tu_contraseña_maestra
   DB_ADAPTER=local  # o "supabase"
   
   # Si usas Supabase:
   SUPABASE_URL=tu_supabase_url
   SUPABASE_KEY=tu_supabase_key
   
   # Para notificaciones de Telegram:
   TELEGRAM_BOT_TOKEN=tu_token
   TELEGRAM_CHAT_ID=tu_chat_id
   ```
5. **Ejecutar la aplicación:**
   ```bash
   streamlit run app.py
   ```

## 🛠️ Tecnologías Utilizadas

*   **Frontend & Web Framework:** [Streamlit](https://streamlit.io/)
*   **Backend:** Python
*   **Bases de Datos:** SQLite (Local) / Supabase (Nube)
*   **Calidad de Código & CI/CD:** GitHub Actions, SonarCloud, Snyk

---
*«Organiza tus ciclos, domina tu tiempo.»*
