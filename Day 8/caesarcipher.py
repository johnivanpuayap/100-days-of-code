alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    if position != -1:
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

exit = 'yes'
while exit == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > len(alphabet):
        shift %= len(alphabet)
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    exit = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")


