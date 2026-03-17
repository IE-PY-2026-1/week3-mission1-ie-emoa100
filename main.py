# 파일이름 :
# 작 성 자 :

# 1. 사용자로부터 데이터 입력 받기 및 형변환
# input()은 모든 입력을 문자열로 받으므로 계산을 위해 int와 float로 변환
name7 = input("당신 이름을 입력하시오: ")
write7 = int(input("당신의 글쓰기 점수를 입력하시오: "))
python7 = int(input("당신의 파이썬 점수를 입력하시오: "))
lastAverage7 = float(input("당신의 지난학기 평균을 입력하시오: "))

# 2. 성적 분석 로직 구현
average7 = (write7 + python7) / 2    # 현재 평균 계산
diff7 = average7 - lastAverage7      # 지난 학기 평균과의 차이 계산

# 3. f-string을 이용한 결과 출력
print(f"\n{name7} 학생의 글쓰기 점수는 {write7}, 파이썬 점수는 {python7} 입니다.")
print(f"평균은 {average7} 이고, 지난 학기와 차이는 {diff7} 입니다.")

