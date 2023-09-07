# EncrypDir:


![N|](https://i.imgur.com/BfDZYgU.png)

# what is EncrypDir?? :
EncrypDir is a versatile and user-friendly directory encryption and decryption tool designed to safeguard your sensitive data with ease and efficiency. Whether you need to secure personal documents, confidential work files, or any sensitive information, EncrypDir provides a robust and intuitive solution for your data protection needs.
___
# screenshots :
![N](https://i.imgur.com/fFe9aHL.png)

## Features :

- **Effortless Encryption:** EncrypDir simplifies the encryption process, allowing users to secure their files with just a few clicks. Encrypt files and directories effortlessly, ensuring your data remains confidential and safe from unauthorized access.
- **Strong Security:** Built on the Fernet symmetric encryption scheme, EncrypDir employs state-of-the-art cryptography to ensure the confidentiality and integrity of your data. Your information is protected with a strong encryption algorithm and hash-based message authentication.
- **Files Integrity:** EncrypDir safeguards the integrity of your encrypted files, ensuring that they cannot be tampered with. Your data remains pristine and secure.
- **Educational and Ethical Use:** EncrypDir is intended for educational and ethical use. Users must adhere to applicable laws and regulations when utilizing this tool, ensuring responsible and legal data protection practices.

# what is information gathering :

> Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. [Fernet](https://github.com/fernet/spec/) is an implementation of symmetric (also known as “secret key”) authenticated cryptography. Fernet also has support for implementing key rotation via [`MultiFernet`](https://cryptography.io/en/latest/fernet/#cryptography.fernet.MultiFernet "cryptography.fernet.MultiFernet")

for more reading click here [Fernet (symmetric encryption)](https://cryptography.io/en/latest/fernet/)



## Tested On :
```sh
Ubuntu
Kali linux 
Termux
Windows
```

## Installation and usage  :

EncrypDir requires [Python3](https://www.python.org/downloads/release/python-3810/) v3.8.10+ to run.
also You need [pip](https://pypi.org/project/pip/) v20.0.2+ to run.
Install the dependencies and devDependencies from the git clone command and the requirtment file then run the tool in any given directory you want to encrypt.
The tool will generate a decryption key on the same directory you are on after the encryption process.
When you want to decrypt the directory run the EncrypDir tool on the encrypted diractory then specify the path to the decryption key where it is stored.
keep this decryption key and don't lose it !! because you need it to decrypt the encrypted files in the directory.

```sh
sudo apt update
git clone https://github.com/rexerf16/EncrypDir.git
pip install -r requirements.txt
python3 encrypdir.py
```
# Practical usage for this tool :
You can save the decryption key on any given media holders like :
```sh
USB sticks, Exsternal Hardisks, Cloude storgaes 
```
# Harsh disclaimer  :
the author of this tool is not responsible for any lost or damaged data nor any illegal misuse of this tool. use this tool with your own discretion. 


# Version :
| Version    | Featurtes                                                                                                                                                                                                                                                          |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| V('0.1.0') | Current version updated features is coming....... |


# License
MIT License

Copyright (c) 2023 Mohammed Farhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
