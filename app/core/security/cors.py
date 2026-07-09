from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

def configurar_cors(app: FastAPI):
    origenes_permitidos = ['http://localhost', 'http://localhost:5173', 'http://127.0.0.1:5173']
    app.add_middleware(CORSMiddleware, allow_origins=origenes_permitidos, allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=['localhost', '127.0.0.1', '*'])