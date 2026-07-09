import uvicorn
from fastapi import FastAPI
from app.api.enrutador import registrar_rutas
from app.core.security.cors import configurar_cors
from app.core.exceptions.excepciones_globales import registrar_manejadores_error

def crear_app() -> FastAPI:
    app = FastAPI(title='Predictor de Deserción Estudiantil', description='API para predecir si un estudiante abandonará sus estudios', version='1.0.1')
    configurar_cors(app)
    registrar_rutas(app)
    registrar_manejadores_error(app)
    return app
aplicacion = crear_app()
if __name__ == '__main__':
    uvicorn.run('main:aplicacion', host='0.0.0.0', port=8000, reload=True)