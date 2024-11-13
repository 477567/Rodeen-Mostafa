**This project involved comprehensive testing of the Any.do application. 
Manual testing was conducted to ensure functional and non-functional correctness including Functions,Usability, Accessibility and adherence to design specifications. 
Performance testing applied, utilizing Android Studio's.**


# High Priority Scenarios 

## Test Scenario 1: User Authentication

**Pre- Conditions:** Application Downloaded successfully 

**Test Case ID: TC1 - Verify user can Sign In with Google**

**Steps to Execute:**
1. Open App
2. Click on Continue with Google 
3. Agree to message box appeared allows app to share information by clicking Continue 
4. Choose preferred Google account 
5. Ensure Sign In by preferred account by clicking Continue
   
**Expected Results:**
1. Successful Sign In
2. Landing on Intro page
   
**Actual Results:**
1. Signed In successfully 
2. Landed on Intro page
   
**Prioritization:** High 

**Status:** Pass 

------------------------------------------------------

**Test Case ID: TC2 - Verify user can Sign In with Apple** 

**Steps to Execute:**

1. Open App
2. Click on Sign In with Apple 
3. Choose whether to Share or Hide your mail while Signing In
4. Click Continue
5. Face ID scanned, if not then device passcode should be entered
   
**Expected Results:**
1. Sign In successful 
2. Landing on Intro page
   
**Actual Results:** 
1. Signed In successful 
2. Landing on Intro page
   
**Prioritization:** High 

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC3 - Verify User can Sign Up with Mail**

**Steps to Execute:**
1. Open App
2. Click on Mail Box logo button 
3. Enter your preferred mail 
4. Then click the right arrow after mail validation 
5. Enter Full Name  
6. Create Password 
7. Click Create Account
   
**Expected Results:**
1. Sign Up successful 
2. Landing on Intro page
   
**Actual Results:**
1. Signed Up successful 
2. Landed on Intro page
   
**Prioritization:** High

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC4 - Verify User can Sign In with Facebook** 

**Steps to Execute:** 
1. Open App 
2. Click on Facebook logo button 
3. Agree to use Facebook for Sign In by clicking Continue 
4. Enter valid credentials for Facebook Sign In, then Log In OR you can Sign In with you Saved Passwords 
5. Verifying that you’re a human by entering the Captcha 
6. Agree to requesting access for Facebook data, click Continue

**Expected Results:**
1. Sign In successful 
2. Landing on Intro page
   
**Actual Results:** 
1. Signed In successful 
2. Landed on Intro page

**Prioritization:** High 

**Status:** Pass 

------------------------------------------------------

## Test Scenario 2: List Management

**Pre - Conditions:**
1. User Signed In 
2. User chose List view 
3. User has minimum one List contains minimum one task 


**Test Case ID: TC5 - User can create a New List** 

**Steps to Execute:**
1. Get into the Home Page 
2. Click on Plus button in My Lists 
3. Add name for new List
   
**Expected Results:** 
1. New list created
2. List displayed in My Lists
   
**Actual Results:** 
1. New list created
2. List displayed in My Lists
   
**Prioritization:** High

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC6 - Verifying User can Edit existing List**

**Steps to Execute:**
1. Enter the preferred List 
2. Click on Plus button on the right side of the screen
3. Write the task 
4. Choose any valid assigning date in the future
5. Click on the Upload/ Up button for task save
   
**Expected Results:**
1. Task Saved 
2. Task in now displayed in the assigned day 
3. Actual Results: 
4. Task Saved 
5. Task in now displayed in the assigned day
   
**Prioritization:** High
**Status:** Pass

------------------------------------------------------

**Test Case ID: TC7 - Verify User can Sort a List** 

**Steps to Execute:**
1. User get into the List 
2. Click on the settings button on the upper right side for the screen 
3. Choose Sort option 
4. Choose either to Sort by Time or List
   
**Expected Results:**
1. Tasks are sorted depending on Date and Time
   
**Actual Results:** 
1. Tasks already sorted

**Prioritization:** High 

**Status:** Pass


------------------------------------------------------

**Test Case ID: TC8 - Verify User can Filter a List**

**Steps to Execute:**
1. User get into the List 
2. Click on the settings button on the upper right side for the screen 
3. Choose Filter option 
4. Choose preferred Tag from Filtration
5. Click Apply
    
