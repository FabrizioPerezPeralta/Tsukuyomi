import streamlit as st
from modules.database import init_db, agregar_actividad, obtener_datos, borrar_dato
from datetime import time

# Configuración inicial
st.set_page_config(page_title="Tsukuyomi System", page_icon="🌙", layout="wide")
init_db()

# Estilo para los colores de las categorías
CAT_COLORS = {
    "Asignatura Universidad": "#4A90E2", # Azul saber
    "Tarea": "#9B59B6",               # Púrpura deber
    "Espacio Libre": "#BDC3C7",         # Gris calma (Luna)
    "Deporte": "#E67E22",               # Naranja energía
    "Producción": "#2ECC71"             # Verde creación
}

st.markdown("<h1 style='text-align: center; color: #A9C9FF;'>月読 TSUKUYOMI</h1>", unsafe_allow_html=True)

# Sidebar para ingresar datos
st.sidebar.markdown("### 🌑 Nueva Fase del Día")
with st.sidebar.form("form_luna"):
    act = st.text_input("Nombre de la Actividad")
    fase = st.selectbox("Día", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
    
    # NUEVAS CATEGORÍAS
    cat = st.selectbox("Tipo de Actividad", [
        "Asignatura Universidad", 
        "Tarea", 
        "Espacio Libre", 
        "Deporte", 
        "Producción"
    ])
    
    c1, c2 = st.columns(2)
    t_in = c1.time_input("Inicio", time(8, 0))
    t_fn = c2.time_input("Fin", time(9, 0))
    
    if st.form_submit_button("Sincronizar con Tsukuyomi"):
        if act:
            agregar_actividad(act, fase, t_in, t_fn, cat)
            st.success(f"'{act}' registrado.")
            st.rerun()

# Visualización por pestañas
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
tabs = st.tabs([f"🌙 {d}" for d in dias])
df = obtener_datos()

for i, tab in enumerate(tabs):
    with tab:
        dia_nombre = dias[i]
        if not df.empty:
            tareas = df[df['fase'] == dia_nombre].sort_values("inicio")
            if tareas.empty:
                st.info("No hay actividades programadas para este ciclo.")
            else:
                for _, row in tareas.iterrows():
                    # Crear una fila con diseño limpio
                    color = CAT_COLORS.get(row['categoria'], "#FFF")
                    
                    with st.container():
                        col_info, col_btn = st.columns([0.85, 0.15])
                        
                        with col_info:
                            # Badge de color según categoría
                            st.markdown(f"""
                                <div style="border-left: 5px solid {color}; padding-left: 15px; margin-bottom: 10px;">
                                    <span style="color: {color}; font-weight: bold; font-size: 0.8rem;">{row['categoria'].upper()}</span><br>
                                    <span style="font-size: 1.2rem; color: #E0E0E0;">{row['inicio']} - {row['fin']} | <b>{row['actividad']}</b></span>
                                </div>
                            """, unsafe_allow_html=True)
                        
                        with col_btn:
                            st.write("") # Espaciador
                            if st.button("Eliminar", key=f"del_{row['id']}"):
                                borrar_dato(row['id'])
                                st.rerun()
        else:
            st.write("El cielo está despejado. Añade tu primera actividad en el panel izquierdo.")