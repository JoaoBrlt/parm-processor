./	.arch armv7-m
	.eabi_attribute 20, 1
	.eabi_attribute 21, 1
	.eabi_attribute 23, 3
	.eabi_attribute 24, 1
	.eabi_attribute 25, 1
	.eabi_attribute 26, 2
	.eabi_attribute 30, 6
	.eabi_attribute 34, 1
	.eabi_attribute 18, 4
	.file	"gcd.c"
	.text
	.align	1
	.global	main
	.syntax unified
	.thumb
	.thumb_func
	.fpu softvfp
	.type	main, %function
main:
	@ args = 0, pretend = 0, frame = 16
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	sub	sp, sp, #16
	movs	r3, #96
	str	r3, [sp, #12]
	movs	r3, #36
	str	r3, [sp, #8]
	b	.L2
.L3:
	ldr	r2, [sp, #12]
	ldr	r3, [sp, #8]
	subs	r3, r2, r3
	str	r3, [sp, #12]
	ldr	r2, [sp, #8]
	ldr	r3, [sp, #12]
	cmp	r2, r3
	ble	.L2
	ldr	r3, [sp, #12]
	str	r3, [sp, #4]
	ldr	r3, [sp, #8]
	str	r3, [sp, #12]
	ldr	r3, [sp, #4]
	str	r3, [sp, #8]
.L2:
	ldr	r2, [sp, #12]
	ldr	r3, [sp, #8]
	cmp	r2, r3
	bne	.L3
	movs	r3, #0
	mov	r0, r3
	add	sp, sp, #16
	@ sp needed
	bx	lr
	.size	main, .-main
	.ident	"GCC: (GNU) 9.3.0"
	.section	.note.GNU-stack,"",%progbits
