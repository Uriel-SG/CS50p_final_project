#Modules needed
import sys
from fpdf import FPDF
from PIL import Image
from pyfiglet import Figlet
import time
import cowsay
import base64


#FUNCTIONS

#The main function of the program
def main():
	global encryption
	try:
		#We call the title function to start our program
		title()

		while True:
			#We assign the variable "choice" to the start function, which shows the options
			choice = start()

			if choice == "1":
				#We call the encrypt function and assign the variable "uriel_string" to it. The function will return the encrypted string
				uriel_string = encrypt(input("Write here the string to encrypt: \n\n--> ").lower().strip())
				print("\nUriel Message:\n\n")
				print(uriel_string)
				print("\n\nDone!")

				while True:
					#We ask the user for a pdf file of the encrypted string
					ifpdf = (input("\n\nDo you want to print your message as PDF? (y/n)  ")).lower().strip()
					if ifpdf == "y":
						try:
							#We call the print_pdf function that creates 'uriel_message.pdf'. The function will generate a 'txt' version too.
							print_pdf()
							time.sleep(0.2)
							print("\n\nPDF succesfully created and saved in your working directory as 'uriel_message.pdf'!\n")
							time.sleep(0.5)
							print("A 'uriel_message.txt' was generated too. It could be useful.")
							time.sleep(0.5)
							print("\n\nPress ENTER to go back to the main menu")
							input()
							break
						except:
							print("\nSorry, somerhing went wrong with the creation of the PDF")
							break
					elif ifpdf == "n":
						break
					else:
						continue
				#Reset of the global variable encryption
				encryption = ""

			elif choice == "2":
				try:
					#We call the decrypt function and assign the variable "decrypted_string" to it. The function will return the decrypted string
					decrypted_string = decrypt(input("Write here the string to decrypt: \n\n--> ").lower().strip())
				except:
					time.sleep(0.5)
					print("\n\nSorry, something went wrong. Are you sure that you string is an Uriel Message?")
					time.sleep(0.5)
					print("\nPress ENTER to continue")
					input()
					continue
				if decrypted_string == "":
					time.sleep(0.5)
					print("\n\nSorry, something went wrong. Are you sure that you string is an Uriel Message?")
					time.sleep(0.5)
					print("\nPress ENTER to continue")
					input()
					continue
				print("\nDecrypted message:\n\n")
				print(decrypted_string)

				#We call the write_text function to write the decrypted string on a text file ('uriel_message.txt')
				write_text(decrypted_string)
				print("\n\nDone!")
				time.sleep(0.5)
				print("\nA '.txt' file called 'uriel_message.txt' with your decrypted message was generated in your working directory.")
				time.sleep(0.5)
				print("\n\nPress ENTER to continue or exit...")
				input()

			elif choice == "3":
				#Paranoid mode: to encode/decode ad uriel string in base64
				paranoid = paranoid_menu()
				while True:
					if paranoid == "1":
						#Encrypt the message
						uriel = encrypt(input("Write here the string to encrypt and encode: \n\n--> ").lower().strip())
						#Encode the message
						paranoid_string = paranoid_uriel_encode(uriel)
						print("\n\nDone!\n\n")
						time.sleep(0.5)
						print("Your paranoid uriel base64 message: \n\n")
						time.sleep(0.5)
						print(paranoid_string)
						time.sleep(0.8)
						print("\n\nPress ENTER to go back to the main menu")
						input()
						#Reset of the global variable encryption
						encryption = ""
						break
					elif paranoid == "2":
						try:
							#Decode the message
							decoded_string = paranoid_urieldecrypt(input("Write here the string to decode and decrypt: \n\n--> "))
						except:
							time.sleep(0.5)
							print("\nSorry, something went wrong. Are you sure that your string is a base64 string?")
							time.sleep(0.5)
							print("\nPress enter to continue")
							input()
							break
						try:
							#Decrypt the message
							decrypted_string_p = decrypt(decoded_string)
							print("\n\nDone!\n\n")
							time.sleep(0.5)
							print("Your paranoid decoded and decrypted message: \n\n")
							time.sleep(0.5)
							print(decrypted_string_p)
							time.sleep(0.8)
							print("\n\nPress ENTER to go back to the main menu")
							input()
							break
						except:
							time.sleep(0.5)
							print("\nSorry, something went wrong. Are you sure that your string is an Uriel Code string?")
							time.sleep(0.5)
							print("\nPress enter to continue")
							input()
							break

					else:
						print("Please, choose '1', '2'\n")

			elif choice == "4":
				#We call the end_program function to exit'
				end_program()
			else:
				print("Please, choose '1', '2' or '3'\n")

	except KeyboardInterrupt:
		#If the user use a KeyboardInterrupt command (ex: '^C'), the end_program function will be called
		end_program()
	except EOFError:
		end_program()


#A title for the program, generated with the figlet module
def title():
	figlet = Figlet()
	figlet.setFont(font="cybermedium")
	print(figlet.renderText("Uriel Code"))


