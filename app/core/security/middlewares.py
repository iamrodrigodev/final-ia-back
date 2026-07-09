import os
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.exceptions.mensajes_error import MensajesDeError
from dotenv import load_dotenv

load_dotenv()

class VerificarOrigenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        origen = request.headers.get("origin")
        
        entorno = os.getenv("ENTORNO", "local").lower()
        if entorno == "local":
            origenes_permitidos = [
                "http://localhost",
                "http://localhost:5173",
                "http://127.0.0.1:5173",
                "http://localhost:3000"
            ]
        else:
            origenes_permitidos = [os.getenv("FRONTEND_URL", "*")]
            
        # Validar si viene un origin y si no está en la lista blanca
        if origen and origen not in origenes_permitidos and "*" not in origenes_permitidos:
            mensaje = MensajesDeError.ACCESO_DENEGADO.value[0]
            status = MensajesDeError.ACCESO_DENEGADO.value[1]
            return JSONResponse(
                status_code=status,
                content={
                    "estado": "error",
                    "codigo": status,
                    "mensaje": "CORS Origin Restringido"
                }
            )
        return await call_next(request)
