from ipywidgets import widgets, Layout
import easygopigo3 as easy

Hassan_gp3 = easy.EasyGoPiGo3()
darkgrey = '#888888'
items_layout = Layout(flex='1 1 auto', width='auto')

# override the default width of the button to 'auto' to let the button grow
box_layout = Layout(display='flex', flex_flow='column', align_items='stretch', border='solid', width='30%')
def on_forward_clicked(b):
Hassan_gp3.forward()
def on_backward_clicked(b):
Hassan_gp3.backward()
def on_stop_clicked(b):
Hassan_gp3.stop()

def on_left_clicked(b):
Hassan_gp3.left()
 
def on_right_clicked(b):
Hassan_gp3.right()
 
buttons = []
descriptions = ["Go Forward", "Left", "STOP", "Right" , "Go Backward"]
callbacks = [on_forward_clicked, on_left_clicked, on_stop_clicked, on_right_clicked, on_backward_clicked ]
for i in range(5):
buttons.append(widgets.Button(description=descriptions[i], layout=items_layout))
buttons[i].style.button_color = darkgrey
buttons[i].on_click(callbacks[i])
buttons[2].style.button_color = 'red' 

# stop button
mid_row = widgets.HBox([buttons[1], buttons[2], buttons[3] ])
display(widgets.VBox([buttons[0], mid_row, buttons[4]], layout=box_layout

