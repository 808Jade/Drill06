from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse_pointer = load_image('hand_arrow.png')

points = []  # 클릭한 점을 저장할 리스트
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2  # 초기 위치 설정

def lerp(p1, p2, t):
    # 선형 보간 함수
    return (1 - t) * p1 + t * p2

def draw_line(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    global frame

    for i in range(0, 100 + 1, 3):
        t = i / 100
        x = lerp(x1, x2, t)
        y = lerp(y1, y2, t)
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

        # 모든 클릭한 점에 마우스 커서 이미지 그리기
        for point in points:
            mx, my = point
            mouse_pointer.draw(mx, my)

        # 캐릭터 그리기
        if points:
            mx, my = points[0]
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

def handle_events():
    global running
    global points
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_pointer.draw_now(event.x,event.y)
            # mx, my = event.x, TUK_HEIGHT - 1 - event.y
            # mx, my = event.x, TUK_HEIGHT - event.y - 1  # Y 좌표 계산 수정
            # if points:
            #     points[0] = (mx, my)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            mx, my = event.x, TUK_HEIGHT - event.y - 1  # Y 좌표 계산 수정
            points.append((mx, my))

running = True
# hide_cursor()

while running:
    handle_events()
    if points:
        # 클릭한 점이 있을 때, 커서 이미지 그리기
        mx, my = points[0]

        clear_canvas()  # 커서를 그리기 전에 화면을 지워줍니다.
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

        # 모든 클릭한 점에 마우스 커서 이미지 그리기
        for point in points:
            mx, my = point
            mouse_pointer.draw(mx, my)

        draw_line((x, y), points[0])
        x, y = points[0]
        if x == points[0][0] and y == points[0][1]:
            points.pop(0)  # 첫 번째 클릭한 점에 도달하면 제거
        update_canvas()
        delay(0.01)
    else:
        # 클릭한 점이 없는 경우, 캐릭터는 현재 위치에서 대기합니다.
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        character.clip_draw(frame * 66, 198, 66, 66, x, y, 150, 150)
        frame = (frame + 1) % 4
        update_canvas()
        delay(0.03)

close_canvas()
