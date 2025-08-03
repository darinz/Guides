# Number Systems Practice Problems

## Problem Set 1: Basic Binary Conversions

### Problem 1.1
**Convert 10101₂ to decimal**

**Solution:**
```
10101₂ = 1×2⁴ + 0×2³ + 1×2² + 0×2¹ + 1×2⁰
        = 1×16 + 0×8 + 1×4 + 0×2 + 1×1
        = 16 + 0 + 4 + 0 + 1
        = 21₁₀
```

### Problem 1.2
**Convert 110011₂ to decimal**

**Solution:**
```
110011₂ = 1×2⁵ + 1×2⁴ + 0×2³ + 0×2² + 1×2¹ + 1×2⁰
         = 1×32 + 1×16 + 0×8 + 0×4 + 1×2 + 1×1
         = 32 + 16 + 0 + 0 + 2 + 1
         = 51₁₀
```

### Problem 1.3
**Convert 45₁₀ to binary**

**Solution:**
```
45 ÷ 2 = 22 remainder 1
22 ÷ 2 = 11 remainder 0
11 ÷ 2 = 5  remainder 1
5  ÷ 2 = 2  remainder 1
2  ÷ 2 = 1  remainder 0
1  ÷ 2 = 0  remainder 1

Reading remainders from bottom to top: 101101₂
```

### Problem 1.4
**Convert 127₁₀ to binary**

**Solution:**
```
127 ÷ 2 = 63 remainder 1
63  ÷ 2 = 31 remainder 1
31  ÷ 2 = 15 remainder 1
15  ÷ 2 = 7  remainder 1
7   ÷ 2 = 3  remainder 1
3   ÷ 2 = 1  remainder 1
1   ÷ 2 = 0  remainder 1

Reading remainders from bottom to top: 1111111₂
```

## Problem Set 2: Octal Conversions

### Problem 2.1
**Convert 347₈ to decimal**

**Solution:**
```
347₈ = 3×8² + 4×8¹ + 7×8⁰
      = 3×64 + 4×8 + 7×1
      = 192 + 32 + 7
      = 231₁₀
```

### Problem 2.2
**Convert 125₈ to decimal**

**Solution:**
```
125₈ = 1×8² + 2×8¹ + 5×8⁰
      = 1×64 + 2×8 + 5×1
      = 64 + 16 + 5
      = 85₁₀
```

### Problem 2.3
**Convert 231₁₀ to octal**

**Solution:**
```
231 ÷ 8 = 28 remainder 7
28  ÷ 8 = 3  remainder 4
3   ÷ 8 = 0  remainder 3

Reading remainders from bottom to top: 347₈
```

### Problem 2.4
**Convert 89₁₀ to octal**

**Solution:**
```
89 ÷ 8 = 11 remainder 1
11 ÷ 8 = 1  remainder 3
1  ÷ 8 = 0  remainder 1

Reading remainders from bottom to top: 131₈
```

## Problem Set 3: Hexadecimal Conversions

### Problem 3.1
**Convert 2A7₁₆ to decimal**

**Solution:**
```
2A7₁₆ = 2×16² + A×16¹ + 7×16⁰
       = 2×256 + 10×16 + 7×1
       = 512 + 160 + 7
       = 679₁₀
```

### Problem 3.2
**Convert F4₁₆ to decimal**

**Solution:**
```
F4₁₆ = F×16¹ + 4×16⁰
      = 15×16 + 4×1
      = 240 + 4
      = 244₁₀
```

### Problem 3.3
**Convert 679₁₀ to hexadecimal**

**Solution:**
```
679 ÷ 16 = 42 remainder 7
42  ÷ 16 = 2  remainder 10 (A)
2   ÷ 16 = 0  remainder 2

Reading remainders from bottom to top: 2A7₁₆
```

### Problem 3.4
**Convert 255₁₀ to hexadecimal**

**Solution:**
```
255 ÷ 16 = 15 remainder 15 (F)
15  ÷ 16 = 0  remainder 15 (F)

Reading remainders from bottom to top: FF₁₆
```

## Problem Set 4: Cross-System Conversions

### Problem 4.1
**Convert 11010110₂ to octal**

**Solution:**
```
Group binary digits in groups of 3 from right:
11 010 110₂

Convert each group:
11₂ = 3₈
010₂ = 2₈
110₂ = 6₈

Result: 326₈
```

### Problem 4.2
**Convert 11010110₂ to hexadecimal**

**Solution:**
```
Group binary digits in groups of 4 from right:
1101 0110₂

Convert each group:
1101₂ = 13₁₀ = D₁₆
0110₂ = 6₁₀ = 6₁₆

Result: D6₁₆
```

### Problem 4.3
**Convert 347₈ to binary**

**Solution:**
```
Convert each octal digit to 3 binary digits:
3₈ = 011₂
4₈ = 100₂
7₈ = 111₂

Result: 11100111₂
```

### Problem 4.4
**Convert 2A7₁₆ to binary**

**Solution:**
```
Convert each hex digit to 4 binary digits:
2₁₆ = 0010₂
A₁₆ = 1010₂
7₁₆ = 0111₂

Result: 1010100111₂
```

## Problem Set 5: Binary Arithmetic

### Problem 5.1
**Add: 1011₂ + 1101₂**

**Solution:**
```
  1 1 1 1  (carry)
    1 0 1 1
  + 1 1 0 1
  --------
  1 1 0 0 0

Result: 11000₂
```

### Problem 5.2
**Subtract: 1101₂ - 1011₂**

**Solution:**
```
  1 1 0 1
- 1 0 1 1
--------
  0 0 1 0

Result: 10₂
```

