from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1("Hello World!"),
        html.P(" #PBW3B1PBL0101"),
        html.P(" 25108020200011 Ravil adel wicaksono"),
        html.P(" fRAMEWORK PILIHAN PYTHON DASH PLOTLY"),
    ],
    style={
        "textAlign": "center",
        "marginTop": "100px"
    }
)

if __name__ == "__main__":
    app.run(debug=True)