**Expected Results:**
1. Filtered Tasks with chose Tag only is displayed 
2. No Tasks appear, if the chose task has no assigned Task 

**Actual Results:** 
1. Filter Tasks only appear 
2. Nothing appear if no Tasks assigned to filtered Tag

**Prioritization:** High 

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC9 - Verify User can delete a List**

**Steps to Execute:**
1. User get into the List 
2. Click on the settings button on the upper right side for the screen 
3. Choose Delete option 
4. Agree to deletion by clicking Delete 

**Expected Results:**
1. User got out of the List 
2. List is no more displayed in My Lists

**Actual Results:** 
1. User got out of the List 
2. List is no more displayed in My Lists

**Prioritization:** High 

**Status:** Pass


------------------------------------------------------

## Test Scenario 3: Task Management
**Pre - Conditions:**
1. User Signed In 
2. User chose List view 
3. User has minimum one List contains minimum one task 


**Test Case ID: TC10 - Verify that a user can mark a task as complete**
**Steps to Execute:**
1. Get into the preferred List 
2. Click on the check box beside the task
3. Click on the Task or Mark as complete button 

**Expected Results:**
1. Task is marked as completed
    
**Actual Results:** 
1. Task is marked as completed
   
**Prioritization:** Medium

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC11 - Verify that a user can unmark a completed task**

**Steps to Execute:**
1. Get into the preferred List 
2. Click on the checkbox beside the task
3. Uncheck the checkbox 

**Expected Results:**
1. Task re-assigned 

**Actual Results:** 
1. Task re-assigned 

**Prioritization:** Medium 

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC12 - Verify User can change assigned Task to another List**

**Pre- Conditions:** 
1. User Signed In 
2. User chose List view 
3. User has minimum two Lists one of them contains minimum one task 

**Steps to Execute:**
1. Get into the preferred List containing task 
2. Click on the Task 
3. Click on the List name displayed 
4. Choose preferred list to re-assign task to 
5. Click Save

**Expected Results:**
1. Task removed from the List 
2. Task is found in the new List 

**Actual Results:** 
1. Task removed from the List 
2. Task is found in the new List 

**Prioritization:** Medium

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC13 - Verifying Free Plan user can add specific Tags to Tasks**

**Steps to Execute:**
1. Get into the preferred List 
2. Click on the Task
3. Click on Add Tags
4. Choose Priority Tag 
5. Click Save 

**Expected Results:**
1. Tag displayed with the Task 

**Actual Results:** 
1. Tag displayed with the Task 

**Prioritization:** Medium 

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC4 - Verifying User can Add Subtasks or Notes**

**Steps to Execute:**
1. Get into the preferred List 
2. Click on the Task
3. Write in Subtasks & Notes as much as you need 

**Expected Results:**
1. Subtasks showed as branches with the Parent Task
2. Notes are Saved & shown when entering the Task

**Actual Results:** 
1. Subtasks showed as branches with the Parent Task
2. Notes are Saved & shown when entering the Task

**Prioritization:** High

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC15 - Verify User can attach Image to a Task in List from Camera**

**Steps to Execute:**
1. User get into the List 
2. Click on Plus button at the bottom of the screen 
3. Choose Camera 
4. Take Picture 
5. Click Use Photo 

**Expected Results:**
1. Image attached in attachments section at the screen bottom 

**Actual Results:** 
1. Image attached in attachments section at the screen bottom

**Prioritization:** High 

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC16 - Verify User can attach Video to a List from Camera**

**Steps to Execute:**
1. User get into the List 
2. Click on Plus button at the bottom of the screen 
3. Choose Camera 
4. Take Video 
5. Stop Video 
6. Click Use Video 

**Expected Results:**
1. Video attached in attachments section at the screen bottom 

**Actual Results:** 
1. Video attached in attachments section at the screen bottom 

**Prioritization:** High 

**Status:** Pass

------------------------------------------------------


**Test Case ID: TC17 - Verify User can attach Image to a List from Gallery**

**Steps to Execute:**
1. User get into the List 
2. Click on Plus button at the bottom of the screen 
3. Choose Gallery
4.Choose image 

