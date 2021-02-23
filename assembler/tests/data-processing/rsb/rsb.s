// Reverse a positive value.
// 0 - 1 = -1
MOVS r0, #1
RSBS r1, r0, #0

// Reverse a positive value.
// 0 - 149 = -149
MOVS r2, #149
RSBS r3, r2, #0

// Reverse a negative value.
// 0 - (-200) = 200
MOVS r4, #200
RSBS r5, r4, #0
RSBS r6, r5, #0

// Reverse same register.
// 0 - 87 = -87
MOVS r7, #87
RSBS r7, r7, #0
