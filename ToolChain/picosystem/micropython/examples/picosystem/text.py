import io
import math
import time

view = 0
view_count = 3
douglas = Buffer(32, 45)


def update(tick):
    global view

    if pressed(RIGHT):
        view += 1

    if pressed(LEFT):
        view -= 1

    view %= view_count


def title(t):
    pen(15, 15, 15)
    frect(0, 0, 120, 11)
    pen(0, 0, 0)

    text(f"{t} ({view + 1}/{view_count})", 2, 2)


def view0_word_wrap(tick):
    title("Word wrap")
    wrap = int(math.sin(time.ticks_ms() / 500.0) * 36.0) + 80

    message = """\
\\penAAAFWe are just an advanced breed of \\penFFFFmonkeys\\penAAAF on a minor \
planet of a \\penFFFFvery average star\\penAAAF. But we can understand the \
Universe. That makes us something very special.\
\n\
\n\t\\penFFFF- Stephen Hawking"""

    # measure how large the text will be and draw boundary on screen
    w, h = measure(message, wrap)
    pen(4, 4, 4, 4)
    frect(0, 28, w + 4, h + 4)

    # draw wrapped text
    pen(8, 8, 8)
    text(message, 2, 30, wrap)

    # draw wrap width marker
    pen(15, 15, 15)
    text("Wrap here ", wrap - 54, 15)
    vline(wrap + 2, 15, 8)
    line(wrap + 2, 23, wrap + 2 - 2, 21)
    line(wrap + 2, 23, wrap + 2 + 2, 21)
    pen(0, 8, 0)
    vline(wrap + 2, 27, 92)


def view1_colour_codes(tick):
    title("Colour codes")

    pen(15, 15, 15)
    message = """\
\\penffff~680nm is \\penf00fred\\penffff\
\n~480nm is \\pen00ffblue\\penffff\
\nYou're on my wavelength\
\nAnd I quite like your hue\
\n\
\n\\pen0fff- Tanya Ha (@Ha_Tanya)"""

    pen(8, 8, 8)
    text(message, 2, 32)


def view2_scroll_and_clip(tick):
    message = """\
\"The fact that we live at the bottom of a deep gravity well, on the surface of \
a gas covered planet going around a nuclear fireball 90 million miles away and \
think this to be normal is obviously some indication of how skewed our \
perspective tends to be.\""""

    # box width and height
    bx = 30
    by = 0
    bw = 90
    bh = 120
    p = 20

    w, h = measure(message, bw - 10)
    h += p * 2
    overflow = h - bh
    scroll = int((math.sin(time.ticks_ms() / 2000.0) * overflow / 2.0) + (overflow / 2.0))
    scroll -= p

    alpha(4)
    blit(douglas, 0, 0, 32, 45, -10, 20 - int(scroll / 3), 32 * 3, 45 * 3)

    alpha()
    pen(12, 12, 12)
    clip(bx, by, bw, bh)
    text(message, bx + 5, by + 5 - scroll, bw - 10)
    clip()

    title("Scroll and clip")


def draw(tick):
    pen(0, 0, 0)
    clear()
    [view0_word_wrap, view1_colour_codes, view2_scroll_and_clip][view](tick)