**Expected Results:**
1. Image attached in attachments section at the bottom of the screen 

**Actual Results:** 
1. Image attached in attachments section at the screen bottom 

**Prioritization:** High 

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC18 - Verify User can attach Video to a Task in a List from Gallery**

**Steps to Execute:**
1. User get into the List 
2. Click on Plus button at the bottom of the screen 
3. Choose Gallery  
6. Select any Video 
7. Click Choose 

**Expected Results:**
1. Video attached in attachments section at the screen button 

**Actual Results:** 
1. Apps lags
2. Choose/ Cancel buttons get unclickable
3. Video is not uploaded  
4. No error messages 

**Prioritization:** High 

**Status:** Fail


------------------------------------------------------

**Test Case ID: TC19 - Verifying User Attach File to Task in a List** 

**Steps to Execute:**
1. User Open App
2. User get into List containing at least one Task 
3. User click on task
4. User click on Plus icon at the right bottom of the screen 
5. Choose Attachment 
6. Choose preferred file 

**Expected Results:**
1. File attached to Task
2. File displayed in Task Attachments 

**Actual Results:** 
1. File not attached
2. No any error messages 

**Prioritization:** High

**Status:** Fail

------------------------------------------------------

**Test Case ID: TC20 - Verifying User attach Voice Note to a Task in a List**

**Steps to Execute:**
1. User Open App
2. User get into List containing at least one Task 
3. User click on task
4. User click on Plus icon at the right bottom of the screen 
5. Choose Voice note
6. User Press to Record
7. User toggle on right icon  

**Expected Results:**
1. Voice Note attached to Task

**Actual Results:** 
1. Voice Note successfully attached

**Prioritization:** High

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC21 - Verifying User cannot save task in the past**

**Steps to Execute:**
1. Enter the preferred List 
2. Click on Plus button on the right side of the screen
3. Write the task 
4. Click on Custom date
5. Choose date in the past 

**Expected Results:**
1. Task should not be saved as type of validation 

**Actual Results:** 
1. Task is not saved 

**Prioritization:** High 

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC22 - Verifying Free Plan user cannot all Tags to Tasks**

**Steps to Execute:**
1. Get into the preferred List 
2. Click on the Task
3. Click on Add Tags
4. Choose any Tag rather than Priority Tag 
5. Click Save 

**Expected Results:**
1. Premium Tags are not clickable 
2. Nothing Change after Save 

**Actual Results:** 
1. Premium Tags are not clickable 
2. Nothing Change after Save
   
**Prioritization:** High

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC23 - Verify User can delete Task from a List**

**Steps to Execute:** 
1. Get into the preferred List 
2. Click on the Task
3. Click on settings icon on the upper left 
4. Choose to Archive Task 
5. Click Delete Task 

**Expected Result:**
1. Task deleted 
2. Task no more displayed in the List 

**Actual Results:**
Task Deleted 

**Prioritization:** High

**Status:** Pass

------------------------------------------------------

## Test Scenario 4: Calendar Management 

**Pre- Conditions:**
1. User Signed In
2. User choose Calendar view


**Test Case ID: TC24 - Verifying User can add event in calendar view**

**Steps to Execute:**
1. Get into the calendar from bottom menu
2. Create Event
3. Name Event 
4. Set start date
5. Set end date
6. Click Confirm
7. Click on Up icon/button
8. Click on Add event on displayed screen 

**Expected Results:**
1. Event created
2. Event displayed in Calendar

**Actual Results:** 
1. Event created & displayed 

**Prioritization:** High

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC25 - Verify User can edit event on Calendar**

**Steps to Execute:**
1. Get into the calendar from bottom menu
2. Click on any event or create one
3. Click Edit on the upper right
4. Change what is needed 
5. Click Done on Upper right

**Expected Results:**
1. New event change dispalyed 

**Actual Results:**
1. Changes dispalyed 

**Prioritization:** High

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC26 - Verifying user can change Calendar View** 

**Steps to Execute:** 
1. Get into Calendar View 
2. Click on menu on top left of the screen 
3. Choose preferred view 

**Expected Results:** 
1. View change depending on choice (2/3 columns)

**Actual Results:**
1. View changed

**Prioritization:** High

**Status:** Pass

------------------------------------------------------

