// Set the registers.
MOVS r0, #1
MOVS r1, #2
MOVS r2, #3
MOVS r3, #4
MOVS r4, #5
MOVS r5, #6
MOVS r6, #7
MOVS r7, #8

// Store in first registers.
STR r0, [SP]
STR r1, [SP, #4]
STR r2, [SP, #8]
STR r3, [SP, #12]
STR r4, [SP, #16]
STR r5, [SP, #20]
STR r6, [SP, #24]
STR r7, [SP, #28]

// Store in last registers.
STR r0, [SP, #992]
STR r1, [SP, #996]
STR r2, [SP, #1000]
STR r3, [SP, #1004]
STR r4, [SP, #1008]
STR r5, [SP, #1012]
STR r6, [SP, #1016]
STR r7, [SP, #1020]
