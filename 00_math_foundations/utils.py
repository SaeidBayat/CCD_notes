import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots

FONT_FAMILY = "Palatino"

def plot_function_with_tangent_line(f, f_prime, x_range=(-10, 10), y_range=(-10, 10), title=None, font=None, xaxis_title='x', yaxis_title='y', show_axis_labels=None):
    """
    Plot function in 2D space.
    
    Args:
        f: function to plot
        f_prime: derivative of function to plot
        x_range: range of x-axis
        y_range: range of y-axis
        title: Optional title for the plot
        font: Optional font dictionary
        xaxis_title: Title for x-axis
        yaxis_title: Title for y-axis
        show_axis_labels: Whether to show axis labels
    
    Returns:
        plotly.graph_objects.Figure: The plotly figure object
    """

    fig = go.Figure()
    x = np.linspace(x_range[0], x_range[1], 100)
    y = f(x)
    y_prime = f_prime(x)
    x_slider=list(range(x_range[0], x_range[1] + 1))

    # Plot function
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x)', line=dict(color='#3d81f6')))

    # Initialize tangent line and point with x = -2 (default position)
    initial_x_point = -2
    initial_tan_slope = f_prime(initial_x_point)
    initial_y_point = f(initial_x_point)
    
    # Calculate tangent line with constant length
    tangent_length = 3  # Half-length of tangent line
    dx = tangent_length / np.sqrt(1 + initial_tan_slope**2)
    initial_x_tangent = np.array([initial_x_point - dx, initial_x_point + dx])
    initial_y_tangent = initial_tan_slope * (initial_x_tangent - initial_x_point) + initial_y_point

    tangent_line = go.Scatter(
        x=initial_x_tangent,
        y=initial_y_tangent,
        mode='lines',
        line=dict(color='orange'),
        name='Tangent line'
    )
    fig.add_trace(tangent_line)

    tangent_point = go.Scatter(
        x=[initial_x_point],
        y=[initial_y_point],
        mode='markers',
        marker=dict(color='orange', size=7),
        name='Tangent point'
    )
    fig.add_trace(tangent_point)
    
    slider_steps = []
    for i, x_point in enumerate(x_slider):
        tan_slope = f_prime(x_point)
        y_point = f(x_point)
        
        # Calculate tangent line with constant length
        tangent_length = 3  # Half-length of tangent line
        dx = tangent_length / np.sqrt(1 + tan_slope**2)
        x_tangent = np.array([x_point - dx, x_point + dx])
        y_tangent = tan_slope * (x_tangent - x_point) + y_point

        # Use original title if provided, otherwise show tangent info
        if title is not None:
            step_title = title
        else:
            step_title = f"Tangent line at x = {x_point}"
        
        step = dict(
            method='update',
            args=[{
                'x': [x, x_tangent, [x_point]],
                'y': [y, y_tangent, [y_point]]
            }, {
                'title': {'text': step_title}
            }],
            label=f"x = {x_point}"
        )
        slider_steps.append(step)

    # Slider layout
    # Find index for x = -2 (default position)
    default_index = x_slider.index(-2)
    sliders = [dict(
        active=default_index,
        steps=slider_steps,
        currentvalue={"prefix": ""},
        pad={"t": 50}
    )]

    layout_dict = dict(
        xaxis=dict(
            title=xaxis_title if show_axis_labels else '',
            range=x_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10, family=FONT_FAMILY),
            title_font=dict(family=FONT_FAMILY)
        ),
        yaxis=dict(
            title=yaxis_title if show_axis_labels else '',
            range=y_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10, family=FONT_FAMILY),
            title_font=dict(family=FONT_FAMILY)
        ),
        sliders=sliders,
        width=600,
        height=600,
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family=FONT_FAMILY) if font is None else font,
        margin=dict(l=50, r=50, t=50, b=50),
        showlegend=False
    )

    # Set initial title to match the default slider position
    if title is not None:
        layout_dict['title'] = title
    else:
        layout_dict['title'] = f"Tangent line at x = {initial_x_point}"

    fig.update_layout(layout_dict)
    return fig

