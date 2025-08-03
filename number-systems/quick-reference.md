# Number Systems Quick Reference

## Conversion Methods

### Binary ↔ Decimal
- **To Decimal**: Sum of (digit × 2^position)
- **To Binary**: Repeated division by 2, read remainders in reverse

### Octal ↔ Decimal
- **To Decimal**: Sum of (digit × 8^position)
- **To Octal**: Repeated division by 8, read remainders in reverse

### Hexadecimal ↔ Decimal
- **To Decimal**: Sum of (digit × 16^position)
- **To Hexadecimal**: Repeated division by 16, read remainders in reverse

### Binary ↔ Octal
- **To Octal**: Group binary digits in threes, convert each group
- **To Binary**: Convert each octal digit to 3 binary digits

### Binary ↔ Hexadecimal
- **To Hexadecimal**: Group binary digits in fours, convert each group
- **To Binary**: Convert each hex digit to 4 binary digits

## Powers to Memorize

### Powers of 2
| Power | Value |
|-------|-------|
| 2⁰    | 1     |
| 2¹    | 2     |
| 2²    | 4     |
| 2³    | 8     |
| 2⁴    | 16    |
| 2⁵    | 32    |
| 2⁶    | 64    |
| 2⁷    | 128   |
| 2⁸    | 256   |
| 2⁹    | 512   |
| 2¹⁰   | 1024  |

### Powers of 8
| Power | Value |
|-------|-------|
| 8⁰    | 1     |
| 8¹    | 8     |
| 8²    | 64    |
| 8³    | 512   |
| 8⁴    | 4096  |

### Powers of 16
| Power | Value  |
|-------|--------|
| 16⁰   | 1      |
| 16¹   | 16     |
| 16²   | 256    |
| 16³   | 4096   |
| 16⁴   | 65536  |

## Common Values

### Binary Patterns
- 11111111₂ = 255₁₀ (8 bits, all 1s)
- 10000000₂ = 128₁₀ (8 bits, only leftmost 1)
- 00000001₂ = 1₁₀ (8 bits, only rightmost 1)

### Hexadecimal Colors
- #000000 = Black
- #FFFFFF = White
- #FF0000 = Red
- #00FF00 = Green
- #0000FF = Blue
- #FFFF00 = Yellow
- #FF00FF = Magenta
- #00FFFF = Cyan

### Common Octal Values
- 777₈ = 511₁₀ (Unix permissions: rwxrwxrwx)
- 755₈ = 493₁₀ (Unix permissions: rwxr-xr-x)
- 644₈ = 420₁₀ (Unix permissions: rw-r--r--)

## Conversion Table (0-15)

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

## Binary Arithmetic Rules

### Addition
- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 10 (carry 1)

### Subtraction
- 0 - 0 = 0
- 1 - 0 = 1
- 1 - 1 = 0
- 0 - 1 = 1 (borrow 1)

## Two's Complement (Negative Numbers)

### 8-bit Two's Complement
- Positive numbers: 00000000₂ to 01111111₂ (0 to 127)
- Negative numbers: 10000000₂ to 11111111₂ (-128 to -1)
- To find negative: invert bits + 1

### Examples
- -1₁₀ = 11111111₂
- -42₁₀ = 11010110₂
- -128₁₀ = 10000000₂

## Floating Point Conversion

### Binary Fractions
- 0.1₂ = 0.5₁₀
- 0.01₂ = 0.25₁₀
- 0.001₂ = 0.125₁₀
- 0.0001₂ = 0.0625₁₀

### Hexadecimal Fractions
- 0.8₁₆ = 0.5₁₀
- 0.4₁₆ = 0.25₁₀
- 0.2₁₆ = 0.125₁₀
- 0.1₁₆ = 0.0625₁₀

## Common Mistakes to Avoid

1. **Reading remainders in wrong order** when converting decimal to other bases
2. **Forgetting to group binary digits correctly** for octal/hex conversion
3. **Confusing A-F values** in hexadecimal (A=10, not 1)
4. **Not handling negative numbers** in binary arithmetic
5. **Forgetting leading zeros** in binary representations

## Quick Tips

1. **Binary doubling**: Each position doubles the previous value
2. **Hex colors**: #RRGGBB format (Red, Green, Blue)
3. **Octal permissions**: rwx format (read, write, execute)
4. **Memory addresses**: Usually in hexadecimal
5. **Network addresses**: IPv4 in decimal, IPv6 in hexadecimal

## Programming Examples

### Python
```python
# Convert between bases
bin(42)      # '0b101010'
oct(42)      # '0o52'
hex(42)      # '0x2a'
int('101010', 2)   # 42
int('52', 8)       # 42
int('2a', 16)      # 42
```

### JavaScript
```javascript
// Convert between bases
(42).toString(2)   // '101010'
(42).toString(8)   // '52'
(42).toString(16)  // '2a'
parseInt('101010', 2)  // 42
parseInt('52', 8)      // 42
parseInt('2a', 16)     // 42
```

### C/C++
```c
// Convert between bases
printf("%b", 42);  // binary (not standard)
printf("%o", 42);  // octal
printf("%x", 42);  // hexadecimal
printf("%X", 42);  // uppercase hexadecimal
```

---

*Keep this reference handy for quick conversions and common values!* 