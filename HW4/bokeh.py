import random
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.models import Select
from bokeh.layouts import column

X = [x for x in range(100)]
Y_up = [y for y in X]
Y_rand = [y + random.randint(-5, 5) for y in Y_up]
Y_down = [-y for y in X]

output_file("random_data.html")

f = figure(
    x_range=(min(X), max(X)),
    y_range=(-100, 100)
)

f.line(X, Y_up, legend_label='Up', line_width=2, line_color='blue')
f.line(X, Y_rand, legend_label='Random', line_width=2, line_color='green')
f.line(X, Y_down, legend_label='Down', line_width=2, line_color='red')

def selection(attr, old, new):
    new_data = dict()
    new_data['x'] = X
    new_data['y'] = Y_up if selector.value == 'Up' else Y_rand if selector.value == 'Random' else Y_down
    f.renderers = []  # Clear existing lines
    f.line(new_data['x'], new_data['y'], legend_label=selector.value, line_width=2)

selector = Select(title='Select line', value='Up', options=['Up', 'Random', 'Down'])
selector.on_change('value', selection)

layout = column(selector, f)

curdoc().add_root(layout)
show(f)



