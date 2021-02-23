#!/usr/bin/env python

# System.
import os
import glob

# Parser.
from syntaxic import parser

# Colors.
from colorama import Fore, Style


class Checker:
	"""
	Checks the functioning of the assembler.
	"""
	@staticmethod
	def __compare(actual: str, expected: str):
		actual = actual.replace("\r", "")
		expected = expected.replace("\r", "")
		return actual == expected

	@staticmethod
	def run():
		# For each test category.
		categories = glob.glob("tests/*")
		for category in categories:
			category_name = os.path.basename(category).replace("-", " ").title()
			print(category_name, ":", sep="")

			# For each test.
			tests = glob.glob(category + "/*")
			for test in tests:
				# Read the input.
				input_path = glob.glob(test + "/*.s")[0]
				input_file = open(input_path, "r")
				data = input_file.read()
				input_file.close()

				# Read the expected result.
				output_path = glob.glob(test + "/*.out")[0]
				output_file = open(output_path, "r")
				expected_result = output_file.read()
				output_file.close()

				# Compute the actual result.
				actual_result = parser.parse(data)

				# Compare with the results.
				test_name = os.path.splitext(os.path.basename(input_path))[0].upper()
				print("  ", test_name, ":", sep="", end="")
				if Checker.__compare(actual_result, expected_result):
					print(Fore.GREEN, "Passed", Style.RESET_ALL)
				else:
					print(Fore.RED, "Failed", Style.RESET_ALL)
					print("Expected:", expected_result)
					print("Actual:", actual_result)


# Run the checker.
if __name__ == "__main__":
	Checker.run()
