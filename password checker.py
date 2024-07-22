from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Encrypt by applying a basic mathematical operation to each pixel
    encrypted_pixels = (pixels + key) % 256

    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Decrypt by reversing the mathematical operation
    decrypted_pixels = (pixels - key) % 256

    decrypted_image = Image.fromarray(decrypted_pixels.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    while True:
        print("Image Encryption Tool")
        choice = input("Would you like to (e)ncrypt or (d)ecrypt an image? (Enter 'q' to quit): ").lower()

        if choice == 'q':
            print("Exiting the program.")
            break

        if choice in ['e', 'd']:
            image_path = input("Enter the path to the image: ")
            output_path = input("Enter the output path for the processed image: ")
            key = int(input("Enter the encryption/decryption key (an integer): "))

            if choice == 'e':
                encrypt_image(image_path, output_path, key)
            elif choice == 'd':
                decrypt_image(image_path, output_path, key)
        else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
        
        print()

if __name__ == "__main__":
    main()
