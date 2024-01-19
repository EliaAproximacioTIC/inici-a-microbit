input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(2000)
    basic.clearScreen()
})
input.onGesture(Gesture.Shake, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    basic.pause(2000)
    basic.showIcon(IconNames.Sad)
    basic.pause(2000)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.EighthNote)
    music.play(music.stringPlayable("C5 G - A - F B C5 ", 250), music.PlaybackMode.UntilDone)
    basic.pause(500)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Happy)
    basic.pause(2000)
    basic.clearScreen()
})
basic.showString("Hola")
