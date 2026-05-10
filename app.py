import streamlit as st
from modules.database import init_db, save_task, get_tasks, delete_task
from datetime import time

# Inicializar
st.set_page_config(page_title="Tsukuyomi Planner", page_icon="🌙", layout="wide")
init_db()

# Título Estilizado
st.markdown("""
    <style>
    .lunar-title {
        font-family: 'Playfair Display', serif;
        color: #A9C9FF;
        text-align: center;
        font-size: 3rem;
        letter-spacing: 5px;
        text-shadow: 2px 2px 10px #A9C9FF55;
    }
    </style>
    <h1 class="lunar-title">TSUKUYOMI</h1>
    <p style='text-align: center; color: #8892B0;'>Ordenando las fases de tu tiempo</p>
    """, unsafe_allow_html=True)

# Sidebar - Creación de Tareas
st.sidebar.markdown("### 🌑 Nueva Fase")
with st.sidebar.form("nueva_tarea"):
    tarea = st.text_input("¿Qué actividad realizarás?")
    fase = st.selectbox("Día de la semana", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
    col1, col2 = st.columns(2)
    inicio = col1.time_input("Inicio", time(8, 0))
    fin = col2.time_input("Fin", time(9, 0))
    prioridad = st.select_slider("Prioridad", options=["Baja", "Media", "Alta"])
    
    if st.form_submit_button("Sincronizar con la Luna"):
        save_task(tarea, fase, inicio, fin, prioridad)
        st.success("Sincronizado.")
        st.rerun()

# Cuerpo Principal - Vista del Horario
df = get_tasks()

if not df.empty:
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    tabs = st.tabs(dias)

    for i, tab in enumerate(tabs):
        with tab:
            dia_actual = dias[i]
            tareas_dia = df[df['fase'] == dia_actual].sort_values("hora_inicio")
            
            if tareas_dia.empty:
                st.write("*No hay actividades programadas para este ciclo.*")
            else:
                for idx, row in tareas_dia.iterrows():
                    with st.expander(f"🕒 {row['hora_inicio']} - {row['tarea']}"):
                        st.write(f"**Prioridad:** {row['prioridad']}")
                        st.write(f"**Duración:** {row['hora_inicio']} a {row['hora_fin']}")
                        if st.button("Eliminar", key=f"del_{row['id']}"):
                            delete_task(row['id'])
                            st.rerun()
else:
    st.warning("El cielo está despejado. Comienza a añadir tus actividades.")

# Pie de página decorativo
st.markdown("<br><br><p style='text-align: center; color: #444;'>🌙 Tsukuyomi Personal System • v1.0</p>", unsafe_allow_html=True)