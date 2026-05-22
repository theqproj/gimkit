# Gimkit PIN Finders

## How to use:
* **Basic Finder:** Install Python, install the dependencies (`
pip install requests`)  then download and run the script (basic.py)

* **Tor Finder:** See the setup instructions below.

## Setting up the Tor Finder

> [!NOTE]
> Setting up the Tor Finder locally is only recommended if you know what you're doing. If not, you can run it on Google Colab [here](https://colab.research.google.com/drive/1rL5MrrAqzQZ6QyOl8SD0NjJrcXLmtWj0#scrollTo=k-yn31Bv2Dym) without needing to configure anything yourself.

### 1. Install Tor
First, install Tor on your machine. A handy installation guide for Windows, macOS, and Linux can be found [here](https://gist.github.com/lukechilds/0be1d56ecd28092822e4fa750b5945c0).


Open your file manager or terminal and locate the `torrc` configuration file. It's typically found under these paths based on your operating system:

* **Windows:** `C:\Users\<your-username>\AppData\Roaming\tor\torrc` 
* **macOS (Apple Silicon M1/M2/M3):** `/opt/homebrew/etc/tor/torrc`
* **macOS (Intel):** `/usr/local/etc/tor/torrc`
* **Linux:** `/etc/tor/torrc`

Open this file and add these 2 lines:
```text
ControlPort 9051

# This line sets the password to "d" by default.
# If you are running this as sudo, you can remove this line.
# To change the password, run tor --hash-password {password here}
# and replace everything after 16: with the output.
# You will also have to change the value of password on line 28.
HashedControlPassword 16:A76A9C9AA4FE6C1C60035686C9B38C93C5A092E3BF702F55CF46E8B944

```

*(Note: Editing this file requires **sudo privileges** on Linux)


### Starting Tor

On Windows, open the command prompt and navigate to the unzipped folder with the Tor files and run
```cmd
tor.exe
```

On Mac, run 
```zsh
brew services start tor
```

And on Linux, run 
```bash
sudo service start tor
```

Next, check if it's running.

On windows, the command prompt window should show `[notice] Bootstrapped 100% (done)
` somewhere in the window once Tor's running.

For Mac and Linux, run these comamnds:

Mac:
Run `brew services list
` and look for "tor" in the results.

Linux: `sudo service tor status`

Finally, install the dependencies for the script:

```
pip install stem requests
```

then download and run the code (tor.py).

