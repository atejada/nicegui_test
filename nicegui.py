from fastapi import FastAPI
import nicegui
from nicegui import app, ui
#import uvicorn

fastapi_app = FastAPI()

@ui.page('/')
def index():
    ui.icon('thumb_up')
    ui.markdown('This is **Markdownsss**.')
    ui.html('This is <strong>HTML</strong>.')
    with ui.row():
        ui.label('CSS').style('color: #888; font-weight: bold')
        ui.label('Tailwind').classes('font-serif')
        ui.label('Quasar').classes('q-ml-xl')
    ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')

ui.run_with(fastapi_app)
