import pygame, math, sys, numpy, point, point_d
from pygame.time import Clock

pygame.init()
display_width, display_height = 600, 600 # 창 크기 설정(display_width = 가로, display_height = 세로)
display = pygame.display.set_mode((display_width, display_height)) 
clock = pygame.time.Clock() # 시간 설정
fps = 100 #fps 성정
anglem = math.pi / 180

# 모델 수치 세팅
axis_h = 150 # 회전축 높이
height_list = [270, 240, 210, 180, 150, 120, 90, 60, 30, 0] # 잎 높이 리스트
size_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # 잎 크기 리스트
angle_list = [1375.0, 1237.5, 1100.0, 962.5, 825.0, 687.5, 550.0, 412.5, 275.0, 137.5] # 잎 각 리스트 (회전축에 수직한 축 기준 시계방향 각)
model_angle = -math.pi / 2
pixel = 600 # 가로 세로 격자 수 설정

# 모델 회전, 사영 좌표 반환 함수
def rotate(angle, leaflist):
    RotateMatrix = numpy.array([[1, 0, 0], 
                            [0, math.cos(angle), -math.sin(angle)], 
                            [0, math.sin(angle), math.cos(angle)]])
    a = []
    for i in range(len(leaflist)):
        b = []
        for j in range(4):
            leaf = numpy.array(leaflist[i][j])
            leaf = RotateMatrix.dot(leaf)
            b.append([int(leaf[0]) + pixel // 2, -int(leaf[1]) + pixel // 2])
        a.append(b)
    return a

# panel 클래스
class panel:
    def __init__(self, n, dotlist):
        self.dotlist = dotlist
        self.n = n
    def main(self):
        pygame.draw.polygon(display, (255, 255, 255), self.dotlist)
        pygame.draw.lines(display, (0, 0, 0), True, self.dotlist, 2)
    def rotate(self, l):
        self.dotlist = l[self.n]

# 시뮬레이션 실행 함수
def run(model,Rleaflist, leaflist):
    global model_angle
    # s = ''
    sum = 0
    while True:
        # 화면을 초기화
        display.fill((0,0,0))

        # 모델 회전, 화면에 blit
        Rleaflist = rotate(model_angle, leaflist) 
        for i in model:
            i.rotate(Rleaflist)
            i.main()

        # 마우스 이벤트 감지
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT
        
        # # 키 이벤트 감지
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]:# up키를 누르면 모델이 위로 회전
        #     model_angle += anglem
        # if keys[pygame.K_DOWN]:# down키를 누르면 모뎅이 아래로 회전
        #     model_angle -= anglem
        
        model_angle += anglem # 모델 자동 회전
        
        # 모델의 흰색 영역 격자점 수(넓이) 측정
        # Wcount = 0
        for i in range(600):
            for j in range(600):
                color = display.get_at((i,j))
                if color == (255,255,255):
                    # Wcount += 1
                    sum += 1
        # s += f'{Wcount}\n' # 모델의 사영 넓이를 출력

        # 시뮬레이션 종료
        if model_angle > math.pi / 2:
            print(sum/180)
            break

        # 화면 업데이트
        clock.tick(fps)
        pygame.display.update()

#기본
# leaflist_o = [[[[100], [100], [0]], [[100], [-100], [0]], [[-100], [-100], [0]], [[-100], [100], [0]]]]

# # 황금각
# leaflist_g = [[[[0], [0], [-150]], [[-99], [-4], [-150]], [[-104], [95], [-150]], [[-4], [99], [-150]]],
#             [[[0], [0], [-120]], [[68], [-57], [-120]], [[11], [-126], [-120]], [[-57], [-68], [-120]]],
#             [[[0], [0], [-90]], [[-10], [79], [-90]], [[68], [89], [-90]], [[79], [10], [-90]]],
#             [[[0], [0], [-60]], [[-40], [-57], [-60]], [[-97], [-17], [-60]], [[-57], [40], [-60]]],
#             [[[0], [0], [-30]], [[58], [12], [-30]], [[71], [-45], [-30]], [[12], [-58], [-30]]],
#             [[[0], [0], [0]], [[-43], [25], [0]], [[-18], [68], [0]], [[25], [43], [0]]],
#             [[[0], [0], [30]], [[12], [-38], [30]], [[-26], [-50], [30]], [[-38], [-12], [30]]],
#             [[[0], [0], [60]], [[12], [27], [60]], [[39], [14], [60]], [[27], [-12], [60]]],
#             [[[0], [0], [90]], [[-18], [-7], [90]], [[-26], [10], [90]], [[-7], [18], [90]]],
#             [[[0], [0], [120]], [[9], [-3], [120]], [[5], [-12], [120]], [[-3], [-9], [120]]]]

# #루카스 각
# leaflist_l = [[[[0], [0], [-150]], [[-81], [58], [-150]], [[-23], [139], [-150]], [[58], [81], [-150]]],
#             [[[0], [0], [-120]], [[-39], [-80], [-120]], [[-120], [-41], [-120]], [[-80], [39], [-120]]],
#             [[[0], [0], [-90]], [[76], [-22], [-90]], [[53], [-99], [-90]], [[-22], [-76], [-90]]],
#             [[[0], [0], [-60]], [[8], [69], [-60]], [[78], [60], [-60]], [[69], [-8], [-60]]],
#             [[[0], [0], [-30]], [[-59], [-2], [-30]], [[-62], [57], [-30]], [[-2], [59], [-30]]],
#             [[[0], [0], [0]], [[10], [-48], [0]], [[-38], [-59], [0]], [[-48], [-10], [0]]],
#             [[[0], [0], [30]], [[37], [14], [30]], [[51], [-22], [30]], [[14], [-37], [30]]],
#             [[[0], [0], [60]], [[-15], [25], [60]], [[10], [41], [60]], [[25], [15], [60]]],
#             [[[0], [0], [90]], [[-15], [-12], [90]], [[-28], [2], [90]], [[-12], [15], [90]]],
#             [[[0], [0], [120]], [[7], [-6], [120]], [[1], [-14], [120]], [[-6], [-7], [120]]]]

# # 제1 변칙 시퀀스
# leaflist_1s = [[[[0], [0], [-150]], [[-96], [-27], [-150]], [[-123], [68], [-150]], [[-27], [96], [-150]]],
#                 [[[0], [0], [-120]], [[87], [-19], [-120]], [[67], [-107], [-120]], [[-19], [-87], [-120]]],
#                 [[[0], [0], [-90]], [[-59], [53], [-90]], [[-6], [112], [-90]], [[53], [59], [-90]]],
#                 [[[0], [0], [-60]], [[23], [-65], [-60]], [[-42], [-89], [-60]], [[-65], [-23], [-60]]],
#                 [[[0], [0], [-30]], [[9], [59], [-30]], [[68], [49], [-30]], [[59], [-9], [-30]]],
#                 [[[0], [0], [0]], [[-30], [-39], [0]], [[-70], [-8], [0]], [[-39], [30], [0]]],
#                 [[[0], [0], [30]], [[36], [15], [30]], [[52], [-21], [30]], [[15], [-36], [30]]],
#                 [[[0], [0], [60]], [[-29], [3], [60]], [[-26], [32], [60]], [[3], [29], [60]]],
#                 [[[0], [0], [90]], [[16], [-11], [90]], [[5], [-27], [90]], [[-11], [-16], [90]]],
#                 [[[0], [0], [120]], [[-4], [8], [120]], [[4], [13], [120]], [[8], [4], [120]]]]

# # 말도 안되는 각(30)
# leaflist_30 = [[[[0], [0], [-150]], [[25], [96], [-150]], [[122], [70], [-150]], [[96], [-25], [-150]]],
#                 [[[0], [0], [-120]], [[-23], [86], [-120]], [[63], [110], [-120]], [[86], [23], [-120]]],
#                 [[[0], [0], [-90]], [[-56], [56], [-90]], [[0], [113], [-90]], [[56], [56], [-90]]],
#                 [[[0], [0], [-60]], [[-67], [18], [-60]], [[-49], [85], [-60]], [[18], [67], [-60]]],
#                 [[[0], [0], [-30]], [[-57], [-15], [-30]], [[-73], [42], [-30]], [[-15], [57], [-30]]],
#                 [[[0], [0], [0]], [[-35], [-35], [0]], [[-70], [0], [0]], [[-35], [35], [0]]],
#                 [[[0], [0], [30]], [[-10], [-38], [30]], [[-48], [-28], [30]], [[-38], [10], [30]]],
#                 [[[0], [0], [60]], [[7], [-28], [60]], [[-21], [-36], [60]], [[-28], [-7], [60]]],
#                 [[[0], [0], [90]], [[14], [-14], [90]], [[0], [-28], [90]], [[-14], [-14], [90]]],
#                 [[[0], [0], [120]], [[9], [-2], [120]], [[7], [-12], [120]], [[-2], [-9], [120]]]]

# # 회전, 사영 좌표 저장
# Rleaflist_o = rotate(model_angle, leaflist_o)
# Rleaflist_g = rotate(model_angle, leaflist_g)
# Rleaflist_l = rotate(model_angle, leaflist_l)
# Rleaflist_1s = rotate(model_angle, leaflist_1s)
# Rleaflist_30 = rotate(model_angle, leaflist_30)

# # 모델 생성
# model_o = [panel(0, Rleaflist_o[0])]

# model_g = []
# for i in range(10):
#     model_g.append(panel(i, Rleaflist_g[i]))

# model_l = []
# for i in range(10):
#     model_l.append(panel(i, Rleaflist_l[i]))

# model_1s = []
# for i in range(10):
#     model_1s.append(panel(i, Rleaflist_1s[i]))

# model_30 = []
# for i in range(10):
#     model_30.append(panel(i, Rleaflist_30[i]))

# 모델 생성함수
def MakeModel(model_angle, angle):
    leaflist = point.vertex(angle)
    Rleaflist = rotate(model_angle, leaflist)
    model = []
    for i in range(len(leaflist)):
        model.append(panel(i, Rleaflist[i]))
    return [model, Rleaflist, leaflist]

def MakeModel_r(model_angle, angle, r, S):
    leaflist = point_r.vertex(angle, r, S)
    Rleaflist = rotate(model_angle, leaflist)
    model = []
    for i in range(len(leaflist)):
        model.append(panel(i, Rleaflist[i]))
    return [model, Rleaflist, leaflist]

def MakeModel_d(model_angle, angle, d, S):
    leaflist = point_d.vertex(angle, d, S)
    Rleaflist = rotate(model_angle, leaflist)
    model = []
    for i in range(len(leaflist)):
        model.append(panel(i, Rleaflist[i]))
    return [model, Rleaflist, leaflist]

for i in range(137,139):
    j = MakeModel_d(model_angle, i, 10, 38500)
    run(j[0], j[1], j[2])
    model_angle = -math.pi / 2