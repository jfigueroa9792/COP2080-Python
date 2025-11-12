from nicegui import ui


# create a greeting
#----------------------------------------
def greet():
    name = input_field.value.strip()
    msg = f"Hello, {name or "stranger"}"
    ui.notify(msg, color= "green", position= "bottom-left") # create a popup
#----------------------------------------

# Counter
#----------------------------------------
class State:
    count = 0

def add_one():
    State.count += slider.value
    count_label.text = f"Count {State.count}"

def reset_count():
    State.count = 0
    count_label.text = f" Count {State.count}"
#----------------------------------------

# Layout
#----------------------------------------
ui.label("Welcome to nicegui!").style("color: green; font-size: 40px")

with ui.row().classes("w-full"):
    with ui.column().classes("flex-1"):    
        with ui.card().classes("h-65 w-full self-auto"):
            ui.label("Greeting").style("font-size: 30px")
            input_field = ui.input("Enter your name").classes("w-100")
            ui.button("Greet Me!", on_click = greet, color = "green")

    with ui.column().classes("flex-1"):
            with ui.card().classes("h-65 w-full self-auto"):
                ui.label("Counter").style("color: blue; font-size: 30px")
                with ui.column():
                    count_label = ui.label("Count: 0").classes("font-mono text-lg")
                    with ui.row():
                        ui.button("Add step", on_click = add_one)
                        ui.button("Reset", on_click= reset_count, color= "red")
                
                # add a slider
                label_slider = ui.label("Step: 5").classes("font-mono text-lg")
                slider = ui.slider(min=1, max=10, value=5)
                slider.on("update:model-value", lambda: label_slider.set_text(f"Step: {slider.value}"))
with ui.row():
    number1 = ui.number("Number 1", value=0).classes("w-24")
    ui.label("+").classes("text-lg")
    number2 = ui.number("Number 2", value=0).classes("w-24")
    ui.label("=").classes("text-lg")
    
    with ui.card():
        n1 = number1.value
        n2 = number2.value
        num = n1 + n2
        result = ui.label(num).classes("text-lg")

ui.switch("Dark Mode", on_change= lambda e: ui.dark_mode().enable() if e.value else ui.dark_mode.disable())
ui.run(title = "Simple Layout")

