import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from app.core.security.middlewares import VerificarOrigenMiddleware
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def configurar_cors(app: FastAPI):
    entorno = os.getenv("ENTORNO", "local").lower()
    
    if entorno == "local":
        origenes_permitidos = [
            "http://localhost",
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://localhost:3000"
        ]
        hosts_permitidos = ["localhost", "127.0.0.1", "*"]
        print("  -> CORS configurado para entorno: LOCAL")
    else:
        frontend_url = os.getenv("FRONTEND_URL", "*")
        origenes_permitidos = [frontend_url]
        # Extraer el host para TrustedHostMiddleware
        host_url = frontend_url.replace("https://", "").replace("http://", "").split("/")[0]
        hosts_permitidos = [host_url, "*"] if host_url != "*" else ["*"]
        print(f"  -> CORS configurado para entorno: PRODUCCIÓN (Origen: {frontend_url})")

    # Middleware 1: Bloqueo estricto de orígenes no permitidos (Modular)
    app.add_middleware(VerificarOrigenMiddleware)

    # Middleware 2: Gestión de cabeceras CORS nativa
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origenes_permitidos,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    
    # Middleware 3: Seguridad contra Host Header Injection
    app.add_middleware(
        TrustedHostMiddleware, 
        allowed_hosts=hosts_permitidos
    )