io.BytesIO(bytearray([
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x11, 0xf1, 0x44, 0xf4,
    0x44, 0xf4, 0x33, 0xf3, 0x22, 0xf2, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x11, 0xf1, 0x66, 0xf6, 0x88, 0xf8, 0x66, 0xf6,
    0x66, 0xf6, 0x88, 0xf8, 0x66, 0xf6, 0x44, 0xf4, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x22, 0xf2, 0x77, 0xf7, 0x88, 0xf8, 0x77, 0xf7, 0x88, 0xf8,
    0x77, 0xf7, 0x77, 0xf7, 0x88, 0xf8, 0x88, 0xf8, 0x66, 0xf6, 0x22, 0xf2, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x11, 0xf1, 0x44, 0xf4, 0x55, 0xf5, 0x55, 0xf5, 0x66, 0xf6, 0x55, 0xf5, 0x55, 0xf5, 0x44, 0xf4,
    0x66, 0xf6, 0x77, 0xf7, 0x99, 0xf9, 0x99, 0xf9, 0x99, 0xf9, 0x88, 0xf8, 0x55, 0xf5, 0x11, 0xf1,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x33, 0xf3,
    0xaa, 0xfa, 0xbb, 0xfb, 0x88, 0xf8, 0x55, 0xf5, 0x44, 0xf4, 0x00, 0xf0, 0x00, 0xf0, 0x33, 0xf3,
    0x88, 0xf8, 0xaa, 0xfa, 0xaa, 0xfa, 0xaa, 0xfa, 0xaa, 0xfa, 0x88, 0xf8, 0x77, 0xf7, 0x55, 0xf5,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x66, 0xf6, 0x77, 0xf7, 0x88, 0xf8,
    0xbb, 0xfb, 0xcc, 0xfc, 0x99, 0xf9, 0x77, 0xf7, 0x66, 0xf6, 0x00, 0xf0, 0x00, 0xf0, 0x77, 0xf7,
    0xaa, 0xfa, 0xbb, 0xfb, 0xcc, 0xfc, 0xbb, 0xfb, 0xaa, 0xfa, 0x88, 0xf8, 0x77, 0xf7, 0x55, 0xf5,
    0x22, 0xf2, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x33, 0xf3, 0xcc, 0xfc, 0x99, 0xf9, 0x99, 0xf9,
    0xcc, 0xfc, 0xee, 0xfe, 0xcc, 0xfc, 0xaa, 0xfa, 0xaa, 0xfa, 0x55, 0xf5, 0x66, 0xf6, 0xbb, 0xfb,
    0xdd, 0xfd, 0xdd, 0xfd, 0xdd, 0xfd, 0xbb, 0xfb, 0x99, 0xf9, 0x88, 0xf8, 0x66, 0xf6, 0x55, 0xf5,
    0x33, 0xf3, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x55, 0xf5, 0xaa, 0xfa, 0x77, 0xf7, 0xaa, 0xfa,
    0xdd, 0xfd, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xee, 0xfe, 0xdd, 0xfd, 0xdd, 0xfd, 0xee, 0xfe,
    0xee, 0xfe, 0xee, 0xfe, 0xdd, 0xfd, 0xbb, 0xfb, 0xaa, 0xfa, 0x88, 0xf8, 0x77, 0xf7, 0x55, 0xf5,
    0x33, 0xf3, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x55, 0xf5, 0x88, 0xf8, 0x88, 0xf8, 0xcc, 0xfc,
    0xee, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
    0xff, 0xff, 0xff, 0xff, 0xdd, 0xfd, 0xcc, 0xfc, 0xbb, 0xfb, 0x99, 0xf9, 0x77, 0xf7, 0x55, 0xf5,
    0x33, 0xf3, 0x11, 0xf1, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x77, 0xf7, 0x99, 0xf9, 0xaa, 0xfa, 0xdd, 0xfd,
    0xee, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
    0xff, 0xff, 0xff, 0xff, 0xee, 0xfe, 0xdd, 0xfd, 0xbb, 0xfb, 0x99, 0xf9, 0x77, 0xf7, 0x55, 0xf5,
    0x33, 0xf3, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x77, 0xf7, 0x88, 0xf8, 0xaa, 0xfa, 0xcc, 0xfc,
    0xee, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xdd, 0xfd, 0xbb, 0xfb, 0x99, 0xf9, 0x77, 0xf7, 0x55, 0xf5,
    0x33, 0xf3, 0x11, 0xf1, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x88, 0xf8, 0x66, 0xf6, 0x99, 0xf9, 0xcc, 0xfc,
    0xee, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xdd, 0xfd, 0xbb, 0xfb, 0x99, 0xf9, 0x77, 0xf7, 0x55, 0xf5,
    0x33, 0xf3, 0x11, 0xf1, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x77, 0xf7, 0x66, 0xf6, 0x88, 0xf8, 0xcc, 0xfc,
    0xdd, 0xfd, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xdd, 0xfd, 0xbb, 0xfb, 0x99, 0xf9, 0x77, 0xf7, 0x55, 0xf5,
    0x33, 0xf3, 0x11, 0xf1, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x56, 0xf6, 0x66, 0xf6, 0x99, 0xf9, 0xcc, 0xfc,
    0xdd, 0xfd, 0xee, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xdd, 0xfd, 0xbb, 0xfb, 0x99, 0xf9, 0x77, 0xf7, 0x55, 0xf5,
    0x22, 0xf2, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x44, 0xf4, 0x33, 0xf3, 0xaa, 0xfa, 0xff, 0xff,
    0xee, 0xfe, 0xee, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
    0xff, 0xff, 0xff, 0xff, 0xee, 0xfe, 0xdd, 0xfd, 0xbb, 0xfb, 0x99, 0xf9, 0x77, 0xf7, 0x55, 0xf5,
    0x22, 0xf2, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x11, 0xf1, 0x22, 0xf2, 0x77, 0xf7, 0x99, 0xf9,
    0xdd, 0xfd, 0xee, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff,
    0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xee, 0xfe, 0xbb, 0xfb, 0x88, 0xf8, 0x66, 0xf6, 0x44, 0xf4,
    0x22, 0xf2, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x11, 0xf1, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x11, 0xf1, 0x11, 0xf1, 0x11, 0xf1, 0x66, 0xf6, 0xff, 0xff, 0xff, 0xff, 0xee, 0xfe, 0xee, 0xfe,
    0xdd, 0xfd, 0xaa, 0xfa, 0x66, 0xf6, 0x44, 0xf4, 0x33, 0xf3, 0x44, 0xf4, 0x11, 0xf1, 0x00, 0xf0,
    0x22, 0xf2, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x11, 0xf1, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x88, 0xf8, 0xff, 0xff, 0xff, 0xff,
    0x88, 0xf8, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x11, 0xf1, 0x33, 0xf3, 0x44, 0xf4, 0x88, 0xf8, 0x00, 0xf0, 0x00, 0xf0, 0xee, 0xfe, 0xff, 0xff,
    0xaa, 0xfa, 0x66, 0xf6, 0x44, 0xf4, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x11, 0xf1,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x44, 0xf4, 0x88, 0xf8, 0x22, 0xf2,
    0x66, 0xf6, 0xcc, 0xfc, 0xff, 0xff, 0xff, 0xff, 0xdd, 0xfd, 0x11, 0xf1, 0xbb, 0xfb, 0xee, 0xfe,
    0xdd, 0xfd, 0xdd, 0xfd, 0xbb, 0xfb, 0x77, 0xf7, 0x66, 0xf6, 0x55, 0xf5, 0x33, 0xf3, 0x22, 0xf2,
    0x11, 0xf1, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x11, 0xf1, 0xcc, 0xfc, 0x88, 0xf8,
    0x66, 0xf6, 0xaa, 0xfa, 0xdd, 0xfd, 0xff, 0xff, 0x99, 0xf9, 0x33, 0xf3, 0xcc, 0xfc, 0xdd, 0xfd,
    0xcc, 0xfc, 0xdd, 0xfd, 0x99, 0xf9, 0x99, 0xf9, 0x88, 0xf8, 0x55, 0xf5, 0x44, 0xf4, 0x22, 0xf2,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x88, 0xf8, 0xab, 0xfb,
    0x99, 0xf9, 0xbb, 0xfb, 0xee, 0xfe, 0xee, 0xfe, 0x55, 0xf5, 0x33, 0xf3, 0xdd, 0xfd, 0xdd, 0xfd,
    0xaa, 0xfa, 0xcc, 0xfc, 0xbb, 0xfb, 0x88, 0xf8, 0x66, 0xf6, 0x44, 0xf4, 0x44, 0xf4, 0x22, 0xf2,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x22, 0xf2, 0x99, 0xf9,
    0xcc, 0xfc, 0xcc, 0xfc, 0xee, 0xfe, 0xbb, 0xfb, 0x33, 0xf3, 0x44, 0xf4, 0xdd, 0xfd, 0xee, 0xfe,
    0xaa, 0xfa, 0xbb, 0xfb, 0xcc, 0xfc, 0xaa, 0xfa, 0x77, 0xf7, 0x66, 0xf6, 0x44, 0xf4, 0x11, 0xf1,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x77, 0xf7,
    0xbb, 0xfb, 0xcc, 0xfc, 0xdd, 0xfd, 0x88, 0xf8, 0x33, 0xf3, 0x88, 0xf8, 0xdd, 0xfd, 0xee, 0xfe,
    0xdd, 0xfd, 0xaa, 0xfa, 0xbb, 0xfb, 0xbb, 0xfb, 0x88, 0xf8, 0x66, 0xf6, 0x33, 0xf3, 0x11, 0xf1,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x44, 0xf4,
    0x99, 0xf9, 0xcc, 0xfc, 0x99, 0xf9, 0x11, 0xf1, 0x55, 0xf5, 0xaa, 0xfa, 0xee, 0xfe, 0xff, 0xff,
    0xdd, 0xfd, 0xcc, 0xfc, 0x88, 0xf8, 0x99, 0xf9, 0x88, 0xf8, 0x66, 0xf6, 0x33, 0xf3, 0x11, 0xf1,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x22, 0xf2,
    0x88, 0xf8, 0xcc, 0xfc, 0x77, 0xf7, 0x00, 0xf0, 0x00, 0xf0, 0xaa, 0xfa, 0xff, 0xff, 0xff, 0xff,
    0xaa, 0xfa, 0x77, 0xf7, 0xaa, 0xfa, 0x66, 0xf6, 0x77, 0xf7, 0x66, 0xf6, 0x33, 0xf3, 0x11, 0xf1,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x66, 0xf6, 0x99, 0xf9, 0x66, 0xf6, 0x00, 0xf0, 0x00, 0xf0, 0x22, 0xf2, 0xaa, 0xfa, 0x88, 0xf8,
    0x66, 0xf6, 0x88, 0xf8, 0xbb, 0xfb, 0x77, 0xf7, 0x44, 0xf4, 0x55, 0xf5, 0x33, 0xf3, 0x11, 0xf1,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x11, 0xf1,
    0x33, 0xf3, 0x55, 0xf5, 0x88, 0xf8, 0x33, 0xf3, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x11, 0xf1,
    0xaa, 0xfa, 0xcc, 0xfc, 0x99, 0xf9, 0x88, 0xf8, 0x55, 0xf5, 0x44, 0xf4, 0x33, 0xf3, 0x11, 0xf1,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x33, 0xf3,
    0x44, 0xf4, 0x00, 0xf0, 0x00, 0xf0, 0x44, 0xf4, 0x22, 0xf2, 0x11, 0xf1, 0x44, 0xf4, 0x88, 0xf8,
    0xbb, 0xfb, 0xaa, 0xfa, 0x88, 0xf8, 0x66, 0xf6, 0x55, 0xf5, 0x44, 0xf4, 0x22, 0xf2, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x66, 0xf6, 0x44, 0xf4, 0x00, 0xf0, 0x11, 0xf1, 0x44, 0xf4, 0x66, 0xf6, 0x99, 0xf9, 0x88, 0xf8,
    0x88, 0xf8, 0x77, 0xf7, 0x44, 0xf4, 0x33, 0xf3, 0x55, 0xf5, 0x44, 0xf4, 0x22, 0xf2, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x44, 0xf4, 0x66, 0xf6, 0x33, 0xf3, 0x22, 0xf2, 0x33, 0xf3, 0x44, 0xf4, 0x22, 0xf2, 0x44, 0xf4,
    0x66, 0xf6, 0x77, 0xf7, 0x77, 0xf7, 0x66, 0xf6, 0x55, 0xf5, 0x44, 0xf4, 0x11, 0xf1, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x11, 0xf1, 0x55, 0xf5, 0x66, 0xf6, 0x55, 0xf5, 0x44, 0xf4, 0x55, 0xf5, 0x66, 0xf6, 0x44, 0xf4,
    0x55, 0xf5, 0x77, 0xf7, 0x88, 0xf8, 0x77, 0xf7, 0x55, 0xf5, 0x33, 0xf3, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x33, 0xf3, 0x77, 0xf7, 0xbb, 0xfb, 0xcc, 0xfc, 0xbb, 0xfb, 0xcc, 0xfc, 0xbb, 0xfb,
    0xbb, 0xfb, 0xaa, 0xfa, 0x99, 0xf9, 0x77, 0xf7, 0x55, 0xf5, 0x22, 0xf2, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x33, 0xf3, 0xaa, 0xfa, 0xbb, 0xfb, 0xcc, 0xfc, 0xee, 0xfe, 0xee, 0xfe,
    0xcc, 0xfc, 0xbb, 0xfb, 0xaa, 0xfa, 0x77, 0xf7, 0x33, 0xf3, 0x00, 0xf0, 0x11, 0xf1, 0x11, 0xf1,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x22, 0xf2, 0x99, 0xf9, 0xcc, 0xfc, 0xdd, 0xfd, 0xdd, 0xfd,
    0xcc, 0xfc, 0xbb, 0xfb, 0x88, 0xf8, 0x11, 0xf1, 0x00, 0xf0, 0x11, 0xf1, 0x33, 0xf3, 0x22, 0xf2,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x44, 0xf4, 0x77, 0xf7, 0x77, 0xf7,
    0x55, 0xf5, 0x44, 0xf4, 0x00, 0xf0, 0x00, 0xf0, 0x22, 0xf2, 0x66, 0xf6, 0x44, 0xf4, 0x11, 0xf1,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x55, 0xf5, 0x88, 0xf8, 0x66, 0xf6, 0x55, 0xf5, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x11, 0xf1, 0x77, 0xf7, 0xaa, 0xfa, 0x88, 0xf8, 0x77, 0xf7, 0x33, 0xf3, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x33, 0xf3, 0x77, 0xf7, 0x99, 0xf9, 0xaa, 0xfa, 0x99, 0xf9, 0x88, 0xf8, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x22, 0xf2, 0x22, 0xf2, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x55, 0xf5,
    0x77, 0xf7, 0xaa, 0xfa, 0xcc, 0xfc, 0xbb, 0xfb, 0xaa, 0xfa, 0x44, 0xf4, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x66, 0xf6, 0xbb, 0xfb, 0xaa, 0xfa, 0x66, 0xf6, 0x55, 0xf5, 0x99, 0xf9,
    0xcc, 0xfc, 0xcc, 0xfc, 0xdd, 0xfd, 0xcc, 0xfc, 0x99, 0xf9, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x77, 0xf7, 0xee, 0xfe, 0xee, 0xfe, 0xcc, 0xfc, 0xcc, 0xfc, 0xdd, 0xfd,
    0xdd, 0xfd, 0xdd, 0xfd, 0xcc, 0xfc, 0xdd, 0xfd, 0x33, 0xf3, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x66, 0xf6, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xee, 0xfe,
    0xee, 0xfe, 0xee, 0xfe, 0xee, 0xfe, 0x99, 0xf9, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0,
    0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0, 0x00, 0xf0
])).readinto(douglas)

start()