def plot_function_with_secant_line(f, x1, x2, x_range=(-10, 10), y_range=(-10, 10), title=None, font=None, xaxis_title='x', yaxis_title='y', show_axis_labels=None):
    """
    Plot function in 2D space with a secant line between two points.
    
    Args:
        f: function to plot
        x1: first x-coordinate for secant line
        x2: second x-coordinate for secant line
        x_range: range of x-axis
        y_range: range of y-axis
        title: Optional title for the plot
        font: Optional font dictionary
        xaxis_title: Title for x-axis
        yaxis_title: Title for y-axis
        show_axis_labels: Whether to show axis labels
    
    Returns:
        plotly.graph_objects.Figure: The plotly figure object
    """

    fig = go.Figure()
    x = np.linspace(x_range[0], x_range[1], 100)
    y = f(x)

    # Plot function
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='f(x)', line=dict(color='#3d81f6')))

    # Calculate secant line points
    y1 = f(x1)
    y2 = f(x2)
    
    # Calculate secant line slope and extend it for visualization
    slope = (y2 - y1) / (x2 - x1)
    
    # Extend secant line for better visualization
    x_secant = np.array([x1 - 2, x2 + 2])
    y_secant = slope * (x_secant - x1) + y1

    # Plot secant line
    secant_line = go.Scatter(
        x=x_secant,
        y=y_secant,
        mode='lines',
        line=dict(color='orange', dash='dash'),
        name='Secant line'
    )
    fig.add_trace(secant_line)

    # Plot the two points
    points = go.Scatter(
        x=[x1, x2],
        y=[y1, y2],
        mode='markers',
        marker=dict(color='orange', size=8),
        name='Points'
    )
    fig.add_trace(points)

    layout_dict = dict(
        xaxis=dict(
            title=xaxis_title if show_axis_labels else '',
            range=x_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10, family=FONT_FAMILY),
            title_font=dict(family=FONT_FAMILY)
        ),
        yaxis=dict(
            title=yaxis_title if show_axis_labels else '',
            range=y_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10, family=FONT_FAMILY),
            title_font=dict(family=FONT_FAMILY)
        ),
        width=600,
        height=600,
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family=FONT_FAMILY) if font is None else font,
        margin=dict(l=50, r=50, t=50, b=50),
        showlegend=False
    )

    if title is not None:
        layout_dict['title'] = title

    fig.update_layout(layout_dict)
    return fig

def plot_multiple_secant_lines(f, secant_points, x_range=(-10, 10), y_range=(-10, 10), title=None, font=None, xaxis_title='x', yaxis_title='y', show_axis_labels=None):
    """
    Plot function with multiple secant lines in separate subplots side by side.
    
    Args:
        f: function to plot
        secant_points: list of tuples, each containing (x1, x2) for secant lines
        x_range: range of x-axis
        y_range: range of y-axis
        title: Optional title for the plot
        font: Optional font dictionary
        xaxis_title: Title for x-axis
        yaxis_title: Title for y-axis
        show_axis_labels: Whether to show axis labels
    
    Returns:
        plotly.graph_objects.Figure: The plotly figure object
    """
    
    n_plots = len(secant_points)
    fig = make_subplots(rows=1, cols=n_plots, subplot_titles=[f"({x1}, f({x1})) to ({x2}, f({x2}))" for x1, x2 in secant_points])
    
    x = np.linspace(x_range[0], x_range[1], 100)
    y = f(x)
    
    for i, (x1, x2) in enumerate(secant_points):
        col = i + 1
        
        # Plot function
        fig.add_trace(
            go.Scatter(x=x, y=y, mode='lines', name='f(x)', line=dict(color='#3d81f6'), showlegend=(i==0)),
            row=1, col=col
        )
        
        # Calculate secant line points
        y1 = f(x1)
        y2 = f(x2)
        
        # Calculate secant line slope and extend it for visualization
        slope = (y2 - y1) / (x2 - x1)
        
        # Extend secant line for better visualization
        x_secant = np.array([x1 - 2, x2 + 2])
        y_secant = slope * (x_secant - x1) + y1
        
        # Plot secant line
        fig.add_trace(
            go.Scatter(
                x=x_secant,
                y=y_secant,
                mode='lines',
                line=dict(color='orange', dash='dash'),
                name='Secant line',
                showlegend=False
            ),
            row=1, col=col
        )
        
        # Plot the two points
        fig.add_trace(
            go.Scatter(
                x=[x1, x2],
                y=[y1, y2],
                mode='markers',
                marker=dict(color='orange', size=8),
                name='Points',
                showlegend=False
            ),
            row=1, col=col
        )
    
    # Update layout for all subplots
    for i in range(1, n_plots + 1):
        fig.update_xaxes(
            title=xaxis_title if show_axis_labels else '',
            range=x_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10, family=FONT_FAMILY),
            title_font=dict(family=FONT_FAMILY),
            row=1, col=i
        )
        fig.update_yaxes(
            title=yaxis_title if show_axis_labels else '',
            range=y_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10, family=FONT_FAMILY),
            title_font=dict(family=FONT_FAMILY),
            row=1, col=i
        )
    
    layout_dict = dict(
        width=200 * n_plots,
        height=600,
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family=FONT_FAMILY) if font is None else font,
        margin=dict(l=50, r=50, t=50, b=50),
        showlegend=False
    )
    
    if title is not None:
        layout_dict['title'] = title
    
    fig.update_layout(layout_dict)
    return fig

