import kagglehub 
import os
import shutil 

def descargar_dataset():
    
    destino = "data/"

    if not os.path.exists(destino):
        os.makedirs(destino)
        print(f"📂 Carpeta '{destino}' creada.")

    print("⏳ Iniciando descarga desde kaggle...")
    path_temporal = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

    print(f"📍 Los archivos se descargaron temporalmente en: {path_temporal} ")

    archivos = os.listdir(path_temporal)

    for nombre in archivos:
        # Creamos la ruta completa de origen y de destino
        origen_completo = os.path.join(path_temporal, nombre)
        destino_completo = os.path.join(destino, nombre)

        # 3. Movemos el archivo
        shutil.move(origen_completo, destino_completo)
        print(f"🚚 Movido: {nombre}")

    print(f"✅ ¡Listo! Todos los archivos están en: {destino}")

if __name__ == "__main__":
    descargar_dataset()