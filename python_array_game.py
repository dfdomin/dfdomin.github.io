#!/usr/bin/env python3
"""
Python Array Learning Game
===========================
A game to help students learn and verify their understanding of Python array methods:
len(), sum(), min(), max(), and index()

Author: Diego Fabián Domínguez Tapia
"""

import random
import sys


def add_spacing():
    """Add spacing between sections for better readability"""
    print("\n" * 2)


def print_separator():
    """Print a visual separator"""
    print("=" * 60)


def print_array(arr):
    """Print an array in a readable format"""
    return f"[{', '.join(map(str, arr))}]"


def generate_random_array(min_size=3, max_size=8, min_val=1, max_val=20):
    """Generate a random array for testing"""
    size = random.randint(min_size, max_size)
    return [random.randint(min_val, max_val) for _ in range(size)]


def ask_len_question():
    """Ask a question about len()"""
    arr = generate_random_array()
    print(f"\nArray: {print_array(arr)}")
    print(f"\n¿Cuál es la longitud del array? (usa len())")
    
    try:
        answer = int(input("Tu respuesta: "))
        correct = len(arr)
        
        if answer == correct:
            print("✓ ¡Correcto! len() devuelve la cantidad de elementos.")
            return True
        else:
            print(f"✗ Incorrecto. La respuesta correcta es {correct}")
            print(f"  len({print_array(arr)}) = {correct}")
            return False
    except ValueError:
        print("✗ Por favor, ingresa un número válido.")
        return False


def ask_sum_question():
    """Ask a question about sum()"""
    arr = generate_random_array(min_size=3, max_size=6)
    print(f"\nArray: {print_array(arr)}")
    print(f"\n¿Cuál es la suma de todos los elementos? (usa sum())")
    
    try:
        answer = int(input("Tu respuesta: "))
        correct = sum(arr)
        
        if answer == correct:
            print("✓ ¡Correcto! sum() suma todos los elementos del array.")
            return True
        else:
            print(f"✗ Incorrecto. La respuesta correcta es {correct}")
            print(f"  sum({print_array(arr)}) = {correct}")
            return False
    except ValueError:
        print("✗ Por favor, ingresa un número válido.")
        return False


def ask_min_question():
    """Ask a question about min()"""
    arr = generate_random_array()
    print(f"\nArray: {print_array(arr)}")
    print(f"\n¿Cuál es el valor mínimo del array? (usa min())")
    
    try:
        answer = int(input("Tu respuesta: "))
        correct = min(arr)
        
        if answer == correct:
            print("✓ ¡Correcto! min() devuelve el elemento más pequeño.")
            return True
        else:
            print(f"✗ Incorrecto. La respuesta correcta es {correct}")
            print(f"  min({print_array(arr)}) = {correct}")
            return False
    except ValueError:
        print("✗ Por favor, ingresa un número válido.")
        return False


def ask_max_question():
    """Ask a question about max()"""
    arr = generate_random_array()
    print(f"\nArray: {print_array(arr)}")
    print(f"\n¿Cuál es el valor máximo del array? (usa max())")
    
    try:
        answer = int(input("Tu respuesta: "))
        correct = max(arr)
        
        if answer == correct:
            print("✓ ¡Correcto! max() devuelve el elemento más grande.")
            return True
        else:
            print(f"✗ Incorrecto. La respuesta correcta es {correct}")
            print(f"  max({print_array(arr)}) = {correct}")
            return False
    except ValueError:
        print("✗ Por favor, ingresa un número válido.")
        return False


def ask_index_question():
    """Ask a question about index()"""
    # Generate array and ensure we pick a unique value for the question
    arr = generate_random_array()
    
    # Get unique values from the array
    unique_values = []
    seen_indices = set()
    for i, val in enumerate(arr):
        if val not in [arr[j] for j in seen_indices]:
            unique_values.append(val)
            seen_indices.add(i)
    
    # If we have unique values, pick one; otherwise use any element
    if unique_values:
        element = random.choice(unique_values)
    else:
        element = random.choice(arr)
    
    print(f"\nArray: {print_array(arr)}")
    print(f"\n¿En qué posición (índice) se encuentra el valor {element}?")
    print(f"(usa index() - recuerda que los índices empiezan en 0)")
    
    try:
        answer = int(input("Tu respuesta: "))
        correct = arr.index(element)
        
        if answer == correct:
            print(f"✓ ¡Correcto! El índice de {element} es {correct}.")
            return True
        else:
            print(f"✗ Incorrecto. La respuesta correcta es {correct}")
            print(f"  {print_array(arr)}.index({element}) = {correct}")
            return False
    except ValueError:
        print("✗ Por favor, ingresa un número válido.")
        return False


