def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.pause(2000)
    basic.show_icon(IconNames.SAD)
    basic.pause(2000)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_icon(IconNames.EIGHTH_NOTE)
    music.play(music.string_playable("C5 G - A - F B C5 ", 250),
        music.PlaybackMode.UNTIL_DONE)
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.HAPPY)
    basic.pause(2000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Hola")