#!/usr/bin/env python3
"""
Number Systems Practice Script

This script generates random practice problems for number system conversions
and provides solutions. Great for self-study and testing your knowledge.
"""

import random
import sys

def decimal_to_binary(decimal):
    """Convert decimal to binary using repeated division."""
    if decimal == 0:
        return "0"
    
    binary = ""
    num = decimal
    
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    
    return binary

def binary_to_decimal(binary):
    """Convert binary to decimal using positional notation."""
    decimal = 0
    for i, digit in enumerate(reversed(binary)):
        decimal += int(digit) * (2 ** i)
    return decimal

def decimal_to_octal(decimal):
    """Convert decimal to octal using repeated division."""
    if decimal == 0:
        return "0"
    
    octal = ""
    num = decimal
    
    while num > 0:
        remainder = num % 8
        octal = str(remainder) + octal
        num = num // 8
    
    return octal

def octal_to_decimal(octal):
    """Convert octal to decimal using positional notation."""
    decimal = 0
    for i, digit in enumerate(reversed(octal)):
        decimal += int(digit) * (8 ** i)
    return decimal

def decimal_to_hexadecimal(decimal):
    """Convert decimal to hexadecimal using repeated division."""
    if decimal == 0:
        return "0"
    
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    num = decimal
    
    while num > 0:
        remainder = num % 16
        hexadecimal = hex_chars[remainder] + hexadecimal
        num = num // 16
    
    return hexadecimal

def hexadecimal_to_decimal(hexadecimal):
    """Convert hexadecimal to decimal using positional notation."""
    decimal = 0
    hex_chars = "0123456789ABCDEF"
    
    for i, digit in enumerate(reversed(hexadecimal.upper())):
        decimal += hex_chars.index(digit) * (16 ** i)
    return decimal

def binary_to_octal(binary):
    """Convert binary to octal by grouping in threes."""
    # Pad with leading zeros if needed
    while len(binary) % 3 != 0:
        binary = "0" + binary
    
    octal = ""
    for i in range(0, len(binary), 3):
        group = binary[i:i+3]
        decimal_val = binary_to_decimal(group)
        octal += str(decimal_val)
    
    return octal

def binary_to_hexadecimal(binary):
    """Convert binary to hexadecimal by grouping in fours."""
    # Pad with leading zeros if needed
    while len(binary) % 4 != 0:
        binary = "0" + binary
    
    hexadecimal = ""
    hex_chars = "0123456789ABCDEF"
    
    for i in range(0, len(binary), 4):
        group = binary[i:i+4]
        decimal_val = binary_to_decimal(group)
        hexadecimal += hex_chars[decimal_val]
    
    return hexadecimal

def generate_problem():
    """Generate a random practice problem."""
    problem_types = [
        "binary_to_decimal",
        "decimal_to_binary", 
        "octal_to_decimal",
        "decimal_to_octal",
        "hex_to_decimal",
        "decimal_to_hex",
        "binary_to_octal",
        "binary_to_hex"
    ]
    
    problem_type = random.choice(problem_types)
    
    if problem_type == "binary_to_decimal":
        # Generate a random binary number (4-8 bits)
        bits = random.randint(4, 8)
        binary = ''.join(random.choice(['0', '1']) for _ in range(bits))
        # Ensure it doesn't start with 0 unless it's just 0
        if binary.startswith('0') and len(binary) > 1:
            binary = '1' + binary[1:]
        return f"Convert {binary}₂ to decimal", binary_to_decimal(binary)
    
    elif problem_type == "decimal_to_binary":
        decimal = random.randint(1, 255)
        return f"Convert {decimal}₁₀ to binary", decimal_to_binary(decimal)
    
    elif problem_type == "octal_to_decimal":
        # Generate random octal number
        digits = random.randint(2, 4)
        octal = ''.join(str(random.randint(0, 7)) for _ in range(digits))
        return f"Convert {octal}₈ to decimal", octal_to_decimal(octal)
    
    elif problem_type == "decimal_to_octal":
        decimal = random.randint(8, 511)
        return f"Convert {decimal}₁₀ to octal", decimal_to_octal(decimal)
    
    elif problem_type == "hex_to_decimal":
        # Generate random hex number
        digits = random.randint(2, 3)
        hex_chars = "0123456789ABCDEF"
        hex_num = ''.join(random.choice(hex_chars) for _ in range(digits))
        return f"Convert {hex_num}₁₆ to decimal", hexadecimal_to_decimal(hex_num)
    
    elif problem_type == "decimal_to_hex":
        decimal = random.randint(16, 4095)
        return f"Convert {decimal}₁₀ to hexadecimal", decimal_to_hexadecimal(decimal)
    
    elif problem_type == "binary_to_octal":
        bits = random.randint(6, 9)
        binary = ''.join(random.choice(['0', '1']) for _ in range(bits))
        if binary.startswith('0') and len(binary) > 1:
            binary = '1' + binary[1:]
        return f"Convert {binary}₂ to octal", binary_to_octal(binary)
    
    elif problem_type == "binary_to_hex":
        bits = random.randint(8, 12)
        binary = ''.join(random.choice(['0', '1']) for _ in range(bits))
        if binary.startswith('0') and len(binary) > 1:
            binary = '1' + binary[1:]
        return f"Convert {binary}₂ to hexadecimal", binary_to_hexadecimal(binary)

def main():
    """Main interactive practice session."""
    print("🔢 Number Systems Practice Script")
    print("=" * 40)
    print("This script generates random practice problems for number system conversions.")
    print("Type 'quit' to exit, 'help' for conversion methods.\n")
    
    correct = 0
    total = 0
    
    while True:
        problem, answer = generate_problem()
        print(f"\nProblem {total + 1}: {problem}")
        
        try:
            user_answer = input("Your answer: ").strip().upper()
            
            if user_answer.lower() == 'quit':
                break
            elif user_answer.lower() == 'help':
                print("\nConversion Methods:")
                print("- Binary to Decimal: Sum of (digit × 2^position)")
                print("- Decimal to Binary: Repeated division by 2")
                print("- Octal to Decimal: Sum of (digit × 8^position)")
                print("- Decimal to Octal: Repeated division by 8")
                print("- Hex to Decimal: Sum of (digit × 16^position)")
                print("- Decimal to Hex: Repeated division by 16")
                print("- Binary to Octal: Group in threes, convert each")
                print("- Binary to Hex: Group in fours, convert each")
                continue
            
            # Check if answer is correct
            if str(user_answer) == str(answer):
                print("✅ Correct!")
                correct += 1
            else:
                print(f"❌ Incorrect. The answer is: {answer}")
            
            total += 1
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue
    
    if total > 0:
        percentage = (correct / total) * 100
        print(f"\n📊 Final Score: {correct}/{total} ({percentage:.1f}%)")
        
        if percentage >= 90:
            print("🎉 Excellent! You're a number systems master!")
        elif percentage >= 75:
            print("👍 Good work! Keep practicing to improve.")
        elif percentage >= 50:
            print("📚 Not bad! Review the conversion methods and practice more.")
        else:
            print("📖 Keep studying! Focus on the basic conversion methods.")

if __name__ == "__main__":
    main() 