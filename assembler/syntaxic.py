# Regex.
import re

# Lex.
from lexical import tokens

# Yacc.
import ply.yacc as yacc

# Instruction dictionary.
from dictionary import *


# Global variables.
current_line = 1
label_positions = {}


def p_logisim_file(p):
	"""logisim_file : program"""
	p[0] = "v2.0 raw\n"  # Header.
	p[0] += p[1]         # Instructions.
	p[0] += " defd\n"    # Infinite loop.


def p_program(p):
	"""program : instructions"""

	# Replace labels with offsets.
	p[0] = replace_labels_with_offsets(p[1])

	# Convert instructions to hexadecimal.
	p[0] = convert_instructions_to_hexadecimal(p[0])

	# Convert instructions to string.
	p[0] = " ".join(p[0])


def p_instructions(p):
	"""instructions : instructions instruction"""
	global current_line

	# Previous instructions.
	p[0] = p[1]

	# New instruction.
	if p[2] is not None:
		p[0].append(p[2])
		current_line += 1


def p_instructions_bis(p):
	"""instructions : instruction"""
	global current_line

	# Initialize the instructions.
	p[0] = []

	# First instruction.
	if p[1] is not None:
		p[0] = [p[1]]
		current_line += 1


def p_label(p):
	"""instruction : LABEL ':'"""
	global label_positions

	# Store the label position.
	label_positions[p[1]] = current_line


def p_label_bis(p):
	"""instruction : LABEL"""
	pass


def p_command_register_register_integer(p):
	"""instruction : COMMAND REGISTER ',' REGISTER ',' INTEGER"""

	# Get the instruction category.
	category = find_category(p[1], COMMAND_REGISTER_REGISTER_INTEGER)
	if category is not None:

		# Check the integer.
		if 0 <= p[6] < pow(2, category["bits"]):

			# Integer on zero bits.
			if category["bits"] == 0:

				# Translate the instruction.
				p[0] = "{}{}{:03b}{:03b}".format(
					category["opcode"],  # Operation code.
					category[p[1]],      # Command code.
					p[4],                # Second register.
					p[2]                 # First register.
				)

			else:

				# Translate the instruction.
				p[0] = ("{}{}{:0" + str(category["bits"]) + "b}{:03b}{:03b}").format(
					category["opcode"],  # Operation code.
					category[p[1]],      # Command code.
					p[6],                # Integer.
					p[4],                # Second register.
					p[2]                 # First register.
				)

		else:
			print(category["bits"])
			print("Syntax error: Integer '{}' is invalid.".format(p[6]))

	else:
		print("Syntax error: Command '{}' not found.".format(p[1]))


def p_command_register_register_register(p):
	"""instruction : COMMAND REGISTER ',' REGISTER ',' REGISTER"""

	# Get the instruction category.
	category = find_category(p[1], COMMAND_REGISTER_REGISTER_REGISTER)
	if category is not None:

		# Ignore the last register.
		if category["ignore_last"]:

			# Translate the instruction.
			p[0] = "{}{}{:03b}{:03b}".format(
				category["opcode"],  # Operation code.
				category[p[1]],      # Command code.
				p[4],                # Second register.
				p[2]                 # First register.
			)

		else:

			# Translate the instruction.
			p[0] = "{}{}{:03b}{:03b}{:03b}".format(
				category["opcode"],  # Operation code.
				category[p[1]],      # Command code.
				p[6],                # Third register.
				p[4],                # Second register.
				p[2]                 # First register.
			)

	else:
		print("Syntax error: Command '{}' not found.".format(p[1]))


def p_command_register_register(p):
	"""instruction : COMMAND REGISTER ',' REGISTER"""

	# Get the instruction category.
	category = find_category(p[1], COMMAND_REGISTER_REGISTER)
	if category is not None:

		# Translate the instruction.
		p[0] = "{}{}{:03b}{:03b}".format(
			category["opcode"],  # Operation code.
			category[p[1]],      # Command code.
			p[4],                # Second register.
			p[2]                 # First register.
		)

	else:
		print("Syntax error: Command '{}' not found.".format(p[1]))


def p_command_register_integer(p):
	"""instruction : COMMAND REGISTER ',' INTEGER"""

	# Get the instruction category.
	category = find_category(p[1], COMMAND_REGISTER_INTEGER)
	if category is not None:

		# Check the integer.
		if 0 <= p[4] < pow(2, category["bits"]):

			# Translate the instruction.
			p[0] = ("{}{}{:03b}{:0" + str(category["bits"]) + "b}").format(
				category["opcode"],  # Operation code.
				category[p[1]],      # Command code.
				p[2],                # Register.
				p[4]                 # Integer.
			)

		else:
			print("Syntax error: Integer '{}' is invalid.".format(p[4]))

	else:
		print("Syntax error: Command '{}' not found.".format(p[1]))


