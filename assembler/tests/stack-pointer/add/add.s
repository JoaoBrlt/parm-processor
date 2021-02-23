// Set the registers.
MOVS r0, #1
MOVS r1, #2
MOVS r2, #3
MOVS r3, #4
MOVS r4, #5
MOVS r5, #6
MOVS r6, #7
MOVS r7, #8

// Add zero to the stack pointer.
ADD SP, SP, #0
STR r0, [SP]

// Add one to the stack pointer.
ADD SP, SP, #4
STR r0, [SP]

// Add maximum to the stack pointer.
ADD SP, SP, #508
STR r0, [SP]
STR r1, [SP, #4]
STR r2, [SP, #8]
STR r3, [SP, #12]
STR r4, [SP, #16]
STR r5, [SP, #20]
STR r6, [SP, #24]
STR r7, [SP, #28]
