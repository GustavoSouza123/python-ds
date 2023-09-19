""" algoritmo para resolver o quebra-cabeça do site countle.org """

result = int(input("Entre com o resultado da expressão: "))
nums = []
for i in range(6):
    nums.append(int(input(f"Entre com o {i+1}º número da expressão: ")))

for cont in range(4):
    if cont == 0:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == result:
                    print("Você acertou!")
                    print(f"{nums[i]} + {nums[j]} = {result}")
    elif cont == 1:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] - nums[j] == result:
                    print("Você acertou!")
                    print(f"{nums[i]} - {nums[j]} = {result}")
    elif cont == 2:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] * nums[j] == result:
                    print("Você acertou!")
                    print(f"{nums[i]} * {nums[j]} = {result}")
    elif cont == 3:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] != 0 and nums[j] != 0:
                    if nums[i] / nums[j] == result:
                        print("Você acertou!")
                        print(f"{nums[i]} / {nums[j]} = {result}")