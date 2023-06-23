import random
import math

def multiply_modulo(a, b, modulus):
    # Performs modular multiplication (a * b) mod modulus
    return (a * b) % modulus

def rsa_encrypt(message, public_key):
    # Encrypts the message using the public key (n, e)
    n, e = public_key
    return pow(message, e, n)

def rsa_decrypt(ciphertext, private_key):
    # Decrypts the ciphertext using the private key (n, d)
    n, d = private_key
    return pow(ciphertext, d, n)

def introduce_fault(ciphertext, fault_position):
    # Introduces a fault by multiplying the ciphertext at a specific position by a random value
    ciphertext_list = list(str(ciphertext))
    fault_value = random.randint(2, 9)  # Random value to introduce the fault
    ciphertext_list[fault_position] = str(multiply_modulo(int(ciphertext_list[fault_position]), fault_value, 10))
    return int(''.join(ciphertext_list))

# Generate RSA key pair
def generate_key_pair():
    # Randomly generate two large prime numbers p and q
    p = random.randint(100, 1000)
    while not is_prime(p):
        p = random.randint(100, 1000)

    q = random.randint(100, 1000)
    while not is_prime(q):
        q = random.randint(100, 1000)

    # Calculate modulus n and Euler's totient function phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose a public exponent e (commonly 65537)
    e = 65537

    # Compute the private exponent d using the modular multiplicative inverse of e modulo phi(n)
    d = modular_inverse(e, phi)

    # Return public and private keys
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

def is_prime(n):
    # Check if a number is prime
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def modular_inverse(a, m):
    # Calculate the modular multiplicative inverse of a modulo m
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist.')
    return x % m

def extended_gcd(a, b):
    # Extended Euclidean Algorithm to calculate gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b)
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Generate RSA key pair
public_key, private_key = generate_key_pair()

# Message to be encrypted
message = 42

# Encrypt the message using the public key
ciphertext = rsa_encrypt(message, public_key)

# Introduce a fault in the ciphertext at a specific position
fault_position = random.randint(0, len(str(ciphertext)) - 1)
faulty_ciphertext = introduce_fault(ciphertext, fault_position)

# Attempt to decrypt the faulty ciphertext using the private key
recovered_message = rsa_decrypt(faulty_ciphertext, private_key)

# Print the results
print("Original Ciphertext:", ciphertext)
print("Faulty Ciphertext:", faulty_ciphertext)
print("Recovered Message:", recovered_message)
