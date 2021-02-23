// First example.
// ...00000000 AND (NOT ...00000000) = ...00000000
MOVS r0, #0
MOVS r1, #0
BICS r1, r0

// Second example.
// ...00000000 AND (NOT ...11111111) = ...00000000
MOVS r2, #0
MOVS r3, #255
BICS r3, r2

// Third example.
// ...11111111 AND (NOT ...00000000) = ...11111111
MOVS r4, #255
MOVS r5, #0
BICS r5, r4

// Fourth example.
// ...11111111 AND (NOT ...11111111) = ...00000000
MOVS r6, #255
MOVS r7, #255
BICS r7, r6

// Same register.
// ...10101010 AND (NOT ...10101010) = ...00000000
MOVS r0, #170
BICS r0, r0
