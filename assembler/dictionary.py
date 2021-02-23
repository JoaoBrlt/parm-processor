# Command register, register, integer.

COMMAND_REGISTER_REGISTER_INTEGER = [
	{
		"opcode": "00",        # Shift, Add, Sub, Move operation.
		"bits": 5,             # Integer on 5 bits.
		"lsl": "000",          # Logical Shift Left (immediate).
		"lsr": "001",          # Logical Shift Right (immediate).
		"asr": "010"           # Arithmetic Shift Right (immediate).
	},
	{
		"opcode": "00",        # Shift, Add, Sub, Move operation.
		"bits": 3,             # Integer on 3 bits.
		"add": "01110",        # Add register (immediate).
		"sub": "01111"         # Subtract register (immediate).
	},
	{
		"opcode": "010000",    # Data Processing operation.
		"bits": 0,             # Integer is zero.
		"rsb": "1001"          # Reverse Subtract from 0 (immediate).
	}
]

# Command register, register, register.

COMMAND_REGISTER_REGISTER_REGISTER = [
	{
		"opcode": "00",        # Shift, Add, Sub, Move operation.
		"ignore_last": False,  # Use all registers.
		"add": "01100",        # Add register (register).
		"sub": "01101"         # Sub register (register).
	},
	{
		"opcode": "010000",    # Data Processing operation.
		"ignore_last": True,   # Ignore the last register.
		"mul": "1101",         # Multiply two registers (register).
	}
]

# Command register, register.

COMMAND_REGISTER_REGISTER = [
	{
		"opcode": "00",        # Shift, Add, Sub, Move operation.
		"mov": "00000000"      # Move (register).
	},
	{
		"opcode": "010000",    # Data Processing operation.
		"and": "0000",         # Bitwise AND (register).
		"eor": "0001",         # Exclusive OR (register).
		"lsl": "0010",         # Logical Shift Left (register).
		"lsr": "0011",         # Logical Shift Right (register).
		"asr": "0100",         # Arithmetic Shift Right (register).
		"adc": "0101",         # Add with Carry (register).
		"sbc": "0110",         # Subtract with Carry (register).
		"ror": "0111",         # Rotate Right (register).
		"tst": "1000",         # Set flags on bitwise AND (register).
		"cmp": "1010",         # Compare Registers (register).
		"cmn": "1011",         # Compare Negative (register).
		"orr": "1100",         # Logical OR (register).
		"bic": "1110",         # Bit clear (register).
		"mvn": "1111"          # Bitwise NOT (register).
	}
]

# Command register, integer.

COMMAND_REGISTER_INTEGER = [
	{
		"opcode": "00",        # Shift, Add, Sub, Move operation.
		"bits": 8,             # Integer on 8 bits.
		"mov": "100"           # Move (immediate).
	}
]

# Command register [stack pointer, integer]

COMMAND_REGISTER_STACK_POINTER_INTEGER = [
	{
		"opcode": "1001",      # Load Store operation.
		"address_bits": 8,     # Address on 8 bits.
		"value_bytes": 4,       # Value on 4 bytes.
		"str": "0",            # Store register (immediate).
		"ldr": "1"             # Load register (immediate).
	}
]

# Command stack pointer, stack pointer, integer.

COMMAND_STACK_POINTER_STACK_POINTER_INTEGER = [
	{
		"opcode": "10110000",  # Stack Pointer operation.
		"address_bits": 7,     # Address on 7 bits.
		"value_bytes": 4,      # Value on 4 bytes.
		"add": "0",            # Add immediate to stack pointer (immediate).
		"sub": "1"             # Subtract immediate from stack pointer (immediate).
	}
]

# Command label.

COMMAND_LABEL = [
	{
		"opcode": "1101",          # Branch operation.
		"bits": 8,                 # Address on 8 bits.
		"beq": "0000",             # Equal.
		"bne": "0001",             # Not equal.
		"bcs": "0010",             # Carry set.
		"bcc": "0011",             # Carry clear.
		"bmi": "0100",             # Minus, negative.
		"bpl": "0101",             # Plus, positive or zero.
		"bvs": "0110",             # Overflow.
		"bvc": "0111",             # No overflow.
		"bhi": "1000",             # Unsigned higher.
		"bls": "1001",             # Unsigned lower or same.
		"bge": "1010",             # Signed greater than or equal.
		"blt": "1011",             # Signed less than.
		"bgt": "1100",             # Signed greater than.
		"ble": "1101",             # Signed less than or equal.
		"bal": "1110",             # Always.
		"b":   "1110"              # Always.
	}
]


def find_category(command, array):
	for category in array:
		if command in category:
			return category
	return None
