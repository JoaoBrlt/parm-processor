// Subtract two positive values.
// 7 - 5 = 2
MOVS r0, #5
MOVS r1, #7
SUBS r2, r1, r0

// Subtract two positive values.
// 160 - 255 = -95
MOVS r3, #255
MOVS r4, #160
SUBS r5, r4, r3

// Subtract a positive value from a negative value.
// -256 - 120 = -376
MOVS r6, #120
MOVS r7, #255
MVNS r7, r7
SUBS r0, r7, r6

// Subtract a negative value from a positive value.
// 150 - (-16) = 166
MOVS r1, #15
MVNS r1, r1
MOVS r2, #150
SUBS r3, r2, r1

// Subtract two negative values.
// -65 - (-89) = 24
MOVS r4, #88
MVNS r4, r4
MOVS r5, #64
MVNS r5, r5
SUBS r6, r5, r4

// Subtract the same register.
// 203 - 203 = 0
MOVS r7, #203
SUBS r0, r7, r7

// Subtract the same register to itself.
// 77 - 77 = 0
MOVS r1, #77
SUBS r1, r1, r1
