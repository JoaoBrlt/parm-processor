// Shift by a bit.
// ...00000001 << 00001 = ...00000010
MOVS r0, #1
MOVS r1, #1
LSLS r1, r0

// Shift by seven bits.
// ...00000001 << 00111 = ...10000000
MOVS r2, #7
MOVS r3, #1
LSLS r3, r2

// Shift by a byte.
// ...10101010 << 01000 = ...10101010 00000000
MOVS r4, #8
MOVS r5, #170
LSLS r5, r4

// Shift by three bytes.
// ...11001100 << 11000 = 11001100 00000000 00000000 00000000
MOVS r6, #24
MOVS r7, #204
LSLS r7, r6

// Shift by maximum.
// ...11111111 << 11111 = 1000000 00000000 00000000 00000000
MOVS r0, #31
MOVS r1, #255
LSLS r1, r0

// Shift by over maximum.
// ...11111111 << 00000 = ...11111111
MOVS r2, #32
MOVS r3, #255
LSLS r3, r2

// Shift itself.
// ...10000001 << 00001 = ...00000001 00000010
MOVS r4, #129
LSLS r4, r4
