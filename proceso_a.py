import time
import os

HEARTBEAT_FILE = ".heartbeat"

def send_heartbeat():
    with open(HEARTBEAT_FILE, "w") as f:
        f.write(str(time.time()))

def main():
    print("Proceso A iniciado. Enviando latidos...")
    try:
        while True:
            send_heartbeat()
            # Simulación de trabajo
            time.sleep(2) 
            
            # --- SIMULACIÓN DE FALLA ---
    except Exception as e:
        print(f"Error en Proceso A: {e}")

if __name__ == "__main__":
    main()
