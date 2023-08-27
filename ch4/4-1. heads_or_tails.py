# Random 모듈을 이용하여 동전 앞 뒷면 표시

import random

random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")