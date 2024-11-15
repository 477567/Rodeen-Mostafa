**Test Cases Documentation**

## Here are 9 Test Cases (1 Positive) & (8 Negative)

All Test Cases having same Precondition 

**Precondition: User is on the login page.**


**Test Case 1: Valid Username and Password**

**Steps:**
 1. Enter any of stated usernames as the username.
 2. Enter secret_sauce as the password.
 3. Click the login button.
    
**Expected Result:** User is redirected to the main page for shopping/navigation 


**Test Case 2: Invalid Username and Valid Password**

**Steps:**
 1. Enter any username rather than the stated ones.
 2. Enter secret_sauce as the password.
 3. Click the login button.
    
**Expected Result:** Error Message 'Username and password do not match any user in this service'


**Test Case 3: Valid username and invalid password**

**Steps:**
 1. Enter any of stated usernames as the username.
 2. Enter any password rather than the stated one.
 3. Click the login button.

**Expected Result:** Error Message 'Username and password do not match any user in this service'


**Test Case 4: Invalid username and password**

**Steps:**
 1. Enter any username rather than the stated ones
 2. Enter any password rather than the stated one.
 3. Click the login button.

**Expected Result:** Error Message 'Username and password do not match any user in this service'


**Test Case 5: Empty username and valid password**

**Steps:**
 1. Don't enter username
 2. Enter secret_sauce as the password.
 3. Click the login button.

**Expected Result:** Error Message 'Username is required'


__Test Case 6: Empty username and invalid password__

**Steps:**
 1. Don't enter username
 2. Enter any password rather than the stated one.
 3. Click the login button.

**Expected Result:** Error Message 'Username is required'


**Test Case 7: Valid username and empty password** 

**Steps:**
 1. Enter any of stated usernames as the username.
 2. Don't enter password
 3. Click the login button.

**Expected Result:** Error Message 'Password is required'


**Test Case 8: Invalid username and empty password**

**Steps:**
 1. Enter any username rather than the stated ones
 2. Don't enter password
 3. Click the login button.

**Expected Result:** Error Message 'Password is required'


**Test Case 9: Empty username and password**

**Steps:**
 1. Don't enter username
 2. Don't enter password
 3. Click the login button.

**Expected Result:** Error Message 'Username & Password are required'
