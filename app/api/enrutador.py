from fastapi import FastAPI
from app.modules.prediccion.controllers.prediccion_controller import controlador as prediccion_controlador
from app.modules.salud.controllers.salud_controller import enrutador_salud

def registrar_rutas(app: FastAPI):
    app.include_router(prediccion_controlador, prefix='/api/prediccion', tags=['Predicción'])
    app.include_router(enrutador_salud, prefix='/api', tags=['Salud'])

    @app.get('/api')
    def raiz():
        return {'mensaje': 'Bienvenido al API de Predicción de Deserción Estudiantil'}