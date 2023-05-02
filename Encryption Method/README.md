# Encryption Method with Matrices

In this assignment, we're going to make a way to hide secret messages using matrices. We will start by giving a number to each letter of the message. Then, we will use a square matrix (which has an inverse) to change those numbers into a new set of numbers. This new set of numbers is going to represent the coded message that will be sent.

When someone receives this coded message, they can use the inverse of the matrix to change the coded numbers back into the original set of numbers. Finally, we can associate each number with its corresponding letter to get the original message.

We will use the correspondence shown in the table given below where A to Z are represented by the numbers 1 to 26, and a space is represented by the number 27.

**Encryption**
This program reads the key and input files from which it learns paths from parameters. First of all, the plain text in the input file digitized as described above. Afterward, the text encrypted by multiplying it with the key matrix in the key file.

**Decryption**
This program reads the key and input files from which it learns paths from parameters. First of all, the ciphertext in the input file read. Afterward, the ciphertext decrypted by multiplying it with inverse of the key matrix in the key file.

**Assertion**
This program is not crash when incorrect entries or commands are given. It identifies the error and writes the error message on the screen.

- "Parameter number" error: Occurs when the program has different numbers of parameters
than 4.
- "Undefined parameter" error: Occurs if a value other than "enc" or "dec" is entered in the
operation type parameter.
- "Input file not found" error: Occurs when the input file cannot be found in the path specified
by the parameter.
- "The input file could not be read" error: Occurs when the format of the input file specified by
the parameter is corrupt.
- "Input file is empty" error: Occurs when the input file specified by the parameter is empty.
- "Invalid character in input file" error: Occurs when the input file specified by the parameter
contains characters other than 26 letters and space.
- "Key file not found" error: Occurs when the key file cannot be found in the path specified by
the parameter.
- "Key file could not be read" error: Occurs when the format of the key file specified by the
parameter is corrupt.
- "Key file is empty" error: Occurs when the input file specified by the parameter is empty.
- "Invalid character in key file" error: Occurs when there are characters other than numbers and
comma in the key file specified by the parameter.
