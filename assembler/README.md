# Assembler

The assembler for the simulated processor.

## Requirements

1. Install [Python 3](https://www.python.org/downloads/) and [pip](https://pypi.org/).
```bash
sudo apt install python3 python3-pip
```

2. Install the [GNU cross compiler for ARM with soft float (arm-linux-gnueabi-gcc)](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-a/downloads).
```bash
sudo apt install gcc-arm-linux-gnueabi
```

3. Install the dependencies.
```bash
pip3 install -r requirements.txt
```

## Compile

- To compile a program from C language to the Logisim format :
```bash
./compiler.py [SOURCE FILE].c
```

- To compile a program from C language to the assembly language :
```bash
./compiler.py -s [SOURCE FILE].c
```

- To specify the output path :
```bash
./compiler.py [SOURCE FILE].c -o [DESTINATION FILE].out
```

## Assemble

- To assemble a program from assembly language to the Logisim format :
```bash
./assembler.py [SOURCE FILE].s
```

- To specify the output path :
```bash
./assembler.py [SOURCE FILE].s -o [DESTINATION FILE].out
```

## Test

- To test the assembler against hand-assembled instructions :

```bash
./checker.py
```
