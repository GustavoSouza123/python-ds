paisA = 80000
paisB = 200000
anos = 0

while paisA < paisB:
    anos += 1
    paisA += paisA * 0.03
    paisB += paisB * 0.015

print(f"\nSão necessários {anos} anos para a população do país A ultrapassar ou igualar a população do país B")