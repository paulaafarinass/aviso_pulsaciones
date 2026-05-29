import streamlit as st
import plotly.express as px
import time
from sensor_pulsaciones import sensor_p
from sensor_movimiento import sensor_m

if 'monitor_encendido' not in st.session_state:
    st.session_state.monitor_encendido = False
    
if 'historial_pulsos' not in st.session_state: 
    st.session_state.historial_pulsos = []


col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("▶️ Iniciar Monitor"):
        st.session_state.monitor_encendido = True 

with col_btn2:
    if st.button("⏹️ Detener Monitor"):
        st.session_state.monitor_encendido = False
        st.session_state.historial_pulsos = []

st.markdown("---")

st.title('🏥 Monitorización cardíaca en tiempo real')
st.header('Paciente-1')

col1, col2 = st.columns(2)
pulso = col1.empty()
indicador_movimiento = col2.empty()
alerta = st.empty()
grafica_f_cardiaca = st.empty()

if st.session_state.monitor_encendido == True:
    pulsaciones=sensor_p()
    movimiento=sensor_m()
            
    pulso.metric(label="♥ Frecuencia Cardíaca", value=f'{pulsaciones} lpm')
        
    estado_mov = "Sí" if movimiento == 1 else "No"
    indicador_movimiento.metric(label="Movimiento detectado:",value=estado_mov)
    
    st.session_state.historial_pulsos.append(pulsaciones)
    
    if len(st.session_state.historial_pulsos) > 50:
        st.session_state.historial_pulsos.pop(0)
    
    fig = px.line(
        y=st.session_state.historial_pulsos, 
        title="📈 Frecuencia cardíaca en tiempo real",
        labels={"y": "Frecuencia cardíaca (LPM)", "index": "Tiempo (s)"} 
    )
    
    fig.update_traces(line_color='#FF4B4B') 
    
    grafica_f_cardiaca.plotly_chart(fig, use_container_width=True)

    if pulsaciones==0:
        alerta.error('🚨 PARADA CARDíACA')
    elif pulsaciones>60 and pulsaciones<=100:
        alerta.success("🟢 Paciente Estable")
    else:
        if movimiento==1:
            alerta.warning("⚠ Se ha detectado movimiento. Revisar sensores.")
        else:
            alerta.error('🔴 ALERTA MÉDICA. Ritmo irregular detectado')
                
    time.sleep(1)
    st.rerun()
else:
    st.info('Monitor apagado ⏸')