def plot_functions(f_list, f_titles, crit_x=None, x_range=(-10, 10), y_range=(-10, 10), title=None, font=None, xaxis_title='x', yaxis_title='y', show_axis_labels=None, exclude_x=None, color_just_one=None):
    """
    Plot function in 2D space.
    
    Args:
        f: function to plot
        f_prime: derivative of function to plot
        crit_x: critical points of function to plot
        x_range: range of x-axis
        y_range: range of y-axis
        title: Optional title for the plot
        font: Optional font dictionary
        xaxis_title: Title for x-axis
        yaxis_title: Title for y-axis
        show_axis_labels: Whether to show axis labels
        exclude_x: x-axis value to exclude
    
    Returns:
        plotly.graph_objects.Figure: The plotly figure object
    """
    # Define color scheme for functions
    colors = ['#3d81f6', 'orange', '#d81b60', '#004d40', '#6f42c1', '#20c997']
    if color_just_one is not None:
        colors = [colors[color_just_one]] * len(f_list)
    
    fig = go.Figure()
    for i, (f, f_title) in enumerate(zip(f_list, f_titles)):
        color = colors[i] if i < len(colors) else colors[i % len(colors)]
        
        if exclude_x is not None:
            x1 = np.linspace(x_range[0], exclude_x-0.001, 10000)
            x2 = np.linspace(exclude_x+0.001, x_range[1], 10000)
            x = np.concatenate([x1, x2])

            y1 = f(x1)
            y2 = f(x2)
            y = np.concatenate([y1, [None], y2])
        else:
            x = np.linspace(x_range[0], x_range[1], 10000)
            y = f(x)
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f_title, line=dict(color=color)))
    
    if crit_x is not None:
        for i, f in enumerate(f_list):
            crit_y = [f(x) for x in crit_x]
            fig.add_trace(go.Scatter(
                x=crit_x,
                y=crit_y,
                mode='markers',
                marker=dict(color=colors[i], size=7),
                # name=f'Critical Points ({f_titles[i]})' if f_titles else 'Critical Points'
            ))

    layout_dict = dict(
        xaxis=dict(
            title=xaxis_title if show_axis_labels else '',
            range=x_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10, family=FONT_FAMILY),
            title_font=dict(family=FONT_FAMILY)
        ),
        yaxis=dict(
            title=yaxis_title if show_axis_labels else '',
            range=y_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10, family=FONT_FAMILY),
            title_font=dict(family=FONT_FAMILY)
        ),
        width=600,
        height=600,
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family=FONT_FAMILY) if font is None else font,
        margin=dict(l=50, r=50, t=50, b=50),
        showlegend=False
    )

    if title is not None:
        layout_dict['title'] = title


    fig.update_layout(layout_dict)
    return fig


