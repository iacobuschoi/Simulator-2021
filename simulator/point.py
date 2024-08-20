import math
# 모델 수치 세팅
axis_h = 150 # 회전축 높이
height_list = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270] # 잎 높이 리스트
for i in range(10):
    height_list[i]-=axis_h
size_list = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10] # 잎 크기 리스트
angle_list = [30*i for i in range(1,11)] # 잎 각 리스트 (회전축에 수직한 축 기준 시계방향 각)
vertex_list=[0]*10
for i in range(10):
    vertex_list[i]=[]
    vertex_list[i]=[[0,0,height_list[i]],[size_list[i]*math.cos((angle_list[i]+45)/180*math.pi),size_list[i]*math.sin((angle_list[i]+45)/180*math.pi),height_list[i]],[size_list[i]*2**0.5*math.cos(angle_list[i]/180*math.pi),size_list[i]*2**0.5*math.sin(angle_list[i]/180*math.pi),height_list[i]],[size_list[i]*math.cos((angle_list[i]-45)/180*math.pi),size_list[i]*math.sin((angle_list[i]-45)/180*math.pi),height_list[i]]] #좌표값 계산

for i in range(10):
    for j in range(4):
        for k in range(3):
            vertex_list[i][j][k]=int(vertex_list[i][j][k]) #정수로 만드는 함수
for i in range(10):
    for j in range(4):
        for k in range(3):
            vertex_list[i][j][k]=[vertex_list[i][j][k]]