## Test Scenario 5: Performance

**Test Case 27:CPU Idle State**
1. Launch the app and let it idle in the background.

**Test Case 28: Normal Usage**
1. Perform common app actions like creating tasks, lists, mark as done

**Test Case 29: Heavy Load**
1. Perform resource-intensive tasks like uploading large files,  high-resolution videos

**Test Case 30: Memory Usage**
1. Perform various app actions and monitor memory usage over time.

## Performance Testing Report 

**Device Information**

**Device Model:** Samsung SM-A325F

**App Name:** AnyDo

**CPU Usage**

**App CPU Usage:** 0%

**Others CPU Usage:** 6%

**Threads:** 30

**Memory Usage**

**Total Memory:** 23.9 MB

**Java Heap:** 512 KB

**Native Heap:** 2.2 MB

**Graphics:** 728 KB

**Stack:** 196 KB

**Code:** 80 KB

**Others:** 20.2 MB

**Allocated Memory:** N/A

**Additional Information**

**Timestamp:** 04:31:51

**Date:** 11/13/2024

**Time:** 7:21 PM

**Analysis**

**CPU Usage:** The app's CPU usage is very low (0%). This indicates that the app is not resource-intensive and is running efficiently.

**Memory Usage:** The app's memory usage is relatively low (23.9 MB). However, the "Others" category accounts for a significant portion of the memory usage (20.2 MB). Further analysis is needed to identify the cause of this high "Others" usage.


------------------------------------------------------

# Medium Priority Scenarios

## Test Scenario 6: User profile handling

**Pre- Conditions:** 
1. Application Downloaded successfully
2. User Signed In


**Test Case ID: TC31 - Verify Hid Email when Signing with Apple** 

**Pre- Conditions:** 
1. Application Downloaded successfully
2. User Signed In with Apple 
3. Use chose to Hide the email while signing In
   
**Steps to Execute:**
1. Click on settings button on Top Right of the screen 
2. Choose Settings from the menu 
3. Choose Profile 

**Expected Results:**
1. Name is displayed 
2. Encrypted Email is displayed 

**Actual Results:** 
1. Name is displayed 
2. Encrypted Email is displayed
   
**Prioritization:** Medium

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC32 - Verify User can update his mail**

**Steps to Execute:** 
1. Get into account settings 
2. Click on edit icon beside email
3. Agree on change 
4. Enter email password 

**Expected Results:**
1. Email changes 
2. New email displayed on profile
   
**Actual Results:**
1. Email changed and displayed 

**Prioritization:** Medium

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC33 - Verify User Add profile photo**

**Steps to Execute:**
1. Get into account settings 
2. Get into Profile
3. User click on User Photo 
4. User choose to Take Photo / Choose from Library 
5. User choose Upload 

**Expected Results:** 
1. Image Displays in account profile
   
**Actual Results:**
1. Image displayed 

**Prioritization:** Medium

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC34 - Verify User can delete profile photo**

**Steps to Execute:**
1. Get into account settings 
2. Get into Profile
3. User click on User Photo 
4. User choose to Take Photo / Choose from Library 
5. User choose Upload 
6. User try to delete profile photo

**Expected Results:** 
1. User can delete photo
2. Photo not displayed anymore 

**Actual Results:**
1. User cannot delete image 

**Prioritization:** Medium

**Status:** Fail

------------------------------------------------------

**Test Case ID: TC35 - Verify User can Sign Out**

**Steps to Execute:**
1. Get into account settings 
2. Get into Profile
3. User click Sign out
4. User click Yes on Message Box 

**Expected Results:** 
1. User logs out 

**Actual Results:**
1. User logged out

**Prioritization:** Medium

**Status:** Pass

------------------------------------------------------

## Test Scenario 7: User account type handling

**Pre- Conditions**
1. User Open App
2. User Signed In

**Test Case ID: TC36 - Verifying Free plan user can upgrade to Premium**

**Steps to Execute:** 
1. User get into List/ Calendar view 
2. User click on 2 dots menu on top left of screen
3. User click settings
4. User click profile
5. User click on Upgrade to Premium
6. User select best plan from available 
7. Click Continue
8. User click Subscribe 
9. User Scan Face ID for Apple Payment (current saved payment method)

**Expected Results:**

