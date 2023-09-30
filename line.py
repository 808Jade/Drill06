import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse_pointer = load_image('hand_arrow.png')

points = [ ( random.randint(0,TUK_WIDTH-75) , random.randint(0,TUK_HEIGHT-750) ) for i in range(10) ]
points_count = 0
frame = 0

# def draw_big_point(p):      # 가야할 곳을 찍는다
#     mouse_pointer.draw(p)

# def draw_point(p):          # 점을 찍는다 (캐릭터가 이 좌표 하나하나를 따라가야함)
#     character.clip_draw(frame * 66, 198, 66, 66, p[0], p[1], 150, 150)

def draw_line(p1, p2):       #  p1(x,y) 시작 p2(x,y) 도착
    x1, y1 = p1[0], p1[1]    # 계산을 위해 좌표 넣어주고..
    x2, y2 = p2[0], p2[1]    # ..
    global frame

    for i in range(0, 100 + 1, 3):
        t = i / 100
        x = (1-t) * x1 + t * x2  # 1-t : t 의 비율로 x1, x2를 섞는다 더한다.
        y = (1-t) * y1 + t * y2
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        mx, my = points[points_count]
        mouse_pointer.draw_now(mx, my)
        if mx - x > 0:
            character.clip_draw(frame * 66, 66, 66, 66, x, y, 150, 150)
        elif mx - x < 0:
            character.clip_draw(frame * 66, 132, 66, 66, x, y, 150, 150)
        elif mx - x == 0:
            if my - y > 0:
                character.clip_draw(frame * 66, 0, 66, 66, x, y, 150, 150)
            elif my - y < 0:
                character.clip_draw(frame * 66, 198, 66, 66, x, y, 150, 150)
        else:
            character.clip_draw(frame * 66, 198, 66, 66, x, y, 150, 150)
        frame = (frame + 1) % 4
        update_canvas()
        delay(0.03)

# draw_point(p2)  # 마지막 점을 확실히 찍기

running = True
mouse_pointer_drawing = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT // 2

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    draw_line((x,y), points[points_count])

    x, y = points[points_count]
    points_count += 1
    delay(0.5)

    if points_count == 9:
        close_canvas()

close_canvas()