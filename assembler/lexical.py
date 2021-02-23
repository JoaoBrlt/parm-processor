# Lex.
import ply.lex as lex

# List of tokens.
tokens = [
	"LABEL",
	"REGISTER",
	"INTEGER",
	"STACK_POINTER",
	"COMMAND"
]

# Literal characters.
literals = ["[", "]", ",", ":"]

# Ignored characters.
t_ignore = " \t"


# Ignore comments.
def t_COMMENT(t):
	r"@.*"
	pass


# Ignore comments.
def t_COMMENT_bis(t):
	r"//.*"
	pass


# Ignore directives.
def t_DIRECTIVE(t):
	r"\..*[ \t]+.*"
	pass


# Label name.
def t_LABEL(t):
	r"(?i)(\.[a-z0-9_]+|main)"
	return t


# Register name.
def t_REGISTER(t):
	r"(?i)r[0-9]+"
	t.value = int(t.value[1:])
	return t


# Integer value.
def t_INTEGER(t):
	r"\#[-+]?[0-9]+"
	t.value = int(t.value[1:])
	return t


# Stack pointer.
def t_STACK_POINTER(t):
	r"(?i)sp"
	t.value = t.value.lower()
	return t


# Command name.
def t_COMMAND(t):
	r"(?i)[a-z]+"
	t.value = t.value.lower()
	if len(t.value) == 4 and t.value[3] == 's':
		t.value = t.value[:-1]
	return t


# New line.
def t_newline(t):
	r"\n+"
	t.lexer.lineno += len(t.value)


# Lexical error.
def t_error(t):
	print("Lexical error: Illegal character '%s'." % t.value[0])
	t.lexer.skip(1)


# Build the lexer.
lexer = lex.lex()
if __name__ == "__main__":
	lex.runmain()
