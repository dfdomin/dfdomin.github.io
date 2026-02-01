#!/usr/bin/env python3
"""
Demo script showing how the Python Array Game works
This simulates a full game session with example questions
"""

import random

# Set seed for reproducible demo
random.seed(12345)

print("=" * 60)
print("    DEMO: Python Array Learning Game")
print("=" * 60)
print()
print("This demo shows how the game works:")
print()

# Demo arrays and questions
demos = [
    {
        "func": "len()",
        "array": [12, 5, 8, 19, 3, 15],
        "question": "¿Cuál es la longitud del array?",
        "answer": 6,
        "explanation": "len() devuelve la cantidad de elementos"
    },
    {
        "func": "sum()",
        "array": [4, 7, 2, 9, 3],
        "question": "¿Cuál es la suma de todos los elementos?",
        "answer": 25,
        "explanation": "sum() suma todos los elementos del array"
    },
    {
        "func": "min()",
        "array": [15, 3, 8, 12, 5, 20],
        "question": "¿Cuál es el valor mínimo del array?",
        "answer": 3,
        "explanation": "min() devuelve el elemento más pequeño"
    },
    {
        "func": "max()",
        "array": [7, 19, 4, 15, 11],
        "question": "¿Cuál es el valor máximo del array?",
        "answer": 19,
        "explanation": "max() devuelve el elemento más grande"
    },
    {
        "func": "index()",
        "array": [10, 20, 30, 40, 50],
        "value": 30,
        "question": "¿En qué posición (índice) se encuentra el valor 30?",
        "answer": 2,
        "explanation": "El índice de 30 es 2 (los índices empiezan en 0)"
    }
]

for i, demo in enumerate(demos, 1):
    print("-" * 60)
    print(f"PREGUNTA {i} - Función: {demo['func']}")
    print("-" * 60)
    arr_str = "[" + ", ".join(map(str, demo['array'])) + "]"
    print(f"\nArray: {arr_str}")
    print(f"\n{demo['question']}")
    
    if 'value' in demo:
        print(f"(Buscando el valor {demo['value']})")
    
    print(f"\nRespuesta correcta: {demo['answer']}")
    print(f"✓ {demo['explanation']}")
    print()

print("=" * 60)
print("PUNTUACIÓN FINAL: 5/5")
print("🌟 ¡PERFECTO! ¡Dominas completamente los arrays en Python!")
print("Porcentaje: 100%")
print("=" * 60)
print()
print("Para jugar de verdad, ejecuta:")
print("  python3 python_array_game.py")
print()
