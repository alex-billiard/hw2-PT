import math

a = math.factorial(5000) / (math.factorial(0) * math.factorial(5000)) * (0.0004 ** 0) * (0.9996 ** 5000)
print(f"Ответ: {a * 100} процента(ов)")

b = math.factorial(5000) / (math.factorial(2) * math.factorial(4998)) * (0.0004 ** 2) * (0.9996 ** 4998)
print(f"Ответ: {b * 100} процента(ов)")

a1 = (2 ** 0) / math.factorial(0) * (math.e ** -2)
print(f"Ответ: {a1 * 100} процента(ов)")

b1 = (2 ** 2) / math.factorial(2) * (math.e ** -2)
print(f"Ответ: {b1 * 100} процента(ов)")