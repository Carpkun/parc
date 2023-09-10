# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# 쓰기 모드
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# 기존 내용을 삭제하지 않고 추가하기 모드
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")