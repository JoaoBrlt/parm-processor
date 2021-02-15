// Two positive values.
// 126 + 150 = 276
// Flags = 0000
MOVS r0, #126
MOVS r1, #150
CMN r1, r0

// Two opposite sign values.
// -170 + 61 = -46
// Flags = 1000
MOVS r2, #169
MVNS r2, r2
MOVS r3, #61
CMN r3, r2

// Two negative values.
// -45 + (-198) = -243
// Flags = 1010
MOVS r4, #44
MVNS r4, r4
MOVS r5, #197
MVNS r5, r5
CMN r5, r4

// Two opposite values.
// 88 + (-88) = 0
// Flags = 0110
MOVS r6, #88
MOVS r7, #87
MVNS r7, r7
CMN r7, r6

// Same register.
// 255 + 255 = 510
// Flags = 0000
MOVS r0, #255
CMN r0, r0
