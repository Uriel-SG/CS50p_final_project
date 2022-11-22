# Uriel Code

![This is an image](https://raw.githubusercontent.com/Uriel-SG/CS50p_final_project/main/ur.jpg?token=GHSAT0AAAAAAB3QWETVM7GH2LEMON4GW25EY35KXDA)

#### Video Demo:

[![Watch the video](https://raw.githubusercontent.com/Uriel-SG/Uriel-Portal/main/example.jpg)](https://youtu.be/8EHYuSfHobg)

## Description:

The **Uriel Code** is a crypto-code created by Uriel-SG in the 2015.

- It's pretty simple, but useful if you need a *quick and friendly* encryption.
- It's easy to use even *without the application* if you understand how it works.


## How does it work?

The method it's really simple: every 'alphanumeric' character corresponds to another.

The correspondence is based on the construction of a cross-shaped drawing.

![This is an image](small image here)

Example:

"Welcome to cs50!"

> *x 2 o d 9 n 2   4 9   d 5 h 0!*


## PDF Generation

If the user wants, it is possible to print the message in a pdf file with the Uriel Code logo.

![This is an image](small image here)


## Paranoid Mode

It gives the possibility to **encode** the encrypt message with the base64 method and *vice-versa*.



"*Welcome to CS50!*"

The program will automatically encrypt the string ("*x 2 o d 9 n 2   4 9   d 5 h 0!*"), and then:

> *eCAyIG8gZCA5IG4gMiAgIDQgOSAgIGQgNSBoIDAhIA==*

#### Example:
##### *Encode-encrypt:*

|  **User input**  |   **Uriel Code**   |       **base64**         |
| ------------- | -------------  | -------------------- |
|    Harvard     | s f 6 y f 6 3  | cyBmIDYgeSBmIDYgMyA= |

##### *Decrypt-decode:*

|  **User input**  |   **Uriel Code**   |       **base64**         |
| ------------- | -------------  | -------------------- |
|   cyBmIDYgeSBmIDYgMyA=     | s f 6 y f 6 3  | harvard |
