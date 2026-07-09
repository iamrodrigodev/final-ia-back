import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
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

    @app.middleware("http")
    async def verificar_origen(request: Request, call_next):
        origen = request.headers.get("origin")
        # Validar si viene un origin y si no está en la lista blanca
        if origen and origen not in origenes_permitidos and "*" not in origenes_permitidos:
            from app.core.exceptions.mensajes_error import MensajesDeError
            mensaje = MensajesDeError.ACCESO_DENEGADO.value[0]
            status = MensajesDeError.ACCESO_DENEGADO.value[1]
            return JSONResponse(
                status_code=status,
                content={
                    "estado": "error",
                    "mensaje": mensaje,
                    "detalles": f"El origen '{origen}' no está autorizado por las políticas CORS.",
                    "ruta": request.url.path,
                    "errores": ["CORS Origin Restringido"]
                }
            )
        return await call_next(request)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origenes_permitidos,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    
    app.add_middleware(
        TrustedHostMiddleware, 
        allowed_hosts=hosts_permitidos
    )