def play_game():
    """Main game loop"""
    print_separator()
    print("         JUEGO DE ARRAYS EN PYTHON")
    print_separator()
    print("\n¡Bienvenido al juego de aprendizaje de arrays!")
    print("\nVas a responder preguntas sobre:")
    print("  • len()   - Obtener la longitud del array")
    print("  • sum()   - Sumar todos los elementos")
    print("  • min()   - Encontrar el valor mínimo")
    print("  • max()   - Encontrar el valor máximo")
    print("  • index() - Encontrar la posición de un elemento")
    print("\nCada respuesta correcta suma 1 punto.")
    print_separator()
    
    input("\nPresiona Enter para comenzar...")
    
    # Define question types
    question_functions = [
        ("len()", ask_len_question),
        ("sum()", ask_sum_question),
        ("min()", ask_min_question),
        ("max()", ask_max_question),
        ("index()", ask_index_question)
    ]
    
    # Shuffle questions for variety
    random.shuffle(question_functions)
    
    score = 0
    total_questions = len(question_functions)
    
    for i, (func_name, question_func) in enumerate(question_functions, 1):
        add_spacing()
        print_separator()
        print(f"  PREGUNTA {i} de {total_questions} - Función: {func_name}")
        print_separator()
        
        if question_func():
            score += 1
        
        print(f"\nPuntuación actual: {score}/{i}")
        
        if i < total_questions:
            input("\nPresiona Enter para la siguiente pregunta...")
    
    # Final results
    add_spacing()
    print_separator()
    print("           RESULTADOS FINALES")
    print_separator()
    print(f"\nPuntuación final: {score}/{total_questions}")
    
    percentage = (score / total_questions) * 100
    
    if percentage == 100:
        print("\n🌟 ¡PERFECTO! ¡Dominas completamente los arrays en Python!")
    elif percentage >= 80:
        print("\n🎉 ¡Muy bien! Tienes un buen conocimiento de arrays.")
    elif percentage >= 60:
        print("\n👍 ¡Bien! Pero puedes mejorar con más práctica.")
    else:
        print("\n📚 Necesitas repasar más sobre arrays. ¡Sigue practicando!")
    
    print(f"\nPorcentaje: {percentage:.0f}%")
    print_separator()


def show_menu():
    """Show main menu"""
    while True:
        print_separator()
        print("    MENÚ PRINCIPAL - Juego de Arrays Python")
        print_separator()
        print("\n1. Jugar")
        print("2. Ver ayuda sobre las funciones")
        print("3. Salir")
        print()
        
        choice = input("Selecciona una opción (1-3): ").strip()
        
        if choice == "1":
            play_game()
            input("\n\nPresiona Enter para volver al menú...")
            add_spacing()
        elif choice == "2":
            show_help()
            input("\n\nPresiona Enter para volver al menú...")
            add_spacing()
        elif choice == "3":
            print("\n¡Gracias por jugar! ¡Hasta luego!")
            print_separator()
            sys.exit(0)
        else:
            print("\n✗ Opción inválida. Por favor, selecciona 1, 2 o 3.")


def show_help():
    """Display help about array functions"""
    add_spacing()
    print_separator()
    print("           AYUDA - FUNCIONES DE ARRAYS")
    print_separator()
    
    print("\n1. len(array) - Longitud del array")
    print("   Devuelve el número de elementos en el array.")
    print("   Ejemplo: len([1, 2, 3, 4, 5]) = 5")
    
    print("\n2. sum(array) - Suma de elementos")
    print("   Devuelve la suma de todos los elementos.")
    print("   Ejemplo: sum([1, 2, 3, 4, 5]) = 15")
    
    print("\n3. min(array) - Valor mínimo")
    print("   Devuelve el elemento más pequeño del array.")
    print("   Ejemplo: min([5, 2, 8, 1, 9]) = 1")
    
    print("\n4. max(array) - Valor máximo")
    print("   Devuelve el elemento más grande del array.")
    print("   Ejemplo: max([5, 2, 8, 1, 9]) = 9")
    
    print("\n5. array.index(value) - Índice de un elemento")
    print("   Devuelve la posición (índice) de un valor en el array.")
    print("   Los índices empiezan en 0.")
    print("   Ejemplo: [10, 20, 30, 40].index(30) = 2")
    
    print_separator()


def main():
    """Entry point of the program"""
    try:
        add_spacing()
        show_menu()
    except KeyboardInterrupt:
        print("\n\n¡Juego interrumpido! ¡Hasta luego!")
        print_separator()
        sys.exit(0)


if __name__ == "__main__":
    main()
