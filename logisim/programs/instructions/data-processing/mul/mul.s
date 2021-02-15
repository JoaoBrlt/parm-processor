// Multiply two positive values.
// 4 * 3 = 12
MOVS r0, #4
MOVS r1, #3
MULS r1, r0, r1

// Multiply two positive values.
// 102 * 150 = 15300
MOVS r2, #102
MOVS r3, #150
MULS r3, r2, r3

// Multiply two opposite sign values.
// -2 * 255 = -510
MOVS r4, #1
MVNS r4, r4
MOVS r5, #255
MULS r5, r4, r5

// Multiply two negative values.
// -255 * (-2) = 510
MOVS r6, #254
MVNS r6, r6
MOVS r7, #1
MVNS r7, r7
MULS r7, r6, r7

// Multiply the same register.
// 150 * 150 = 22500
MOVS r0, #150
MULS r0, r0, r0
