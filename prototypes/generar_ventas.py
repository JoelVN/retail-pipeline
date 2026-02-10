import pandas as pd
import random
import os
from datetime import datetime,timedelta
from tqdm import tqdm

## Preparar capa bronze 
if not os.path.exists('data'):
    os.makedirs('data')

## definir dimensiones del negocio
productos = ['Laptop','Mouse','Teclado','Monitor','Webcamp']
tiendas = ['Quito-Centro', 'Guayaquil-Sur','Cuenca-Norte','Manta-Puerto']

data = []

## Bucle para generar 100 transacciones 
for i in tqdm(range(1,101), desc="Generando Ventas"):
    ## Fecha aleatoria
    fecha = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d %H:%M:%S")
    data.append({
        "transaction_id": f"TRX-{i:03d}",
        "timestamp": fecha,
        "product": random.choice(productos),
        "amount": round(random.uniform(10.5,1200.0),2),
        "store": random.choice(tiendas),
        "status": random.choice(['Completed','Completed','Failed'])
    })
    if i % 10 == 0:
        print(f"⏳ Procesando... {i}% completado")

df = pd.DataFrame(data)
df.to_csv("data/ventas_raw.csv", index=False)

print("---")
print("✅ Capa Bronze Creada!")
print("Se generó el archivo: data/ventas_raw.csv")
print("---")