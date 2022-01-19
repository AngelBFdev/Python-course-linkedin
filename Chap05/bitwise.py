#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Value of 10 in hexadecimal
x = 0x0a
y = 0x02

# Just the binary operator match
# 1010 and 0010 just match 0010
z = x & y

# first character is to fill with 0
# second is the number of 0
# third is the numeric system
# (x hexadecimal, b is binary)
print('And')
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

# Add all the binary in both variables
# 1010 and 1010 so 1010
# if 1010 and 0101 it would be 1111
y = 0x05
z = x | y
print('OR')
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

# The ones that don't match
# 1010 and 1111 so 0101
# 1010 and 0101 so 1111
y = 0x0f
z = x ^ y
print('XOR')
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

# The shift left
y = 0x01
z = x << y
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')

# The shift right
z = x >> y
print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
