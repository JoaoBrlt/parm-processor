// Add two positive values.
// 4 + 3 = 7
MOVS r0, #4
MOVS r1, #3
ADDS r2, r1, r0

// Add two positive values.
// 102 + 150 = 252
MOVS r3, #102
MOVS r4, #150
ADDS r5, r4, r3

// Add two opposite sign values.
// -1 + 255 = 254
MOVS r6, #0
MVNS r6, r6
MOVS r7, #255
ADDS r0, r7, r6

// Add two negative values.
// -256 + (-1) = -257
MOVS r1, #255
MVNS r1, r1
MOVS r2, #0
MVNS r2, r2
ADDS r3, r2, r1

// Add the same register.
// 150 + 150 = 300
MOVS r4, #150
ADDS r5, r4, r4

// Add the same register to itself.
// 124 + 124 = 248
MOVS r6, #124
ADDS r6, r6, r6
