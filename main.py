import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)


# Datos para el primer KPI
acceso_actual_1 = 216
nuevo_acceso_1 = 220.32
kpi_1 = ((nuevo_acceso_1 - acceso_actual_1) / acceso_actual_1) * 100  

# Datos para el segundo KPI
acceso_actual_2 = 216
nuevo_acceso_2 = 324
kpi_2 = ((nuevo_acceso_2 - acceso_actual_2) / acceso_actual_2) * 100   

app.layout = html.Div([
    html.H1('KPIs'),
    html.Div([
        dcc.Graph(
            id='kpi-1',
            figure={
                'data': [
                    {'x': [nuevo_acceso_1,acceso_actual_1,kpi_1], 'y': [nuevo_acceso_1,acceso_actual_1,kpi_1], 'type': 'bar', 'name': 'KPI 1'},
                ],
                'layout': {
                    'title': 'KPI 1',
                },
            } 
        ),
        dcc.Graph(
            id='kpi-2',
            figure={
                'data': [
                    {'x': [nuevo_acceso_2,acceso_actual_2,kpi_2], 'y': [nuevo_acceso_2,acceso_actual_2,kpi_2], 'type': 'bar', 'name': 'KPI 2'},
                ],
                'layout': {
                    'title': 'KPI 2',
                },
            }
        ),
    ])
])
if __name__ == '__main__':
    app.run_server(debug=True)