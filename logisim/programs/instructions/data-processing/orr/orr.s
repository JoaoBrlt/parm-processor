// First example.
// ...00000000 OR ...00000000 = ...00000000
MOVS r0, #0
MOVS r1, #0
ORRS r1, r0

// Second example.
// ...00000000 OR ...11111111 = ...11111111
MOVS r2, #0
MOVS r3, #255
ORRS r3, r2

// Third example.
// ...11111111 OR ...00000000 = ...11111111
MOVS r4, #255
MOVS r5, #0
ORRS r5, r4

// Fourth example.
// ...11111111 OR ...11111111 = ...11111111
MOVS r6, #255
MOVS r7, #255
ORRS r7, r6

// Same register.
// ...10101010 OR ...10101010 = ...10101010
MOVS r0, #170
ORRS r0, r0
