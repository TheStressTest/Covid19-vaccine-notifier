# Covid 19 vaccine notifier 💉
This script will email you whenever a city you provide has any available vaccines.

## Setup:
- Install python if you dont already have it [here](https://python.org/downloads).
- Install requests using the following command:
```sh
# Windows:
py -3 -m pip install requests
# MacOS & Linux:
pip3 install reqeusts
```
Then run the main file:
```sh
# Windows:
py -3 main.py
# MacOS & Linux:
python3 main.py
```
Thats it! You can just let it run in the background and it will email you whenever a city has available vaccinations.

Now if you ever want to quit type <kbd>Ctrl</kbd> + <kbd>c</kbd> while in the terminal.

## Trouble shooting:
- Getting an error saying that password authentication failed even though you typed in the correct password?
  - This could be because you need to let google know that you are okay with insecure apps using your account. You can change that [here](https://myaccount.google.com/security).
  - If you have 2FA enabled you have to provide an account token instead of your password.
- Are you on windows and getting an erorr like `No module named pip` when you try to install requests?
  - Try running `python -m ensurepip` then installing requests again.
