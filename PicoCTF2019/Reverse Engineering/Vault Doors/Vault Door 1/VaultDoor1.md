# Vault Door 1
This is a continuation of the Vault Door challenges.<br><br>
In this challenge we can see that the base code is the same as the previous vault code challenges but the checkPassword algorithm has changed. Let's take a look at the new algorithm.

## Base Code
![Vault Door 1 Base Code](./images/vd1_base.png)
## checkPassword
![Vault Door 1 checkPassword](./images/vd1_checkPassword.png)

It looks like the new password should be 32 characters in length and it is checking for specific characters at a specific index. So, `charAt(0) == 'd'` would mean that the first letter of the password must be a "d". If that's the case the lets reorganize it.It should look like:
## checkPassword Organized
![Vault Door 1 checkPassword Organized](./images/vd_checkPassword_organized.png)

Now we can just read straight down to see that the password is 
<font color="green">d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4</font>. Since the base code is the same, we need to submit it in the same format as last time which is `picoCTF{}`. The password should be 
<font color=green>picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_f6daf4}</font>. Let's give it a try. 

![Vault Door 1 Access Granted](./images/vd1_access_granted.png)

Success!