def plot_functions_grid(f_list, f_titles, f_excludes=None, rows=2, cols=2, x_range=(-10, 10), y_range=(-10, 10), title=None, font=None, xaxis_title='x', yaxis_title='y', show_axis_labels=None, exclude_x=None, exclude_y=None,
                        grid_spacing=0.05):
    """
    Plot 2D functions in a grid.
    
    Args:
        f_list: list of functions to plot
        f_titles: list of titles for each function
        f_excludes: list of x-axis values to exclude for function with same index
        x_range: range of x-axis
        y_range: range of y-axis
        title: Optional title for the plot
        font: Optional font dictionary
        xaxis_title: Title for x-axis
        yaxis_title: Title for y-axis
        show_axis_labels: Whether to show axis labels
    
    Returns:
        plotly.graph_objects.Figure: The plotly figure object
    """
    # Define color scheme for functions
    colors = ['#3d81f6', 'orange', '#d81b60', '#004d40', '#6f42c1', '#20c997']
    
    fig = make_subplots(rows=rows, cols=cols, subplot_titles=f_titles, horizontal_spacing=grid_spacing, vertical_spacing=grid_spacing)

    
    for r in range(rows):   
        for c in range(cols):
            f = f_list[r*cols + c]
            color = colors[r*cols + c] if r*cols + c < len(colors) else colors[(r*cols + c) % len(colors)]
            
            if f_excludes is not None and f_excludes[r*cols + c] is not None:
                exclude_x = f_excludes[r*cols + c]
                x1 = np.linspace(x_range[0], exclude_x-0.001, 10000)
                x2 = np.linspace(exclude_x+0.001, x_range[1], 10000)
                x = np.concatenate([x1, x2])

                y1 = f(x1)
                y2 = f(x2)
                y = np.concatenate([y1, [None], y2])
            else:
                x = np.linspace(x_range[0], x_range[1], 10000)
                y = f(x)

            fig.add_trace(
                go.Scatter(x=x, y=y, mode='lines', name=f_titles[r*cols + c], line=dict(color=color)),
                row=r + 1, col=c + 1)

    layout_dict = dict(
        width=400,
        height=400,
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(family=FONT_FAMILY) if font is None else font,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=True
    )

    for i in range(1, rows * cols + 1):
        axis_suffix = "" if i == 1 else str(i)
        layout_dict[f'xaxis{axis_suffix}'] = dict(
            title=xaxis_title if show_axis_labels else '',
            range=x_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10, family=FONT_FAMILY),
            title_font=dict(family=FONT_FAMILY),
            showticklabels=False
        )
        layout_dict[f'yaxis{axis_suffix}'] = dict(
            title=yaxis_title if show_axis_labels else '',
            range=y_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10, family=FONT_FAMILY),
            title_font=dict(family=FONT_FAMILY),
            showticklabels=False
        )
    

    if title is not None:
        layout_dict['title'] = title

    fig.update_layout(**layout_dict)
    return fig

def plot_piecewise(f_list, intervals=None, x_range=(-10, 10), y_range=(-10, 10), title=None, font=None, xaxis_title='x', yaxis_title='y', show_axis_labels=None):
    """
    Plot function in 2D space.
    
    Args:
        f: function to plot
        f_prime: derivative of function to plot
        crit_x: critical points of function to plot
        x_range: range of x-axis
        y_range: range of y-axis
        title: Optional title for the plot
        font: Optional font dictionary
        xaxis_title: Title for x-axis
        yaxis_title: Title for y-axis
        show_axis_labels: Whether to show axis labels
        intervals: list of tuples, each containing (x_start, x_end), REQUIRED
    
    Returns:
        plotly.graph_objects.Figure: The plotly figure object
    """
    fig = go.Figure()
    for i in range(len(f_list)):
        x = np.linspace(intervals[i][0], intervals[i][1], 100)
        y = f_list[i](x)
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))
    
    layout_dict = dict(
        xaxis=dict(
            title=xaxis_title if show_axis_labels else '',
            range=x_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10)
        ),
        yaxis=dict(
            title=yaxis_title if show_axis_labels else '',
            range=y_range,
            gridcolor='#f0f0f0',
            zerolinecolor='gray',
            tickfont=dict(size=10)
        ),
        width=600,
        height=600,
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=font,
        margin=dict(l=50, r=50, t=50, b=50),
    )

    if title is not None:
        layout_dict['title'] = title


    fig.update_layout(layout_dict)
    return fig