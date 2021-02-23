// Add two positive values
// 76 + 184 + 0 = 260
// Flags = 0000
MOVS r0, #76
MOVS r1, #184
ADCS r1, r0

// Add two opposite sign values
// -1 + 255 + 0 = 254
// Flags = 0010
MOVS r2, #0
MVNS r2, r2
MOVS r3, #255
ADCS r3, r2

// Add two positive values (with carry in).
// 102 + 150 + 1 = 253
// Flags = 0000
MOVS r4, #102
MOVS r5, #150
ADCS r5, r4

// Add two negative values.
// -256 + (-1) + 0 = -257
// Flags = 1010
MOVS r6, #255
MVNS r6, r6
MOVS r7, #0
MVNS r7, r7
ADCS r7, r6

// Add the same register (with carry in).
// 150 + 150 + 1 = 301
// Flags = 0000
MOVS r0, #150
ADCS r0, r0
