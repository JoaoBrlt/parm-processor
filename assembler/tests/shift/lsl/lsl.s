// Shift by zero.
// ...00000001 << 00000 = ...00000001
MOVS r0, #1
LSLS r1, r0, #0

// Shift by a bit.
// ...00000001 << 00001 = ...00000010
MOVS r2, #1
LSLS r3, r2, #1

// Shift by seven bits.
// ...00000001 << 00111 = ...10000000
MOVS r4, #1
LSLS r5, r4, #7

// Shift by a byte.
// ...10101010 << 01000 = ...10101010 00000000
MOVS r6, #170
LSLS r7, r6, #8

// Shift by three bytes.
// ...11001100 << 11000 = 11001100 00000000 00000000 00000000
MOVS r0, #204
LSLS r1, r0, #24

// Shift by maximum.
// ...11111111 << 31 = 1000000 00000000 00000000 00000000
MOVS r2, #255
LSLS r3, r2, #31

// Shift itself by a bit.
// ...10000001 << 00001 = ...00000001 00000010
MOVS r4, #129
LSLS r4, r4, #1
