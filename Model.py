import matplotlib.pyplot as plt
import numpy as np

Height_1step = []
Height_2step = []
time_1step = 200  # время работы первой ступени
time_2step = 100  # время работы первой ступени
mass_takeoff = 90_000  # взлётная масса
mass_n1step = 19_000  # масса без 1 ступени
fuel_1step = 374_000 * 4  # в первой ступени было 4 двигателя
fuel_2step = 374_000  # вторая ступень
LossFuel_1step = 325  # скороть расхода массы первой ступени
LossFuel_2step = 81.25  # скороть расхода массы второй ступени
RotationSpeed_1step = -0.001  # скорость повортота ракеты на 1 ступени рад/с
RotationSpeed_2step = -0.024  # скорость повортота ракеты на 2 ступени
CoefficientResistance = 0.8  # (с потолка) коэф сопростивления(надо обЪем)
SurfaceResistance = 2_712 ** (2 / 3)  # площадь лобового сопротивления(примерное, пусть ракета просто цилиндр)

TimeO = 0.1  # отрезок времяни равное 0.1 с
angle_1 = np.pi / 2
angle_2 = angle_1 + time_1step * RotationSpeed_1step
g = 9.81
ma = 0.029
r = 8.31
temp = 300
SteamPressure = 101_300
GasConstant = ma / (r * temp)

xVals = [0]
yVals = [0]
vxVals = [0]
vyVals = [0]
axVals = [0]
ayVals = [-9.81]

x = 0
y = 0
vx = 0
vy = 0
ax = 0
ay = 0

for i in range(int(time_1step // TimeO)):  # рассчитываем n секунд шагов первой ступени
    t = i * TimeO
    rho = (GasConstant * SteamPressure) * np.exp((-g * y * GasConstant))
    f_cx = CoefficientResistance * SurfaceResistance * (rho * (vxVals[-1] ** 2) * 0.5)
    f_cy = CoefficientResistance * SurfaceResistance * (rho * (vyVals[-1] ** 2) * 0.5)
    ax = (fuel_1step * np.cos(angle_1 + RotationSpeed_1step * t) - f_cx) / (mass_takeoff - LossFuel_1step * t)
    ay = (fuel_1step * np.sin(angle_1 + RotationSpeed_1step * t) - f_cy) / (mass_takeoff - LossFuel_1step * t) - g
    vx = vxVals[-1] + ax * TimeO
    vy = vyVals[-1] + ay * TimeO
    x = xVals[-1] + vx * TimeO
    y = yVals[-1] + vy * TimeO
    axVals.append(ax)
    ayVals.append(ay)
    vxVals.append(vx)
    vyVals.append(vy)
    xVals.append(x)
    yVals.append(y)


for i in range(int(time_2step // TimeO)):  # рассчитываем n секунд шагов второй ступени
    t = i * TimeO
    rho = (GasConstant * SteamPressure) * np.exp((-g * y * GasConstant))
    f_cx = CoefficientResistance * SurfaceResistance * (rho * (vxVals[-1] ** 2) * 0.5)
    f_cy = CoefficientResistance * SurfaceResistance * (rho * (vyVals[-1] ** 2) * 0.5)
    ax = (fuel_2step * np.cos(angle_2 + RotationSpeed_2step * t) - f_cx) / (mass_n1step - LossFuel_2step * t)
    ay = (fuel_2step * np.sin(angle_2 + RotationSpeed_2step * t) - f_cy) / (mass_n1step - LossFuel_2step * t) - g
    vx = vxVals[-1] + ax * TimeO
    vy = vyVals[-1] + ay * TimeO
    x = xVals[-1] + vx * TimeO
    y = yVals[-1] + vy * TimeO
    axVals.append(ax)
    ayVals.append(ay)
    vxVals.append(vx)
    vyVals.append(vy)
    xVals.append(x)
    yVals.append(y)

velocity = [((vxVals[i]) ** 2 + vyVals[i] ** 2) ** 0.5 for i in range(len(vxVals))]

#plt.plot(range(0, time_1step+time_2step), vxVals[::int(TimeO ** -1)])
plt.xlabel("Время, с")
plt.ylabel("Скорость, м/с")
#plt.plot(range(0, time_1step+time_2step), vyVals[::int(TimeO ** -1)])
#plt.plot(range(0, time_1step + 1), velocity[::int(TimeO ** -1)][:time_1step + 1])
plt.plot(range(0, time_2step), velocity[::int(TimeO ** -1)][time_1step:time_1step+time_2step])
plt.show()