#!/usr/bin/env python

# System.
import os

# Arguments.
import argparse

# Parser.
from syntaxic import parser

# Helper.
from helper import Helper


class Assembler:
	"""
	Assembles programs.
	"""

	@staticmethod
	def __parse_arguments():
		"""
		Parses the arguments.

		:return: The parsed arguments.
		"""

		# Parse the arguments.
		argument_parser = argparse.ArgumentParser()
		argument_parser.add_argument("file", help="select the input assembly file")
		argument_parser.add_argument("-o", "--output", help="select the output logisim file")
		return vars(argument_parser.parse_args())

	@staticmethod
	def assemble(input_path: str, output_path: str):
		"""
		Assembles a program.

		:param input_path: The input assembly file.
		:param output_path: The output logisim file.
		"""

		# Check the input file.
		if os.path.exists(input_path):

			# Read the assembly file.
			input_file = open(input_path, "r")
			data = input_file.read()
			input_file.close()

			# Write the logisim file.
			output_file = open(output_path, "w")
			output = parser.parse(data)
			output_file.write(output)
			output_file.close()

			# Check the output file.
			if not os.path.exists(output_path):
				print("Assembler error: Error while assembling the program.")

		else:
			print("Assembler error: No such file '{}'.".format(input_path))

	@staticmethod
	def run():
		"""
		Runs the assembler.
		"""

		# Parse the arguments.
		options = Assembler.__parse_arguments()

		# Set the default output path.
		if options["output"] is None:
			options["output"] = Helper.replace_extension(options["file"], "out")

		# Assemble the program.
		Assembler.assemble(options["file"], options["output"])


# Run the assembler.
if __name__ == "__main__":
	Assembler.run()