1. Account Upgraded 
2. New features appear 

**Actual Results:** 
1. Account upgraded with new features

**Prioritization:** Medium

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC37- Verifying User can Manage Subscription** 

**Steps to Execute:** 
1. User get into List/ Calendar view 
2. User click on 2 dots menu on top left of screen
3. User click settings
4. User click profile
5. User click on Manage Subscription
6. User Plan listed (if found)
7. User choose to Cancel 
8. Click Continue
   
**Expected Results:**
1. Subscription Cancelled 
2. Actual Results: 
3. Subscription Cancelled

**Prioritization:** Medium

**Status:** Pass

------------------------------------------------------

## Test Scenario 8: Account Integration

**Pre- Conditions**
1. User Open App
2. User Signed In
3. User has WhatsApp or Slack

**Test Case ID: TC38 - Verifying Premium User can Integrate with WhatsApp**

**Steps to Execute:** 
1. User get into List/ Calendar view 
2. User click on 2 dots menu on top left of screen
3. User click settings
4. User click Integration
5. User Click WhatsApp

------------------------------------------------------

**Test Case ID: TC39 - Verify User can Integrate with Slack**

**Steps to Execute:**
1. User get into List/ Calendar view 
2. User click on 2 dots menu on top left of screen
3. User click settings
4. User click Integration
5. User Click Slack
6. User Sign In to Slack work space 
7. User click Continue
   
**Expected Results:** 
1. User Any.do and Slack accounts are integrated 
2. Slack Tasks get into Any.do
   
**Actual Results:** 
1. User Any.do and Slack accounts are integrated
   
**Prioritization:** Medium

**Status:** Pass

------------------------------------------------------

## Test Scenario 9: Notifications and Alerts

**Pre- Conditions**
1. User Open App
2. User Signed In

**Test Case ID: TC40 - Verify User can see Notifications** 

**Steps to Execute:** 
1. User get into List/ Calendar view 
2. User set Task or Meeting 
3. User wait for assigning time to see Notification 

**Expected Results:** 
1. Notification Displayed on Time

**Actual Results:** 
1. Notification Displayed on Time

**Prioritization:** Medium

**Status:** Pass

------------------------------------------------------

# Low Priority Scenarios

## Test Scenario 10: User Accessibility 

**Pre- Conditions**
1. User Open App
2. User Signed In


**Test Case ID: TC41 - Verify User can change Themes**

**Steps to Execute:** 
1. User get 3 dots settings menu 
2. User choose preferred themes from available 

**Expected Results:** 
1. App theme changes

**Actual Results:** 
1. App theme changed

**Prioritization:** Low

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC42 - Verify User can Language and Speech**

**Steps to Execute:** 
1. User get 3 dots settings menu 
2. User choose Language/Speech
3. User change preferred Language 

**Expected Results:** 
1. Language changes as selected 

**Actual Results:** 
1. Language changed as selected 

**Prioritization:** Low

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC43 - Verify User can On /Off sound**

**Steps to Execute:** 
1. User get 3 dots settings menu 
2. User choose Sounds
3. User choose ON or OF

**Expected Results:** 
1. Sounds are ON if this option is chosen
2. Sounds are OF if this option is chosen

**Actual Results:** 
1. Sounds ON for ON option
2. Sounds OF for OF option

**Prioritization:** Low

**Status:** Pass

------------------------------------------------------

## Test Scenario 11: User Usability 
**Pre- Conditions**
1. User Open App
2. User Signed In


**Test Case ID: TC44 - Verify User can change preferred Home Screen**

**Steps to Execute:** 
1. User get 3 dots settings menu  
2. User Click Preferred Home Screen 
3. User keep clicking until reaching preferred option 

**Expected Results:**
1. Home screen is as user preference 

**Actual Results:** 
1. Home screen is now as user preference 

**Prioritization:** Low

**Status:** Pass

------------------------------------------------------

**Test Case ID: TC45 - Verify User have Support option**

**Steps to Execute:** 
1. User get 3 dots settings menu  
2. User Click on Support
3. User choose FAQs, Report a Bug, Feature Request 

**Expected Results:** 
1. User get support
   
**Actual Results:** 
1. User got needed support 

**Prioritization:** Low

**Status:** Pass

