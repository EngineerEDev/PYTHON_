import random

# 🔹 Sin semilla → resultados diferentes cada vez
print("🎲 Números aleatorios SIN semilla:")
for _ in range(5):
    print(random.randint(1, 6))

print("\n🎲 Números aleatorios CON semilla (42):")
random.seed(42)  # fijamos la semilla
for _ in range(5):
    print(random.randint(1, 6))
##se utiliza "_" cuando no se va a utilizar la variable del ciclo

