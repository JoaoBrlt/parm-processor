// Two positive values.
// 170 - 1 = 169
// Flags = 0000
MOVS r0, #170
MOVS r1, #1
CMP r1, r0

// Two positive values.
// 64 - 189 = -125
// Flags = 1010
MOVS r2, #64
MOVS r3, #189
CMP r3, r2

// Two opposite sign values.
// -74 - 250 = -324
// Flags = 1000
MOVS r4, #73
MVNS r4, r4
MOVS r5, #250
CMP r5, r4

// Two negative values.
// -25 - (-210) = 185
// Flags = 0000
MOVS r6, #24
MVNS r6, r6
MOVS r7, #209
MVNS r7, r7
CMP r7, r6

// Same register.
// 10 - 10 = 0
// Flags = 0100
MOVS r0, #10
CMP r0, r0
