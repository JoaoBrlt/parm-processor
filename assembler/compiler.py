#!/usr/bin/env python

# System.
import os
import subprocess

# Arguments.
import argparse

# Assembler.
from assembler import Assembler

# Helper.
from helper import Helper


class Compiler:
	"""
	Compiles programs.
	"""

	@staticmethod
	def __parse_arguments():
		"""
		Parses the arguments.

		:return: The parsed arguments.
		"""

		# Parse the arguments.
		argument_parser = argparse.ArgumentParser()
		argument_parser.add_argument("file", help="select the input C file")
		argument_parser.add_argument("-o", "--output", help="select the output logisim file")
		argument_parser.add_argument("-k", "--keep-assembly", action="store_true", help="keep the temporary assembly file")
		argument_parser.add_argument("-s", "--only-assembly", action="store_true", help="compile to assembly language only")
		return vars(argument_parser.parse_args())

	@staticmethod
	def compile(input_path: str, output_path: str):
		"""
		Compiles a program.

		:param input_path: The input C source file.
		:param output_path: The output assembly file.
		"""

		# Check the input file.
		if os.path.exists(input_path):

			# Compile the program.
			# command = "clang -S -target arm-none-eabi -mcpu=cortex-m0 -O0 -mfloat-abi=soft --output {output} {input}"
			command = "arm-linux-gnueabi-gcc {input} -S -mtune=cortex-m0 -march=armv7-m -mthumb -fomit-frame-pointer -o {output}"
			command = command.format(input=input_path, output=output_path)
			subprocess.run(command.split(" "))

			# Check the output file.
			if not os.path.exists(output_path):
				print("Compiler error: Error while compiling the program.")

		else:
			print("Compiler error: No such file '{}'.".format(input_path))

	@staticmethod
	def run():
		"""
		Runs the compiler.
		"""

		# Parse the arguments.
		options = Compiler.__parse_arguments()

		# Set the default output.
		if options["output"] is None:
			options["output"] = Helper.replace_extension(options["file"], "out")

		# Compile to assembly only.
		if options["only_assembly"]:
			# Compile the program.
			Compiler.compile(options["file"], options["output"])

		else:
			# Compile the program.
			temporary_path = Helper.replace_extension(options["output"], "s")
			Compiler.compile(options["file"], temporary_path)

			# Assemble the program.
			Assembler.assemble(temporary_path, options["output"])

			# Remove the assembly file.
			if not options["keep_assembly"]:
				os.remove(temporary_path)


# Run the compiler.
if __name__ == "__main__":
	Compiler.run()
