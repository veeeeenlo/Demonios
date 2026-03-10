import subprocess
import time
import os
import logging

logging.basicConfig(filename='tolerancia.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

HEARTBEAT_FILE = ".heartbeat"
TIMEOUT = 6  # Segundos máximos sin latido antes de considerar falla

class FaultTolerantMonitor:
    def __init__(self):
        self.proceso = None

    def iniciar_proceso(self):
        logging.info("Iniciando Proceso A...")
        self.proceso = subprocess.Popen(['python', 'proceso_a.py'])
        # Inicializamos el latido para evitar falsos positivos al arranque
        with open(HEARTBEAT_FILE, "w") as f:
            f.write(str(time.time()))

    def ejecutar(self):
        self.iniciar_proceso()
        
        while True:
            time.sleep(3)
            ahora = time.time()
            
            try:
                with open(HEARTBEAT_FILE, "r") as f:
                    ultimo_latido = float(f.read())
                
                # REGLA DE TOLERANCIA
                if ahora - ultimo_latido > TIMEOUT:
                    logging.error("Falla detectada: El proceso A dejó de enviar latidos.")
                    self.recuperar()
                else:
                    print(f"Sincronización OK. Latido hace {round(ahora-ultimo_latido, 2)}s")
                    
            except FileNotFoundError:
                logging.warning("Archivo de latido no encontrado. Reiniciando...")
                self.recuperar()

    def recuperar(self):
        logging.info("Ejecutando estrategia de recuperación (Reinicio)...")
        if self.proceso:
            self.proceso.kill() # Asegurar que el proceso viejo muera
        self.iniciar_proceso()

if __name__ == "__main__":
    monitor = FaultTolerantMonitor()
    monitor.ejecutar()
