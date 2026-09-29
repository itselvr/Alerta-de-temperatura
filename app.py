import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Mini Sistema Experto Clima", page_icon="🌤️☀️⛈️")

st.title("🌤️ Mini Sistema Experto — Clima")
st.write("Clasificación de condiciones climáticas y alertas de calor.")

# 1. Entrada de datos desde el menú lateral
st.sidebar.header("Parámetros de Medición")

temp_input = st.sidebar.number_input("Temperatura (°C)", value=31, step=1)
hum_input = st.sidebar.number_input("Humedad (%)", value=68, min_value=0, max_value=100, step=1)
llueve_input = st.sidebar.checkbox("¿Está lloviendo?", value=False)

# Guardar en la lista solicitada
medicion = [temp_input, hum_input, llueve_input]

# 2. Extraer valores desde la lista
temperatura, humedad, llueve = medicion

# 3. Clasificación de condiciones
if temperatura >= 30 and humedad >= 70:
    clasificacion = "Calor húmedo"
elif temperatura >= 30 and humedad < 70:
    clasificacion = "Calor seco"
elif 15 <= temperatura < 30 and llueve:
    clasificacion = "Templado lluvioso"
elif 15 <= temperatura < 30 and not llueve:
    clasificacion = "Templado"
else:
    clasificacion = "Frío"

# 4. Alerta de calor
alerta = temperatura >= 35 and humedad >= 70

# 5. Visualización de resultados en la app mediante f-strings
st.subheader("📊 Resultados de la Medición")

texto_lluvia = "Sí" if llueve else "No"
st.write(f"**Datos recibidos:** {temperatura}°C | {humedad}% Humedad | Lluvia: **{texto_lluvia}**")
st.write(f"**Clasificación del clima:** `{clasificacion}`")

if alerta:
    st.error("⚠️ **ALERTA POR CALOR ACTIVADA:** Existe riesgo por altas temperaturas y humedad.")
else:
    st.success("✅ **Alerta por calor:** No activa.")
