# Logisim simulation

The processor simulation project.

## Requirements

1. Install [Java SE 8 or higher](https://www.oracle.com/fr/java/technologies/javase-downloads.html).
2. Download [Logisim Evolution 2.15.0](https://github.com/reds-heig/logisim-evolution/releases/tag/v2.15.0).
   
## Run 

1. Run Logisim Evolution.
```bash
java -jar logisim-evolution.jar
```

2. Open the simulation project.

`File` > `Open` > [`Select logisim/parm.circ`]()

3. Load a compiled program into the ROM.

`Right click on the ROM` > `Load Image` > [`Select logisim/programs/file.out`](programs)

4. Select the simulation frequency.

`Simulate` > `Tick Frequency` > `Select the frequency`

5. Start the simulation. 

`Simulate` > `Ticks Enabled`

## Test vectors

1. Run Logisim Evolution.
```bash
java -jar logisim-evolution.jar
```

2. Open the simulation project.

`File` > `Open` > [`Select logisim/parm.circ`]()

3. Open the circuit to test.

`Tree View` > `Double click to open the circuit` 

4. Open the Test Vector window.

`Simulate` > `Test Vector`

5. Select the test vector to execute.

`File` > `Open` > [`Select logisim/tests/vectors/file.txt`](tests/vectors)

## Test chronograms

1. Run Logisim Evolution.
```bash
java -jar logisim-evolution.jar
```

2. Open the tests project.

`File` > `Open` > [`Select logisim/tests/chronograms/tests.circ`](tests/chronograms)

3. Open the circuit to test.

`Tree View` > `Double click to open the circuit`

4. Open the Chronogram window.

`Simulate` > `Chronogram`

5. Select the inputs and outputs to monitor.

6. Start the chronogram generation.

`Buttons` > `Start/stop sysclk`

7. Compare the generated chronogram with the expected one.

`Load file` > [`Select logisim/tests/chronograms/expected/file.txt`](tests/chronograms/expected)
