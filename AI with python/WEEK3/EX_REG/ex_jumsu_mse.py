# ==================================================
# Linear Regression 실습 - (3) 오차/손실(Cost, Loss)함수
# MSE 함수 사용
# ==================================================
# 모듈 로딩 ------------------------------------------
import numpy as np

# 전역변수 선언 -----------------------------------------
# (1) 데이터 준비
x=[2, 4, 6, 8, 10]         # 시간 데이터
y=[81, 89, 93, 91, 97]     # 점수 데이터

# (2) 가상의 기울기 w와 절편 b
fake_w_b=[2.1,77]          # 임의의 값

# 함수 선언 --------------------------------------------
# y=wx + b 대입 결과 출력하는 함수 (예측함수)
def predict(x):
   return fake_w_b[0]*x + fake_w_b[1]

# 오차 계산 함수
def mse(predict_result,y):
   return ((predict_result - y) ** 2).mean()

# 각 y값에 대입한 최종 오차 값 계산 함수
def mse_val(predict_result,y):
   return mse( np.array(predict_result),np.array(y) )

# 기능 구현 ----------------------------------------------
# 예측값이 들어갈 빈 리스트
predict_result = []

# x값에 대한 예측값 계산 및 출력 ----------------------------
for i in range(len(x)):
   predict_result.append( predict(x[i]) )
   print("공부시간=%.f, 실제점수=%.f, 예측점수=%.f"
         %(x[i], y[i], predict(x[i])))

# 최종 MSE 출력
print("MSE 최종값: " + str(mse_val(predict_result, y)))


# # 평균제곱오차 계산 함수 --------------------------------
# 오차 계산 MSE 함수
def mse(predict_result,y):
   return ((predict_result - y) ** 2).mean()

# MSE 함수를 각 y값에 대입하여 최종 값을 구하는 함수
def mse_val(predict_result,y):
   return mse( np.array(predict_result),np.array(y) )

def getMSE(predict_result, y):
   return mse_val(predict_result, y)





