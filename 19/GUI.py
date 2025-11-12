from nicegui import ui

ui.label("Welcome to nicegui!").style("color: green; font: 24px")
ui.run()

#create a greeting

def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "stranger"}"
    ui.notify(msg) # create a popup

input_field = ui.input("Enter your name")
ui.button("Greet Me!", on_click = greet, color = "green")


class State:
    count = 0

count_label = ui.label("Count: 0")

def add_one():
    State.count += 1
    count_label.text = f"Count {State.count}"

ui.button("Add 1", on_click = add_one)

ui.run(title = "Simple Greeting App")

#-------------- TODO --------------
#create a reset button which sets the counter to 0
def reset_count():
    State.count = 0
    count_label.text = f" Count {State.count}"
ui.button("Reset the count!", on_click= reset_count)