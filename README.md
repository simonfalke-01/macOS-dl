# macOS-dl
A simple macOS curl wrapper (also supports Linux if you edit the download path in the code yourself, if you use Linux you would know how to do that already ;P)

## Usage
```
./dl <url>
```
The file will be downloaded to the Downloads folder in your home directory.

## Installation
Make sure you have python3 installed.
```
git clone https://github.com/simonfalke-01/macOS-dl.git
cd macOS-dl
pip3 install -r requirements.txt
chmod +x dl
```
Optional: `sudo cp ./dl /usr/local/bin/dl` to use anywhere in the shell with `dl`.

## Why I made this
I was tired of typing `curl -O <url>` and `mv <filename> ~/Downloads` every time I wanted to download something, *lol*.