#Start function: contains the option menu of the program. Returns the user's choice
def start():
	time.sleep(0.5)
	print("\nChoose an option:\n")
	time.sleep(0.5)
	print("  	1) Encrypt")
	time.sleep(0.3)
	print("  	2) Decrypt")
	time.sleep(0.3)
	print("  	3) Paranoid Mode")
	time.sleep(0.3)
	print("  	4) Exit\n")
	time.sleep(0.3)
	choice = str(input("-> "))
	return choice


#A greeting function to exit the program. Figlet and cowsay modules are combined
def end_program():
	figlet = Figlet()
	figlet.setFont(font="cybermedium")
	sys.exit(cowsay.get_output_string("fox", (figlet.renderText("Bye")) + "\n~~~~~~~~~~~~~~~\nZ 6 R 2 O"))


#Function to create a pdf file using the module fpdf. A '.txt' file is generated too
def print_pdf():
	global encryption
	pdf = FPDF(orientation="P", unit="mm", format="A4")
	pdf.add_page()
	pdf.set_auto_page_break(True)
	pdf.set_font('helvetica', "B", size=45)
	pdf.cell(190.0, 15.25 , "~ Uriel Message ~", align='C')
	#We use PIL.Image to open and resize the image
	im = Image.open("uriel.png")
	uriel_logo = im.resize((204, 223))
	pdf.image(uriel_logo, 68, 33)
	pdf.ln(105)
	pdf.set_font('times', "B", size=20)
	pdf.multi_cell(0, 17, txt=encryption, align="C")
	pdf.output("uriel_message.pdf")
	#The write_text function is called to write the message on a '.txt' file'
	write_text(encryption)


#Function for writing the encrypted message on a text file
def write_text(string):
	with open("uriel_message.txt", "w") as f:
		f.write(string)



#The heart of our job:

#1) The Encrypt function
def encrypt(user_string):
	global encryption
	for letter in user_string:
		if letter in alphabet:
			encryption += (alphabet[letter] + " ")
		else:
			encryption += letter + " "
	punctuation = [".", ",", "?", "!"]
	for p in punctuation:
		if p in encryption:
			p = encryption.index(p)
			if encryption[p - 1] == " ":
				encryption = encryption[:p-1] + encryption[p:]
	return encryption


#2) The Decrypt function
def decrypt(user_string):
	try:
		decryption = ""
		punctuation = [".", ",", "?", "!"]
		for p in punctuation:
			if p in user_string:
				p = user_string.index(p)
				user_string = user_string[:p] + " " + user_string[p:]
		string_list = user_string.split(" ")
		for x in string_list:
			if x == "":
				decryption += " "
			for key in alphabet:
				if  x == alphabet[key]:
					decryption += key
		specials = ["à", "á", "ã", "â", "ä", "é", "è", "ë", "ê", "ì", "í", "î", "ï", "ò", "ó", "õ", "ô", "ö", "ú", "ù", "û", "ü", "ç"]
		for l in specials:
			if l in decryption:
				decryption = decryption.replace(l, "")
		return decryption
	except:
		raise ValueError("Something went wrong")

#The PARANOID option (encrypt/decrypt + encode/decode base64)
def paranoid_menu():
	print("\n\n")
	time.sleep(0.2)
	cowsay.fox("Welcome to the Paranoid Mode!")
	print('''

			Choose an option:

				1) encrypt and base64 encode

				2) base64 decode and decrypt

				''')
	choice = input("--> ")
	return choice


#base64 encode function
def paranoid_uriel_encode(uriel):
	uriel_bytes = uriel.encode("ascii")
	base64_bytes = base64.b64encode(uriel_bytes)
	base64_string = base64_bytes.decode("ascii")
	return base64_string


#base64 decode function
def paranoid_urieldecrypt(b64_string):
	base64_bytes = b64_string.encode("ascii")
	string_bytes = base64.b64decode(base64_bytes)
	final = string_bytes.decode("ascii")
	return final


#The 'alphabet' map of the Uriel Code (a python dictionary)
alphabet = {
		"a": "f",
		"à": "f",
		"á": "f",
		"ã": "f",
		"â": "f",
		"ä": "f",
		"b": "e",
		"c": "d",
		"ç": "d",
		"d": "3",
		"e": "2",
		"è": "2",
		"é": "2",
		"ê": "2",
		"ë": "2",
		"f": "1",
		"g": "t",
		"h": "s",
		"i": "r",
		"ì": "r",
		"í": "r",
		"î": "r",
		"ï": "r",
		"j": "q",
		"k": "p",
		"l": "o",
		"m": "n",
		"n": "10",
		"o": "9",
		"ò": "9",
		"ó": "9",
		"ô": "9",
		"õ": "9",
		"ö": "9",
		"p": "8",
		"q": "7",
		"r": "6",
		"s": "5",
		"t": "4",
		"u": "z",
		"ù": "z",
		"ú": "z",
		"û": "z",
		"ü": "z",
		"v": "y",
		"w": "x",
		"x": "13",
		"y": "12",
		"z": "11",
		".": ".",
		",": ",",
		"?": "?",
		"!": "!",
		"0": "0",
		"1": "a",
		"2": "b",
		"3": "c",
		"4": "g",
		"5": "h",
		"6": "i",
		"7": "j",
		"8": "k",
		"9": "l"}


#A global variable used for the print_pdf function
encryption = ""


if __name__ == "__main__":
	main()
