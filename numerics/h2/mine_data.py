import numpy as np
import os
import subprocess
import sys
import matplotlib.pyplot as plt

# 스타일 파일 경로 추가
sys.path.append('/home/mmotta/QITE/imag_time_for_qcomp/code_v4/')
import style as st  # 스타일 모듈 (이 파일이 있어야 함)

# 출력 파일 설정
fname = 'h2.eps'

# 데이터 크기 설정
nb = 400  # b 축 데이터 개수
nr = 54   # R 축 데이터 개수

# 데이터 로드
my_data = np.genfromtxt('h2_surf.dat', skip_header=0)
R = my_data[:, 0]  # R 값
b = my_data[:, 1]  # b 값
E = my_data[:, 2]  # E 값

# 데이터 일부 출력 확인
print(R[:10])
print(b[:10])
print(E[:10])

# Figure 설정
x0 = 7.00
xfig = 1.00 * 1 * x0
yfig = 0.75 * 1 * x0

fig, pan = plt.subplots(1, 1, figsize=(xfig, yfig))

# Tick 설정
pan.get_xaxis().set_tick_params(which='both', direction='in', labelsize=18)
pan.get_yaxis().set_tick_params(which='both', direction='in', labelsize=18)

# 축 라벨 설정
pan.set_xlabel(r'$\displaystyle{R \, [\AA]}$', fontsize=18)
pan.set_ylabel(r'$\displaystyle{E(\beta) \, \big[\mathrm{E_{Ha}}\big]}$', fontsize=18)

# x, y 축 범위 설정
pan.set_xlim([-0.2, 3.2])
pan.set_ylim([-1.2001, 0.2])

# 데이터 시각화 (FCI 데이터)
u = [R[nb * x] for x in range(nr)]
v = [E[nb - 1 + nb * x] for x in range(nr)]
st.Palette[st.fci].dataplot(pan, u, v, spline=False, connected=True)

# 다양한 β 값에 대한 데이터 플롯
mu = 16
for ib in [0, 100, 200, 300]:
    u = [R[nb * x] for x in range(nr)]
    v = [E[ib + nb * x] for x in range(nr)]
    st.Palette[mu].dataplot(pan, u, v, spline=False, connected=True)
    mu += 1

# 그래프 레이블 추가
plt.text(2.4, -0.03, r'$(d)$', fontsize=21)

# 범례 추가
x0, dx = -0.035, 1.07
y0, dy = 1.00, 0.10
order = [0, 1, 2, 3, 4]
lgd = st.make_legend(pan, order, ncol=5, bbox_to_anchor=(x0, y0, dx, dy),
                     loc=3, mode="expand", borderaxespad=1, fontsize=13, handlelength=2.5, numpoints=2)

# EPS 파일 저장
fig.savefig(fname, format='eps', bbox_inches='tight')

# EPS 파일 변환
os.system(f'ps2epsi {fname}')
os.system(f'mv {fname}i {fname}')
