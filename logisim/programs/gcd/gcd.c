int main() {
	int a = 96;
	int b = 36;

	while (a - b != 0) {
		a = a - b;

		if (b > a) {
			int c = a;
			a = b;
			b = c;

		}
	}

	return 0;
}
