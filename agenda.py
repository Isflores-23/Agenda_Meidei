import streamlit as st
import json
import os
import base64
from datetime import datetime, date
import calendar

ARCHIVO = "mi_libreta_meidei.json"
LOGO_EMPRESA = "logo_meidei.png"
FOTO_JEFE = "foto_jefe.png"

def cargar_datos():
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def guardar_datos(pendientes):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(pendientes, f, ensure_ascii=False, indent=4)

def obtener_base64_imagen(ruta_imagen):
    if os.path.exists(ruta_imagen):
        with open(ruta_imagen, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            return f"data:image/png;base64,{encoded}"
    return ""

st.set_page_config(page_title="Grupo Meidei | Agenda Directiva", page_icon="🔴", layout="wide")

# --- ESTILOS PROFESIONALES (ROJO CARMÍN Y BLANCO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }
    .stApp {
        background-color: #F8F9FA;
    }
    
    .main p, .main span, .main label {
        color: #1F2937 !important;
    }

    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] span, 
    section[data-testid="stSidebar"] label, 
    section[data-testid="stSidebar"] div {
        color: #FFFFFF !important;
    }
    
    section[data-testid="stSidebar"] input, 
    section[data-testid="stSidebar"] select,
    section[data-testid="stSidebar"] div[data-baseweb="select"] span {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

    .sidebar-logo-container {
        text-align: center;
        padding: 5px 0;
        margin-bottom: 5px;
    }
    .sidebar-logo-container img {
        max-width: 160px;
        height: auto;
        object-fit: contain;
    }

    .badge-card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 8px;
        padding: 12px 14px;
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 10px;
    }
    .badge-avatar-container {
        width: 55px;
        height: 55px;
        min-width: 55px;
        border-radius: 50%;
        border: 2px solid #9B111E;
        overflow: hidden;
        background-color: #111;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .badge-avatar-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .badge-info {
        display: flex;
        flex-direction: column;
    }
    .badge-label {
        font-size: 0.65rem;
        font-weight: 700;
        color: #9CA3AF !important;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .badge-name {
        font-size: 0.9rem;
        font-weight: 700;
        color: #FFFFFF !important;
        margin-top: 1px;
    }

    .erp-header {
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-top: 4px solid #9B111E;
        padding: 24px 30px;
        border-radius: 10px;
        margin-bottom: 25px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .erp-title {
        color: #111827 !important;
        font-size: 1.75rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .erp-subtitle {
        color: #6B7280 !important;
        font-size: 0.9rem;
        margin-top: 4px;
    }

    .stButton>button {
        border-radius: 6px;
        font-weight: 600;
        border: none;
        background-color: #9B111E;
        color: white !important;
        transition: background 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #7A0D17;
        color: white !important;
    }

    div[data-testid="metric-container"] {
        background-color: #FFFFFF !important;
        border: 1px solid #E5E7EB !important;
        padding: 16px !important;
        border-radius: 8px !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.01) !important;
    }
    div[data-testid="metric-container"] label {
        color: #6B7280 !important;
        font-size: 0.85rem !important;
    }
    div[data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: #111827 !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }
    
    h3 {
        color: #111827 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- PANEL LATERAL DE CONTROL ---
with st.sidebar:
    # 1. Logo de la Empresa
    logo_base64 = obtener_base64_imagen(LOGO_EMPRESA)
    if logo_base64:
        st.markdown(f"""
            <div class="sidebar-logo-container">
                <img src="{logo_base64}" alt="Grupo Meidei Logo">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='text-align: center; margin-bottom: 0px;'>
                <h3 style='font-weight: 700; color: #FFFFFF; margin-bottom: 0px;'>GRUPO MEIDEI</h3>
                <p style='color: #9CA3AF; font-size: 0.8rem; margin-top: 2px;'>MÓDULO EJECUTIVO</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    # 2. Foto y Credencial del Jefe
    foto_base64 = obtener_base64_imagen(FOTO_JEFE)
    foto_tag = f'<img src="{foto_base64}">' if foto_base64 else '<div style="color: #9B111E; font-size: 0.55rem; text-align: center; font-weight: bold;">Sin Foto</div>'

    st.markdown(f"""
        <div class="badge-card">
            <div class="badge-avatar-container">
                {foto_tag}
            </div>
            <div class="badge-info">
                <span class="badge-label">Dirección General</span>
                <span class="badge-name">Grupo Meidei</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📅 Fecha del Pendiente")
    
    hoy = datetime.today()
    anio_actual = hoy.year
    
    col_y, col_m, col_d = st.columns(3)
    with col_y:
        anos_disponibles = list(range(2020, 2071))
        default_idx = anos_disponibles.index(anio_actual) if anio_actual in anos_disponibles else 0
        anio_sel = st.selectbox("Año", anos_disponibles, index=default_idx)
    with col_m:
        meses_lista = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
        mes_sel_str = st.selectbox("Mes", options=meses_lista, index=hoy.month-1)
        mes_sel = meses_lista.index(mes_sel_str) + 1
    with col_d:
        _, ultimo_dia = calendar.monthrange(anio_sel, mes_sel)
        dias_disponibles = list(range(1, ultimo_dia + 1))
        dia_default = min(hoy.day, ultimo_dia) - 1
        dia_sel = st.selectbox("Día", options=dias_disponibles, index=dia_default)

    fecha_seleccionada = date(anio_sel, mes_sel, dia_sel)

    st.markdown("---")
    st.markdown("#### 📝 Nuevo Pendiente")
    
    with st.form("form_erp", clear_on_submit=True):
        titulo_tarea = st.text_input("Asunto / Directriz")
        categoria_sel = st.selectbox("Clasificación", ["Juntas", "Pagos pendientes", "Nóminas"])
        
        c_hora, c_prio = st.columns(2)
        with c_hora:
            hora_sel = st.time_input("Hora", value=datetime.now().time())
        with c_prio:
            prioridad_sel = st.selectbox("Prioridad", ["Alta", "Media", "Baja"])
            
        btn_guardar = st.form_submit_button("Registrar en Sistema", use_container_width=True)
        
        if btn_guardar:
            if not titulo_tarea.strip():
                st.warning("Ingrese una descripción válida.")
            else:
                db = cargar_datos()
                db.append({
                    "titulo": titulo_tarea,
                    "categoria": categoria_sel,
                    "fecha": fecha_seleccionada.strftime("%Y-%m-%d"),
                    "hora": hora_sel.strftime("%H:%M"),
                    "prioridad": prioridad_sel,
                    "completado": False
                })
                guardar_datos(db)
                st.success("¡Operación registrada con éxito!")
                st.rerun()

# --- VISTA PRINCIPAL (DASHBOARD) ---
st.markdown("""
    <div class="erp-header">
        <p class="erp-title">🔴 Grupo Meidei — Panel Directivo</p>
        <p class="erp-subtitle">Sistema de control de Juntas, Pagos pendientes, Nóminas y seguimiento ejecutivo.</p>
    </div>
""", unsafe_allow_html=True)

registros = cargar_datos()

total_reg = len(registros)
activos_reg = sum(1 for r in registros if not r["completado"])
criticos_reg = sum(1 for r in registros if r["prioridad"] == "Alta" and not r["completado"])

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Total Registros", total_reg)
with m2:
    st.metric("Pendientes", activos_reg)
with m3:
    st.metric("Urgencias Críticas", criticos_reg)

st.markdown("---")

col_v1, col_v2 = st.columns([0.4, 0.6])
with col_v1:
    st.subheader("📋 Agenda de Operaciones")
with col_v2:
    opciones_vista = ["Ver Todos los Días (Organizados por Fecha)", "Ver un Día Específico"]
    modo_visualizacion = st.selectbox("Agrupar / Filtrar vista", options=opciones_vista, index=0)

if not registros:
    st.info("La base de datos institucional se encuentra vacía. Comienza registrando un pendiente en el panel izquierdo.")
else:
    if modo_visualizacion == "Ver un Día Específico":
        st.markdown("---")
        fecha_filtro_usuario = st.date_input("Selecciona el día que deseas consultar:", value=fecha_seleccionada)
        fecha_str = fecha_filtro_usuario.strftime("%Y-%m-%d")
        
        filtrados = [(idx, r) for idx, r in enumerate(registros) if r["fecha"] == fecha_str]
        
        pendientes_dia = sum(1 for _, r in filtrados if not r["completado"])
        completados_dia = sum(1 for _, r in filtrados if r["completado"])
        
        st.info(f"📊 Resumen para el **{fecha_str}**: **{pendientes_dia} pendientes** | **{completados_dia} completados** (Total: {len(filtrados)} actividades)")
        
        if not filtrados:
            st.warning(f"No hay actividades registradas para el día {fecha_str}.")
        else:
            filtrados = sorted(filtrados, key=lambda x: x[1]["hora"])
            
            for idx, r in filtrados:
                color_borde = "#9B111E" if r["prioridad"] == "Alta" else "#D97706" if r["prioridad"] == "Media" else "#059669"
                cat = r.get("categoria", "Juntas")
                
                st.markdown(f"""
                    <div style="background-color: #FFFFFF; border: 1px solid #E5E7EB; border-left: 5px solid {color_borde}; padding: 14px 18px; border-radius: 6px; margin-bottom: 10px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 0.75rem; font-weight: 700; color: {color_borde};">PRIORIDAD {r['prioridad'].upper()} &nbsp;|&nbsp; 📁 {cat}</span>
                            <span style="font-size: 0.85rem; color: #4B5563; font-weight: 600;">⏰ {r['hora']} hrs</span>
                        </div>
                        <div style="font-size: 1.05rem; font-weight: 500; color: #1F2937;">
                            {'~~' + r['titulo'] + '~~' if r['completado'] else r['titulo']}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                c_chk, c_del = st.columns([0.9, 0.1])
                with c_chk:
                    estado_cambio = st.checkbox("Completado", value=r["completado"], key=f"chk_esp_{idx}")
                    if estado_cambio != r["completado"]:
                        registros[idx]["completado"] = estado_cambio
                        guardar_datos(registros)
                        st.rerun()
                with c_del:
                    if st.button("🗑️", key=f"del_esp_{idx}", help="Eliminar"):
                        registros.pop(idx)
                        guardar_datos(registros)
                        st.rerun()
                st.write("")
                
    else:
        st.markdown("---")
        
        registros_ordenados = sorted(list(enumerate(registros)), key=lambda x: (x[1]["fecha"], x[1]["hora"]))
        fechas_unicas = sorted(list(set(r["fecha"] for _, r in registros_ordenados)))
        
        for fecha in fechas_unicas:
            items_del_dia = [(idx, r) for idx, r in registros_ordenados if r["fecha"] == fecha]
            pendientes_fecha = sum(1 for _, r in items_del_dia if not r["completado"])
            total_fecha = len(items_del_dia)
            
            st.markdown(f"### 📅 Fecha: {fecha} &nbsp;&nbsp;|&nbsp;&nbsp; <span style='font-size:0.9rem; color:#6B7280;'>📌 Pendientes: <b>{pendientes_fecha}</b> de {total_fecha} total</span>", unsafe_allow_html=True)
            
            for idx, r in items_del_dia:
                color_borde = "#9B111E" if r["prioridad"] == "Alta" else "#D97706" if r["prioridad"] == "Media" else "#059669"
                cat = r.get("categoria", "Juntas")
                
                st.markdown(f"""
                    <div style="background-color: #FFFFFF; border: 1px solid #E5E7EB; border-left: 5px solid {color_borde}; padding: 14px 18px; border-radius: 6px; margin-bottom: 8px;">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                            <span style="font-size: 0.75rem; font-weight: 700; color: {color_borde};">PRIORIDAD {r['prioridad'].upper()} &nbsp;|&nbsp; 📁 {cat}</span>
                            <span style="font-size: 0.85rem; color: #4B5563; font-weight: 600;">⏰ {r['hora']} hrs</span>
                        </div>
                        <div style="font-size: 1.05rem; font-weight: 500; color: #1F2937;">
                            {'~~' + r['titulo'] + '~~' if r['completado'] else r['titulo']}
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                c_chk, c_del = st.columns([0.9, 0.1])
                with c_chk:
                    estado_cambio = st.checkbox("Completado", value=r["completado"], key=f"chk_gen_{idx}")
                    if estado_cambio != r["completado"]:
                        registros[idx]["completado"] = estado_cambio
                        guardar_datos(registros)
                        st.rerun()
                with c_del:
                    if st.button("🗑️", key=f"del_gen_{idx}", help="Eliminar"):
                        registros.pop(idx)
                        guardar_datos(registros)
                        st.rerun()
                        
            st.markdown("---")