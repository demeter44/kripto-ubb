"""Assignment 1: Cryptography for CS41 Winter 2020.

Name: Demeter Tamás
SUNet: dtim1806

Cryptography Suite
"""
import string


#################
# CAESAR CIPHER #
#################

def encrypt_caesar(plaintext):
    """Encrypt a plaintext using a Caesar cipher.

    Add more implementation details here.

    :param plaintext: The message to encrypt.
    :type plaintext: str

    :returns: The encrypted ciphertext.
    """

    output = ""
    for c in plaintext:
        if c in string.ascii_uppercase:
            output += string.ascii_uppercase[(string.ascii_uppercase.find(c) + 3) % len(string.ascii_uppercase)]
        else:
            output += c
    return output


def decrypt_caesar(ciphertext):
    """Decrypt a ciphertext using a Caesar cipher.

    Add more implementation details here.

    :param ciphertext: The message to decrypt.
    :type ciphertext: str

    :returns: The decrypted plaintext.
    """

    output = ""
    for c in ciphertext:
        if c in string.ascii_uppercase:
            output += string.ascii_uppercase[
                (string.ascii_uppercase.find(c) + len(string.ascii_uppercase) - 3) % len(string.ascii_uppercase)]
        else:
            output += c
    return output


###################
# VIGENERE CIPHER #
###################

def encrypt_vigenere(plaintext, keyword):
    """Encrypt plaintext using a Vigenere cipher with a keyword.

    Add more implementation details here.

    :param plaintext: The message to encrypt.
    :type plaintext: str
    :param keyword: The key of the Vigenere cipher.
    :type keyword: str

    :returns: The encrypted ciphertext.
    """

    output = ""
    i = 0
    for c in plaintext:
        if c in string.ascii_uppercase:
            output += string.ascii_uppercase[
                (string.ascii_uppercase.find(c) + string.ascii_uppercase.find(keyword[i % len(keyword)])) % len(
                    string.ascii_uppercase)]
        else:
            output += c
        i += 1
    return output


def decrypt_vigenere(ciphertext, keyword):
    """Decrypt ciphertext using a Vigenere cipher with a keyword.

    Add more implementation details here.

    :param ciphertext: The message to decrypt.
    :type ciphertext: str
    :param keyword: The key of the Vigenere cipher.
    :type keyword: str

    :returns: The decrypted plaintext.
    """
    output = ""
    i = 0
    for c in ciphertext:
        if c in string.ascii_uppercase:
            output += string.ascii_uppercase[
                (string.ascii_uppercase.find(c) + len(string.ascii_uppercase) - string.ascii_uppercase.find(
                    keyword[i % len(keyword)])) % len(
                    string.ascii_uppercase)]
        else:
            output += c
        i += 1
    return output


########################################
# MERKLE-HELLMAN KNAPSACK CRYPTOSYSTEM #
########################################

def generate_private_key(n=8):
    """Generate a private key to use with the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key
    components of the MH Cryptosystem. This consists of 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        Note: You can double-check that a sequence is superincreasing by using:
            `utils.is_superincreasing(seq)`
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q`
        Note: You can use `utils.coprime(r, q)` for this.

    You'll also need to use the random module's `randint` function, which you
    will have to import.

    Somehow, you'll have to return all three of these values from this function!
    Can we do that in Python?!

    :param n: Bitsize of message to send (defaults to 8)
    :type n: int

    :returns: 3-tuple private key `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    # Your implementation here.
    raise NotImplementedError('generate_private_key is not yet implemented!')


def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in
    the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one or two lines using list comprehensions.

    :param private_key: The private key created by generate_private_key.
    :type private_key: 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    :returns: n-tuple public key
    """
    # Your implementation here.
    raise NotImplementedError('create_public_key is not yet implemented!')


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    Following the outline of the handout, you will need to:
    1. Separate the message into chunks based on the size of the public key.
        In our case, that's the fixed value n = 8, corresponding to a single
        byte. In principle, we should work for any value of n, but we'll
        assert that it's fine to operate byte-by-byte.
    2. For each byte, determine its 8 bits (the `a_i`s). You can use
        `utils.byte_to_bits(byte)`.
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk of the message.

    Hint: Think about using `zip` and other tools we've discussed in class.

    :param message: The message to be encrypted.
    :type message: bytes
    :param public_key: The public key of the message's recipient.
    :type public_key: n-tuple of ints

    :returns: Encrypted message bytes represented as a list of ints.
    """
    # Your implementation here.
    raise NotImplementedError('encrypt_mh is not yet implemented!')


def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key.

    Following the outline of the handout, you will need to:
    1. Extract w, q, and r from the private key.
    2. Compute s, the modular inverse of r mod q, using the Extended Euclidean
        algorithm (implemented for you at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum problem using c' and w to recover
        the original plaintext byte.
    5. Reconstitute the decrypted bytes to form the original message.

    :param message: Encrypted message chunks.
    :type message: list of ints
    :param private_key: The private key of the recipient (you).
    :type private_key: 3-tuple of w, q, and r

    :returns: bytearray or str of decrypted characters
    """
    # Your implementation here.
    raise NotImplementedError('decrypt_mh is not yet implemented!')


def encrypt_scytale(plaintext, circumference):
    output = "" + plaintext[0]

    i = circumference
    while len(output) != len(plaintext):
        if i >= len(plaintext):
            i = i % len(plaintext) + 1
        output += plaintext[i]
        i += circumference
    return output


def decrypt_scytale(ciphertext, circumference):
    return encrypt_scytale(ciphertext, circumference - 1)


def encrypt_railfence(plaintext, num_rails):
    rails = [['' for i in range(len(plaintext))]
             for j in range(num_rails)]

    rail = 0
    i = 0
    railstep = 1
    while i < len(plaintext):
        rails[rail].append(plaintext[i])
        rail = rail + railstep
        if rail == num_rails or rail == -1:
            railstep = railstep * (-1)
            rail = rail + (2 * railstep)
        i += 1
    out = ""

    for r in rails:
        for c in r:
            out += c

    return out


def decrypt_railfence(ciphertext, num_rails):
    rail = [['' for i in range(len(ciphertext))]
            for j in range(num_rails)]

    going_down = True
    row, col = 0, 0

    for i in range(len(ciphertext)):
        if row == 0:
            going_down = True
        if row == num_rails - 1:
            going_down = False

        rail[row][col] = '.'
        col += 1

        if going_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(num_rails):
        for j in range(len(ciphertext)):
            if ((rail[i][j] == '.') and
                    (index < len(ciphertext))):
                rail[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):

        if row == 0:
            going_down = True
        if row == num_rails - 1:
            going_down = False

        if rail[row][col] != '.':
            result.append(rail[row][col])
            col += 1

        if going_down:
            row += 1
        else:
            row -= 1

    out = ""
    for c in result:
        out += c

    return out

def encrypt_scytale_file(filename, circumference):
    f = open(filename, "rb")
    file_data = f.read().decode()
    output = ""
    output+=(file_data[0])
    i = circumference
    while len(output) != len(file_data):
        if i >= len(file_data):
            i = i % len(file_data) + 1
        output+=(file_data[i])
        i += circumference

    g = open("encrypted", "wb")
    g.write(str.encode(output))

def decrypt_scytale_file(filename,circumference):

    f = open(filename, "rb")
    file_data = f.read().decode()
    output = ""
    output+=(file_data[0])
    i = circumference-1
    while len(output) != len(file_data):
        if i >= len(file_data):
            i = i % len(file_data) + 1
        output+=(file_data[i])
        i += circumference-1
    g = open("decrypted", "wb")
    g.write(str.encode(output))
