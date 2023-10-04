# K3ygenme

Starting off with Ghidra, the main function can be found in the function folder.

![Main](./images/main.png)

Notice that there is a ``validate_key`` function. It will probably lead to solving the crackme. Navigating to the function with the decompiler shows some logic.

![Validate Key](./images/validate_key.png)

It looks like as long as the password is divisble by 1223 then it will work.

![Password](./images/password.png)