def p_command_register_stack_pointer_integer(p):
	"""instruction : COMMAND REGISTER ',' '[' STACK_POINTER ',' INTEGER ']'
					| COMMAND REGISTER ',' '[' STACK_POINTER ']'"""

	# Get the instruction category.
	category = find_category(p[1], COMMAND_REGISTER_STACK_POINTER_INTEGER)
	if category is not None:

		# Get the address.
		assembly_address = p[7] if len(p) == 9 else 0
		instruction_address = int(assembly_address / category["value_bytes"])

		# Check the address.
		if (
			assembly_address % category["value_bytes"] == 0 and
			0 <= instruction_address < pow(2, category["address_bits"])
		):

			# Translate the instruction.
			p[0] = ("{}{}{:03b}{:0" + str(category["address_bits"]) + "b}").format(
				category["opcode"],  # Operation code.
				category[p[1]],      # Command code.
				p[2],                # Register.
				instruction_address  # Address.
			)

		else:
			print("Syntax error: Address {} is invalid.".format(assembly_address))

	else:
		print("Syntax error: Command '{}' not found.".format(p[1]))


def p_command_stack_pointer_stack_pointer_integer(p):
	"""instruction : COMMAND STACK_POINTER ',' STACK_POINTER ',' INTEGER
					| COMMAND STACK_POINTER ',' INTEGER"""

	# Get the instruction category.
	category = find_category(p[1], COMMAND_STACK_POINTER_STACK_POINTER_INTEGER)
	if category is not None:

		# Get the address.
		assembly_address = int(p[6]) if len(p) == 7 else 0
		instruction_address = int(assembly_address / category["value_bytes"])

		# Check the address.
		if (
			assembly_address % category["value_bytes"] == 0 and
			0 <= instruction_address < pow(2, category["address_bits"])
		):

			# Translate the instruction.
			p[0] = ("{}{}{:0" + str(category["address_bits"]) + "b}").format(
				category["opcode"],  # Operation code.
				category[p[1]],      # Command code.
				instruction_address  # Address.
			)

		else:
			print("Syntax error: Address '{}' is invalid.".format(assembly_address))

	else:
		print("Syntax error: Command '{}' not found.".format(p[1]))


def p_command_label(p):
	"""instruction : COMMAND LABEL"""
	category = find_category(p[1], COMMAND_LABEL)
	if category is not None:
		p[0] = "{}{}LABEL[{}/{}/{}]".format(
			category["opcode"],  # Operation code.
			category[p[1]],      # Command code.
			p[2],                # Label name.
			current_line,        # Current line.
			category["bits"]     # Offset size.
		)
	else:
		print("Syntax error: Command '{}' not found.".format(p[1]))


def p_command_command(p):
	"""instruction : COMMAND COMMAND"""
	if p[1] != "bx":
		print("Syntax error: Command '{}' not found.".format(p[1]))


def p_error(p):
	if p is not None:
		token = f"{p.type}({p.value}) on line {p.lineno}"
	else:
		token = "end of file"
	print(f"Syntax error: Unexpected {token}.")
	parser.errok()


def convert_decimal_to_binary(value, bits):
	value &= (2 << bits - 1) - 1
	result = '{:0' + str(bits) + 'b}'
	return result.format(int(value))


def convert_binary_to_hexadecimal(value):
	return "%04x" % int(value, 2)


def replace_labels_with_offsets(instructions):
	result = []

	# For each instruction.
	for instruction in instructions:

		# The instruction contains a label.
		found_label = re.search(r"^([01]+)LABEL\[(.*)/(.*)/(.*)]$", instruction)
		if found_label:

			# The label exists.
			label_name = found_label.group(2)
			if label_name in label_positions:

				# Get the information.
				instruction_start = found_label.group(1)
				current_position = int(found_label.group(3))
				offset_size = int(found_label.group(4))

				# Compute the offset.
				label_position = int(label_positions[label_name])
				offset = label_position - current_position - 3

				# Update the instruction.
				instruction = "{}{}".format(
					instruction_start,                              # Instruction start.
					convert_decimal_to_binary(offset, offset_size)  # Offset.
				)

			else:
				print("Syntax error: Label '{}' not found.".format(label_name))

		# Add the instruction.
		result.append(instruction)

	return result


def convert_instructions_to_hexadecimal(instructions):
	result = []

	# For each instruction.
	for instruction in instructions:
		# Convert the instruction.
		instruction = convert_binary_to_hexadecimal(instruction)

		# Add the instruction.
		result.append(instruction)

	return result


# Build the parser.
parser = yacc.yacc()
