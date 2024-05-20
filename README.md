The task is to read a list of integers from an input file and generate an output file containing only the unique integers from the input. The implementation avoids using built-in libraries such as `Set`, `Array`, or `Sorted`.

### Prerequisites

- Python installed on your machine

### Running the Program

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/cysron-b/dsa_UniqueInt.git
   cd /dsa_UniqueInt/hw01/
   ```

2. **Prepare Input Files:**

   Place your input text files in the `sample_inputs` directory.

3. **Ensure Output Directory Exists:**

   Make sure the `sample_results` directory exists:
   
   ```sh
   mkdir -p sample_results
   ```

### Input and Output

- **Input Files:**
  - Input files should be placed in the `sample_inputs` directory.
  - Each input file should contain one integer per line.

- **Output Files:**
  - Output files will be generated in the `sample_results` directory.
  - Each output file will contain the unique integers from the corresponding input file, sorted in ascending order.

## Example

Here's an example of how the input and output files should look:

- **Input File (`input1.txt`):**
  ```
  5
  3
  5
  -2
  8
  -2
  10
  3
  ```

- **Output File (`input1_results.txt`):**
  ```
  -2
  3
  5
  8
  10
  ```

