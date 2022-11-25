# **Uriel Code**

![Urielnewpiccola](https://user-images.githubusercontent.com/65650311/203684846-5fdac103-1dff-4b14-b1ac-50e4d3de05ce.jpg)  


#### Video Demo:

[![Watch the video](https://raw.githubusercontent.com/Uriel-SG/Uriel-Portal/main/example.jpg)](https://youtu.be/8EHYuSfHobg)

## Description:

The **Uriel Code** is a *crypto-code* created by Uriel-SG in 2015 on a piece of paper.

Today it's a *python script* which, starting from a string as *input*, generates a *"secret message"* (and *viceversa*).

- It's pretty simple, but useful if you need a *quick and friendly "homemade"* encryption.
- It's easy to use even *without the application* if you understand how it works.


## How does it work?

The method it's really simple: every 'alphanumeric' character corresponds to another.

The correspondence is based on the construction of a *cross-shaped drawing*.

![This is an image](small image here)

Example:

"Welcome to cs50!"

> *x 2 o d 9 n 2   4 9   d 5 h 0!*


## PDF Generation

If the user wants, it is possible to print the message in a pdf file with the *Uriel Code logo*.

#### Example:

*Input* --> "Welcome to Harvard cs50 course: introduction to Python Programming"

##### *PDFOutput sample*:

![urielpdf](https://user-images.githubusercontent.com/65650311/203441129-db1d2c74-1dd2-48a4-a826-5419601e00f7.jpg)


## Paranoid Mode

It gives the possibility to **encode** the encrypted message with the base64 method and *viceversa*.



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

## Future

Even if so simple, I really care about this project.

- I'm working on an intresting graphical interface written in tkinter. It's already "*work in progress*" but the idea is to find something more professional, modern, dynamic and interactive;
- My [brother](https://github.com/Dabolus), a really competent and brilliant programmer, *javascript* expert, worked for me on a website (*written in React*);
- If my python skills continue and improve, I'd like to write an android application using *kivy*;
- The "*Paranoid Mode*" will be improved! Now is only a base64 encoding, but it will have a much more complex and useful method, based on a ***simmetric encryption***. The Uriel Code generated will be encrypted with a *key*, and only who has that *key* will be able to decrypt the secret message;

### *That's all folks!*
*Enjoy it!*
