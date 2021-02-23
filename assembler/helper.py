#!/usr/bin/env python

# System.
import os


class Helper:
	"""
	Provides useful methods for other classes.
	"""

	@staticmethod
	def replace_extension(path, extension):
		"""
		Replaces the extension of a file.

		:param path: The file path to update.
		:param extension: The new extension.
		:return: The new file path.
		"""

		return os.path.splitext(path)[0] + "." + extension
