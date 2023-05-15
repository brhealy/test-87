def on_button_pressed_a():
    basic.show_icon(IconNames.EIGTH_NOTE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
