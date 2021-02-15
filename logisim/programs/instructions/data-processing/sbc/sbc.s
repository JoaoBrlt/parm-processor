// Subtract two positive values.
// 247 - 145 + 0 - 1 = 101
// Flags = 0000
MOVS r0, #145
MOVS r1, #247
SBCS r1, r0

// Subtract two positive values.
// 160 - 255 + 0 - 1 = -96
// Flags = 1010
MOVS r2, #255
MOVS r3, #160
SBCS r3, r2

// Subtract two positive values (with carry in).
// 127 - 85 + 1 - 1 = 42
// Flags = 0000
MOVS r4, #85
MOVS r5, #127
SBCS r5, r4

// Subtract a negative value from a positive value.
// 150 - (-16) + 0 - 1 = 165
// Flags = 0010
MOVS r6, #15
MVNS r6, r6
MOVS r7, #150
SBCS r7, r6

// Subtract two negative values.
// -65 - (-89) + 0 - 1 = 23
// Flags = 0000
MOVS r0, #88
MVNS r0, r0
MOVS r1, #64
MVNS r1, r1
SBCS r1, r0

// Subtract the same register.
// 203 - 203 + 0 - 1 = -1
// Flags = 1010
MOVS r2, #203
SBCS r2, r2
