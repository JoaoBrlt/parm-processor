// Positive shift by a bit.
// ...10000000 >> 00001 = ...01000000
MOVS r0, #1
MOVS r1, #128
ASRS r1, r0

// Negative shift by a bit.
// 11111111 11111111 11111111 00000000 >> 00001 =
// 11111111 11111111 11111111 10000000
MOVS r2, #1
MOVS r3, #255
MVNS r3, r3
ASRS r3, r2

// Positive shift by seven bits.
// ...10000000 >> 00111 = ...00000001
MOVS r4, #7
MOVS r5, #128
ASRS r5, r4

// Negative shift by seven bits.
// 11111111 11111111 11111111 01010101 >> 00111 =
// 11111111 11111111 11111111 11111110
MOVS r6, #7
MOVS r7, #170
MVNS r7, r7
ASRS r7, r6

// Positive shift by a byte.
// ...11001100 >> 01000 = ...00000000
MOVS r0, #8
MOVS r1, #204
ASRS r1, r0

// Negative shift by a byte.
// 11111111 11111111 11111111 00110011 >> 01000 =
// 11111111 11111111 11111111 11111111
MOVS r2, #8
MOVS r3, #204
MVNS r3, r3
ASRS r3, r2

// Positive shift by three bytes.
// ...11000011 >> 11000 = ...00000000
MOVS r4, #24
MOVS r5, #195
ASRS r5, r4

// Negative shift by three bytes.
// 11111111 11111111 11111111 00111100 >> 11000 =
// 11111111 11111111 11111111 11111111
MOVS r6, #24
MOVS r7, #195
MVNS r7, r7
ASRS r7, r6

// Positive shift by maximum.
// 11111111 >> 11111 = ...00000000
MOVS r0, #31
MOVS r1, #255
ASRS r1, r0

// Negative shift by maximum.
// 11111111 11111111 11111111 00000000 >> 11111 =
// 11111111 11111111 11111111 11111111
MOVS r2, #31
MOVS r3, #255
MVNS r3, r3
ASRS r3, r2

// Positive shift by over maximum.
// 11111111 >> 00000 = ...11111111
MOVS r4, #32
MOVS r5, #255
ASRS r5, r4

// Negative shift by over maximum.
// 11111111 11111111 11111111 00000000 >> 00000 =
// 11111111 11111111 11111111 00000000
MOVS r6, #32
MOVS r7, #255
MVNS r7, r7
ASRS r7, r6
