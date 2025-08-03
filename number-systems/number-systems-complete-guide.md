# Complete Guide to Number Systems: Binary, Octal, and Hexadecimal

## Table of Contents
1. [Introduction to Number Systems](#introduction-to-number-systems)
2. [Binary Numbers](#binary-numbers)
3. [Octal Numbers](#octal-numbers)
4. [Hexadecimal Numbers](#hexadecimal-numbers)
5. [Conversion Methods](#conversion-methods)
6. [Practice Problems](#practice-problems)
7. [Solutions](#solutions)
8. [Real-World Applications](#real-world-applications)

## Introduction to Number Systems

A number system is a way to represent numbers using a set of symbols and rules. The most familiar system is the decimal (base-10) system, but computers and programming often use other bases.

### Key Concepts
- **Base**: The number of unique digits used in a number system
- **Positional Notation**: Each position represents a power of the base
- **Radix**: Another term for the base of a number system

## Binary Numbers

Binary is a base-2 number system using only two digits: 0 and 1.

### Binary to Decimal Conversion
Each position represents a power of 2, starting from the right (2⁰).

**Example**: Convert 1101₂ to decimal
```
1101₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰
       = 1×8 + 1×4 + 0×2 + 1×1
       = 8 + 4 + 0 + 1
       = 13₁₀
```

### Decimal to Binary Conversion
Use repeated division by 2 and read remainders in reverse order.

**Example**: Convert 25₁₀ to binary
```
25 ÷ 2 = 12 remainder 1
12 ÷ 2 = 6  remainder 0
6  ÷ 2 = 3  remainder 0
3  ÷ 2 = 1  remainder 1
1  ÷ 2 = 0  remainder 1

Reading remainders from bottom to top: 11001₂
```

### Binary Arithmetic

#### Addition
```
  1 1 1 1  (carry)
    1 0 1 1
  + 0 1 1 0
  --------
  1 0 0 0 1
```

#### Subtraction
```
  1 0 1 1
- 0 1 1 0
--------
  0 1 0 1
```

## Octal Numbers

Octal is a base-8 number system using digits 0-7.

### Octal to Decimal Conversion
Each position represents a power of 8.

**Example**: Convert 347₈ to decimal
```
347₈ = 3×8² + 4×8¹ + 7×8⁰
      = 3×64 + 4×8 + 7×1
      = 192 + 32 + 7
      = 231₁₀
```

### Decimal to Octal Conversion
Use repeated division by 8.

**Example**: Convert 231₁₀ to octal
```
231 ÷ 8 = 28 remainder 7
28  ÷ 8 = 3  remainder 4
3   ÷ 8 = 0  remainder 3

Reading remainders from bottom to top: 347₈
```

### Binary to Octal Conversion
Group binary digits in groups of 3 (from right) and convert each group.

**Example**: Convert 110101₂ to octal
```
110 101₂
6   5₈
Result: 65₈
```

## Hexadecimal Numbers

Hexadecimal is a base-16 number system using digits 0-9 and letters A-F.

### Hexadecimal Digits
- A = 10, B = 11, C = 12, D = 13, E = 14, F = 15

### Hexadecimal to Decimal Conversion
Each position represents a power of 16.

**Example**: Convert 2A7₁₆ to decimal
```
2A7₁₆ = 2×16² + A×16¹ + 7×16⁰
       = 2×256 + 10×16 + 7×1
       = 512 + 160 + 7
       = 679₁₀
```

### Decimal to Hexadecimal Conversion
Use repeated division by 16.

**Example**: Convert 679₁₀ to hexadecimal
```
679 ÷ 16 = 42 remainder 7
42  ÷ 16 = 2  remainder 10 (A)
2   ÷ 16 = 0  remainder 2

Reading remainders from bottom to top: 2A7₁₆
```

### Binary to Hexadecimal Conversion
Group binary digits in groups of 4 (from right) and convert each group.

**Example**: Convert 11010110₂ to hexadecimal
```
1101 0110₂
D    6₁₆
Result: D6₁₆
```

## Conversion Methods

### Quick Conversion Table

| Decimal | Binary | Octal | Hexadecimal |
|---------|--------|-------|-------------|
| 0       | 0      | 0     | 0           |
| 1       | 1      | 1     | 1           |
| 2       | 10     | 2     | 2           |
| 3       | 11     | 3     | 3           |
| 4       | 100    | 4     | 4           |
| 5       | 101    | 5     | 5           |
| 6       | 110    | 6     | 6           |
| 7       | 111    | 7     | 7           |
| 8       | 1000   | 10    | 8           |
| 9       | 1001   | 11    | 9           |
| 10      | 1010   | 12    | A           |
| 11      | 1011   | 13    | B           |
| 12      | 1100   | 14    | C           |
| 13      | 1101   | 15    | D           |
| 14      | 1110   | 16    | E           |
| 15      | 1111   | 17    | F           |

### Conversion Formulas

#### Binary ↔ Decimal
- **To Decimal**: Sum of (digit × 2^position)
- **To Binary**: Repeated division by 2

#### Octal ↔ Decimal
- **To Decimal**: Sum of (digit × 8^position)
- **To Octal**: Repeated division by 8

#### Hexadecimal ↔ Decimal
- **To Decimal**: Sum of (digit × 16^position)
- **To Hexadecimal**: Repeated division by 16

#### Binary ↔ Octal
- **To Octal**: Group binary digits in threes, convert each group
- **To Binary**: Convert each octal digit to 3 binary digits

#### Binary ↔ Hexadecimal
- **To Hexadecimal**: Group binary digits in fours, convert each group
- **To Binary**: Convert each hex digit to 4 binary digits

## Practice Problems

### Level 1: Basic Conversions

#### Binary Conversions
1. Convert 10101₂ to decimal
2. Convert 110011₂ to decimal
3. Convert 45₁₀ to binary
4. Convert 127₁₀ to binary

#### Octal Conversions
5. Convert 347₈ to decimal
6. Convert 125₈ to decimal
7. Convert 231₁₀ to octal
8. Convert 89₁₀ to octal

#### Hexadecimal Conversions
9. Convert 2A7₁₆ to decimal
10. Convert F4₁₆ to decimal
11. Convert 679₁₀ to hexadecimal
12. Convert 255₁₀ to hexadecimal

### Level 2: Cross-System Conversions

13. Convert 11010110₂ to octal
14. Convert 11010110₂ to hexadecimal
15. Convert 347₈ to binary
16. Convert 2A7₁₆ to binary
17. Convert 65₈ to hexadecimal
18. Convert D6₁₆ to octal

### Level 3: Arithmetic

#### Binary Arithmetic
19. Add: 1011₂ + 1101₂
20. Subtract: 1101₂ - 1011₂
21. Add: 1111₂ + 1₂
22. Subtract: 1000₂ - 1₂

#### Mixed Operations
23. Convert (1011₂ + 1101₂) to decimal
24. Convert (347₈ + 125₈) to decimal
25. Convert (2A7₁₆ + F4₁₆) to decimal

### Level 4: Advanced Problems

26. Convert 0.101₂ to decimal
27. Convert 0.347₈ to decimal
28. Convert 0.2A7₁₆ to decimal
29. Find the binary representation of π (first 8 bits)
30. Convert -42₁₀ to 8-bit two's complement binary

## Solutions

### Level 1 Solutions

1. 10101₂ = 21₁₀
2. 110011₂ = 51₁₀
3. 45₁₀ = 101101₂
4. 127₁₀ = 1111111₂
5. 347₈ = 231₁₀
6. 125₈ = 85₁₀
7. 231₁₀ = 347₈
8. 89₁₀ = 131₈
9. 2A7₁₆ = 679₁₀
10. F4₁₆ = 244₁₀
11. 679₁₀ = 2A7₁₆
12. 255₁₀ = FF₁₆

### Level 2 Solutions

13. 11010110₂ = 326₈
14. 11010110₂ = D6₁₆
15. 347₈ = 11100111₂
16. 2A7₁₆ = 1010100111₂
17. 65₈ = 35₁₆
18. D6₁₆ = 326₈

### Level 3 Solutions

19. 1011₂ + 1101₂ = 11000₂
20. 1101₂ - 1011₂ = 10₂
21. 1111₂ + 1₂ = 10000₂
22. 1000₂ - 1₂ = 111₂
23. (1011₂ + 1101₂) = 11000₂ = 24₁₀
24. (347₈ + 125₈) = 474₈ = 316₁₀
25. (2A7₁₆ + F4₁₆) = 39B₁₆ = 923₁₀

### Level 4 Solutions

26. 0.101₂ = 0.625₁₀
27. 0.347₈ = 0.451171875₁₀
28. 0.2A7₁₆ = 0.166015625₁₀
29. π ≈ 11.00100100₂ (first 8 bits)
30. -42₁₀ = 11010110₂ (8-bit two's complement)

## Real-World Applications

### Computer Science
- **Binary**: CPU operations, memory addressing
- **Hexadecimal**: Memory addresses, color codes, MAC addresses
- **Octal**: Unix file permissions, some programming languages

### Programming
- **Binary**: Bit manipulation, flags, masks
- **Hexadecimal**: Color codes (#FF0000), memory dumps
- **Octal**: File permissions (chmod 755)

### Electronics
- **Binary**: Digital circuits, logic gates
- **Hexadecimal**: Microcontroller programming, debugging

### Networking
- **Hexadecimal**: MAC addresses, IPv6 addresses
- **Binary**: Subnet masks, network protocols

## Tips and Tricks

1. **Powers of 2**: Memorize 2⁰=1, 2¹=2, 2²=4, 2³=8, 2⁴=16, 2⁵=32, 2⁶=64, 2⁷=128, 2⁸=256
2. **Powers of 8**: 8⁰=1, 8¹=8, 8²=64, 8³=512
3. **Powers of 16**: 16⁰=1, 16¹=16, 16²=256, 16³=4096
4. **Quick Binary**: Each position doubles the previous value
5. **Hex Colors**: #RRGGBB format (Red, Green, Blue, each 2 hex digits)

## Common Mistakes to Avoid

1. **Forgetting to read remainders in reverse order** when converting decimal to other bases
2. **Not grouping binary digits correctly** when converting to octal/hex
3. **Confusing A-F values** in hexadecimal (A=10, not 1)
4. **Forgetting to handle negative numbers** in binary arithmetic
5. **Not accounting for leading zeros** in binary representations

## Additional Resources

- Practice with online converters
- Use programming languages to verify conversions
- Study bitwise operations in programming
- Explore floating-point number representations
- Learn about signed vs unsigned numbers

---

*This guide covers the fundamental concepts of number systems. Practice regularly with these problems to build confidence and speed in conversions.* 