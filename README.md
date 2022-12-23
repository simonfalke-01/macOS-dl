# macOS-dl
A simple macOS curl wrapper (also supports linux if you edit the download path in the code yourself ;P)

## Usage
```
./dl <url>
```
The file will be downloaded to the Downloads folder in your home directory.

## Installation
```
git clone https://github.com/simonfalke-01/macOS-dl.git
cd macOS-dl
chmod +x dl
```
Optional: `sudo cp ./dl /usr/local/bin/dl` to use anywhere in the shell with `dl`.

## Why did I make this
I was tired of typing `curl -O <url>` and `mv <filename> ~/Downloads` every time I wanted to download something, *lol*.