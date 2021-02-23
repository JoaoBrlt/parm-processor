// Add one to a positive value.
// 8 + 0 = 5
MOVS r0, #8
ADDS r1, r0, #0

// Add one to a positive value.
// 5 + 1 = 6
MOVS r2, #5
ADDS r3, r2, #1

// Add two to a positive value.
// 255 + 2 = 257
MOVS r4, #255
ADDS r5, r4, #2

// Add three to a negative value.
// -125 + 3 = -122
MOVS r6, #124
MVNS r6, r6
ADDS r7, r6, #3

// Add maximum.
// 68 + 7 = 75
MOVS r0, #68
ADDS r1, r0, #7

// Add to same register.
// 128 + 5 = 133
MOVS r2, #128
ADDS r3, r2, #5
