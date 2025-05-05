
import numpy as np
import plotly.graph_objects as go

def generate_3d_surface(
    func,
    x_range=(-3, 3),
    y_range=(-3, 3),
    path=None,
    point=None,
    title="3D Surface Plot",
    resolution=100
):
    x_vals = np.linspace(x_range[0], x_range[1], resolution)
    y_vals = np.linspace(y_range[0], y_range[1], resolution)
    X, Y = np.meshgrid(x_vals, y_vals)

    Z = func(X, Y)

    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])

    if path:
        x_path = [p[0] for p in path]
        y_path = [p[1] for p in path]
        z_path = [func(x, y) for x, y in path]
        
        fig.add_trace(go.Scatter3d(
            x=x_path,
            y=y_path,
            z=z_path,
            mode="markers+lines",
            marker=dict(size=5, color="red"),
            line=dict(color="red", width=2),
            name="Optimization Path"
        ))

    if point is not None:
        x, y = point
        z = func(x, y)
        
        fig.add_trace(go.Scatter3d(
            x=[x],
            y=[y],
            z=[z],
            mode="markers",
            marker=dict(size=5, color="green"),
            name="Point"
        ))

    fig.update_layout(
        title={
            'text': title,
            'x': 0.5,
            'font': {'size': 18}
        },
        scene=dict(
            xaxis_title="x₁",
            yaxis_title="x₂",
            zaxis_title="f(x₁, x₂)",
            aspectmode="cube"
        ),
        height=700,
        margin=dict(l=0, r=0, b=0, t=30)
    )
    
    return fig
