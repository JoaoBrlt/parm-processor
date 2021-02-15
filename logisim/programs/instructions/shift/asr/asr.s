// Positive shift by a bit.
// ...10000000 >> 00001 = ...01000000
MOVS r0, #128
ASRS r1, r0, #1

// Negative shift by a bit.
// 11111111 11111111 11111111 00000000 >> 00001 =
// 11111111 11111111 11111111 10000000
MOVS r2, #255
MVNS r2, r2
ASRS r3, r2, #1

// Positive shift by seven bits.
// ...10000000 >> 00111 = ...00000001
MOVS r4, #128
ASRS r5, r4, #7

// Negative shift by seven bits.
// 11111111 11111111 11111111 01010101 >> 00111 =
// 11111111 11111111 11111111 11111110
MOVS r6, #170
MVNS r6, r6
ASRS r7, r6, #7

// Positive shift by a byte.
// ...11001100 >> 01000 = ...00000000
MOVS r0, #204
ASRS r1, r0, #8

// Negative shift by a byte.
// 11111111 11111111 11111111 00110011 >> 01000 =
// 11111111 11111111 11111111 11111111
MOVS r2, #204
MVNS r2, r2
ASRS r3, r2, #8

// Positive shift by three bytes.
// ...11000011 >> 11000 = ...00000000
MOVS r4, #195
ASRS r5, r4, #24

// Negative shift by three bytes.
// 11111111 11111111 11111111 00111100 >> 11000 =
// 11111111 11111111 11111111 11111111
MOVS r6, #195
MVNS r6, r6
ASRS r7, r6, #24

// Positive shift itself by maximum.
// 11111111 >> 11111 = ...00000000
MOVS r0, #255
ASRS r0, r0, #31

// Negative shift itself by maximum.
// 11111111 11111111 11111111 00000000 >> 11111 =
// 11111111 11111111 11111111 11111111
MOVS r1, #255
MVNS r1, r1
ASRS r1, r1, #31

// Positive shift itself by over maximum.
// 11111111 >> 00000 = ...11111111
MOVS r2, #255
ASRS r2, r2, #32

// Negative shift itself by over maximum.
// 11111111 11111111 11111111 00000000 >> 00000 =
// 11111111 11111111 11111111 00000000
MOVS r3, #255
MVNS r3, r3
ASRS r3, r3, #32
