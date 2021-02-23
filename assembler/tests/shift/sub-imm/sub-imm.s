// Subtract zero from a positive value.
// 4 - 0 = 4
MOVS r0, #4
SUBS r1, r0, #0

// Subtract one from a positive value.
// 9 - 1 = 8
MOVS r2, #9
SUBS r3, r2, #1

// Subtract two from a positive value.
// 189 - 2 = 187
MOVS r4, #189
SUBS r5, r4, #2

// Subtract three from a negative value.
// -156 - 3 = -159
MOVS r6, #155
MVNS r6, r6
SUBS r7, r6, #3

// Subtract maximum.
// 255 - 7 = 248
MOVS r0, #255
SUBS r1, r0, #7

// Subtract from same register.
// 230 - 5 = 225
MOVS r2, #230
SUBS r2, r2, #5
