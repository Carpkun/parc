#max()를 쓰지않고 반복문만을 사용해서 리스트내 최대값 구하기

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_score = 0
for score in student_scores:
  if max_score < score:
    max_score = score
#   else:
#     max_score = max_score
print(f"The highest score in the class is: {max_score}")


  

