// First example.
// ...00000000 AND ...00000000 = ...00000000
MOVS r0, #0
MOVS r1, #0
ANDS r1, r0

// Second example.
// ...00000000 AND ...11111111 = ...00000000
MOVS r2, #0
MOVS r3, #255
ANDS r3, r2

// Third example.
// ...11111111 AND ...00000000 = ...00000000
MOVS r4, #255
MOVS r5, #0
ANDS r5, r4

// Fourth example.
// ...11111111 AND ...11111111 = ...11111111
MOVS r6, #255
MOVS r7, #255
ANDS r7, r6

// Same register.
// ...10101010 AND ...10101010 = ...10101010
MOVS r0, #170
ANDS r0, r0