### Problem 5.3
**Add: 1111₂ + 1₂**

**Solution:**
```
  1 1 1 1  (carry)
    1 1 1 1
  + 0 0 0 1
  --------
  1 0 0 0 0

Result: 10000₂
```

### Problem 5.4
**Subtract: 1000₂ - 1₂**

**Solution:**
```
  1 0 0 0
- 0 0 0 1
--------
  0 1 1 1

Result: 111₂
```

## Problem Set 6: Advanced Problems

### Problem 6.1
**Convert 0.101₂ to decimal**

**Solution:**
```
0.101₂ = 1×2⁻¹ + 0×2⁻² + 1×2⁻³
        = 1×0.5 + 0×0.25 + 1×0.125
        = 0.5 + 0 + 0.125
        = 0.625₁₀
```

### Problem 6.2
**Convert 0.347₈ to decimal**

**Solution:**
```
0.347₈ = 3×8⁻¹ + 4×8⁻² + 7×8⁻³
        = 3×0.125 + 4×0.015625 + 7×0.001953125
        = 0.375 + 0.0625 + 0.013671875
        = 0.451171875₁₀
```

### Problem 6.3
**Convert 0.2A7₁₆ to decimal**

**Solution:**
```
0.2A7₁₆ = 2×16⁻¹ + A×16⁻² + 7×16⁻³
         = 2×0.0625 + 10×0.00390625 + 7×0.000244140625
         = 0.125 + 0.0390625 + 0.001708984375
         = 0.166015625₁₀
```

### Problem 6.4
**Convert -42₁₀ to 8-bit two's complement binary**

**Solution:**
```
Step 1: Convert 42₁₀ to 8-bit binary
42₁₀ = 00101010₂

Step 2: Invert all bits
00101010₂ → 11010101₂

Step 3: Add 1
11010101₂ + 1₂ = 11010110₂

Result: 11010110₂
```

## Problem Set 7: Mixed Operations

### Problem 7.1
**Convert (1011₂ + 1101₂) to decimal**

**Solution:**
```
Step 1: Add binary numbers
1011₂ + 1101₂ = 11000₂

Step 2: Convert to decimal
11000₂ = 1×2⁴ + 1×2³ + 0×2² + 0×2¹ + 0×2⁰
        = 16 + 8 + 0 + 0 + 0
        = 24₁₀

Result: 24₁₀
```

### Problem 7.2
**Convert (347₈ + 125₈) to decimal**

**Solution:**
```
Step 1: Add octal numbers
347₈ + 125₈ = 474₈

Step 2: Convert to decimal
474₈ = 4×8² + 7×8¹ + 4×8⁰
      = 4×64 + 7×8 + 4×1
      = 256 + 56 + 4
      = 316₁₀

Result: 316₁₀
```

### Problem 7.3
**Convert (2A7₁₆ + F4₁₆) to decimal**

**Solution:**
```
Step 1: Add hexadecimal numbers
2A7₁₆ + F4₁₆ = 39B₁₆

Step 2: Convert to decimal
39B₁₆ = 3×16² + 9×16¹ + B×16⁰
       = 3×256 + 9×16 + 11×1
       = 768 + 144 + 11
       = 923₁₀

Result: 923₁₀
```

## Problem Set 8: Challenge Problems

### Problem 8.1
**Find the binary representation of π (first 8 bits)**

**Solution:**
```
π ≈ 3.14159265359...

Convert 3₁₀ to binary:
3₁₀ = 11₂

Convert 0.14159265359... to binary:
0.14159265359... × 2 = 0.28318530718... → 0
0.28318530718... × 2 = 0.56637061436... → 0
0.56637061436... × 2 = 1.13274122872... → 1
0.13274122872... × 2 = 0.26548245744... → 0
0.26548245744... × 2 = 0.53096491488... → 0
0.53096491488... × 2 = 1.06192982976... → 1
0.06192982976... × 2 = 0.12385965952... → 0
0.12385965952... × 2 = 0.24771931904... → 0

Result: 11.00100100₂ (first 8 bits)
```

### Problem 8.2
**Convert 0.1₁₀ to binary (first 8 bits after decimal point)**

**Solution:**
```
0.1 × 2 = 0.2 → 0
0.2 × 2 = 0.4 → 0
0.4 × 2 = 0.8 → 0
0.8 × 2 = 1.6 → 1
0.6 × 2 = 1.2 → 1
0.2 × 2 = 0.4 → 0
0.4 × 2 = 0.8 → 0
0.8 × 2 = 1.6 → 1

Result: 0.00011001₂ (first 8 bits)
```

### Problem 8.3
**Convert 0.5₁₀ to hexadecimal**

**Solution:**
```
0.5 × 16 = 8.0 → 8

Result: 0.8₁₆
```

## Additional Practice Problems

### Binary to Decimal
1. 111001₂ = ?
2. 1010101₂ = ?
3. 1000000₂ = ?

### Decimal to Binary
4. 73₁₀ = ?
5. 128₁₀ = ?
6. 255₁₀ = ?

### Octal Conversions
7. 777₈ = ?
8. 1000₈ = ?
9. 1234₁₀ = ?₈

### Hexadecimal Conversions
10. ABC₁₆ = ?
11. FFFF₁₆ = ?
12. 1000₁₀ = ?₁₆

### Cross-System
13. 10101010₂ = ?₈ = ?₁₆
14. 777₈ = ?₂ = ?₁₆
15. F0F0₁₆ = ?₂ = ?₈

---

*Practice these problems regularly to improve your number system conversion skills!* 