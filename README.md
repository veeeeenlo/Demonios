# Demonios
Diseño e Implementación de un Sistema Tolerante a Fallas mediante Demonios (Servicios) para revisar el estado de tu app (Estatus)

# Objetivo:
Diseñar e implementar un  que funcione en segundo plano y que forme parte de una aplicación tolerante a fallas.

# Problema: 
Un proceso crítico puede entrar en un "Bucle Infinito" o "Deadlock". En estos casos, el proceso sigue existiendo en el sistema operativo (tiene un PID), pero no está trabajando. Un monitor simple fallaría al detectarlo.
# Estrategia de Tolerancia: Heartbeat por Archivo/Señal. 
El proceso A actualiza un timestamp en un archivo temporal cada 2 segundos. El Demonio B revisa que ese timestamp no sea mayor a 5 segundos.
# Estrategia de Recuperación: Fail-Stop and Restart. 
Si el latido se detiene, el Demonio mata el proceso colgado (por si acaso) y lanza una nueva instancia limpia.
