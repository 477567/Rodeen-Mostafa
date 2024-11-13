**This project involved comprehensive testing of the Any.do application. 
Manual testing was conducted to ensure functional and non-functional correctness including Functions,Usability, Accessibility and adherence to design specifications. 
Performance testing applied, utilizing Android Studio's.**


**High Priority Scenarios** 

**Test Scenario 1: User Authentication**

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

Test Case ID: TC3 - Verify User can Sign Up with Mail 
Steps to Execute:
Open App
Click on Mail Box logo button 
Enter your preferred mail 
Then click the right arrow after mail validation 
Enter Full Name  
Create Password 
Click Create Account 
Expected Results:
Sign In successful 
Landing on Intro page 
Actual Results: 
Signed In successful 
Landed on Intro page 
Prioritization: High 
Status: Pass



Test Case ID: TC4 - Verify User can Sign In with Facebook 
Steps to Execute: 
Open App 
Click on Facebook logo button 
Agree to use Facebook for Sign In by clicking Continue 
Enter valid credentials for Facebook Sign In, then Log In OR you can Sign In with you Saved Passwords 
Verifying that you’re a human by entering the Captcha 
Agree to requesting access for Facebook data, click Continue 
Expected Results:
Sign In successful 
Landing on Intro page 
Actual Results: 
Signed In successful 
Landed on Intro page 
Prioritization: High 
Status: Pass 



Test Scenario 2: List Management 
Pre - Conditions:
User Signed In 
User chose List view 
User has minimum one List contains minimum one task 


Test Case ID: TC - User can create a New List 
Steps to Execute:
Get into the Home Page 
Click on Plus button in My Lists 
Add name for new List 
Expected Results: 
New list created
List displayed in My Lists 
Actual Results: 
New list created
List displayed in My Lists 
Prioritization: High
Status: Pass

Test Case ID: TC - Verifying User can Edit existing List 
Steps to Execute:
Enter the preferred List 
Click on Plus button on the right side of the screen
Write the task 
Choose any valid assigning date in the future
Click on the Upload/ Up button for task save
Expected Results:
Task Saved 
Task in now displayed in the assigned day 
Actual Results: 
Task Saved 
Task in now displayed in the assigned day 
Prioritization: High
Status: Pass

Test Case ID: TC - Verify User can Sort a List 
Steps to Execute:
User get into the List 
Click on the settings button on the upper right side for the screen 
Choose Sort option 
Choose either to Sort by Time or List 
Expected Results:
Tasks are sorted depending on Date and Time 
Actual Results: 
Tasks already sorted
Prioritization: High 
Status: Pass


Test Case ID: TC - Verify User can Filter a List 
Steps to Execute:
User get into the List 
Click on the settings button on the upper right side for the screen 
Choose Filter option 
Choose preferred Tag from Filtration
Click Apply  
Expected Results:
Filtered Tasks with chose Tag only is displayed 
No Tasks appear, if the chose task has no assigned Task 
Actual Results: 
Filter Tasks only appear 
Nothing appear if no Tasks assigned to filtered Tag
Prioritization: High 
Status: Pass


Test Case ID: TC - Verify User can delete a List 
Steps to Execute:
User get into the List 
Click on the settings button on the upper right side for the screen 
Choose Delete option 
Agree to deletion by clicking Delete 
Expected Results:
User got out of the List 
List is no more displayed in My Lists
Actual Results: 
User got out of the List 
List is no more displayed in My Lists
Prioritization: High 
Status: Pass




Test Scenario 3: Task Management
Pre - Conditions:
User Signed In 
User chose List view 
User has minimum one List contains minimum one task 




Test Case ID: TC - Verify that a user can mark a task as complete
Steps to Execute:
Get into the preferred List 
Click on the check box beside the task
      Either 
Click on the Task
Click on the Mark as complete button 
Expected Results:
Task is marked as completed 
Actual Results: 
Task is marked as completed 
Prioritization: Medium
Status:Pass


Test Case ID: TC - Verify that a user can unmark a completed task
Steps to Execute:
Get into the preferred List 
Click on the checkbox beside the task
Uncheck the checkbox 
Expected Results:
Task re-assigned 
Actual Results: 
Task re-assigned 
Prioritization: Medium 
Status: Pass


Test Case ID: TC - Verify User can change assigned Task to another List 
Pre- Conditions: 
User Signed In 
User chose List view 
User has minimum two Lists one of them contains minimum one task 
Steps to Execute:
Get into the preferred List containing task 
Click on the Task 
Click on the List name displayed 
Choose preferred list to re-assign task to 
Click Save
Expected Results:
Task removed from the List 
Task is found in the new List 
Actual Results: 
Task removed from the List 
Task is found in the new List 
Prioritization: Medium
Status: Pass


Test Case ID: TC - Verifying Free Plan user can add specific Tags to Tasks 
Steps to Execute:
Get into the preferred List 
Click on the Task
Click on Add Tags
Choose Priority Tag 
Click Save 
Expected Results:
Tag displayed with the Task 
Actual Results: 
Tag displayed with the Task 
Prioritization: Medium 
Status: Pass


Test Case ID: TC - Verifying User can Add Subtasks or Notes
Steps to Execute:
Get into the preferred List 
Click on the Task
Write in Subtasks & Notes as much as you need 
Expected Results:
Subtasks showed as branches with the Parent Task
Notes are Saved & shown when entering the Task
Actual Results: 
Subtasks showed as branches with the Parent Task
Notes are Saved & shown when entering the Task
Prioritization: High
Status: Pass


Test Case ID: TC - Verify User can attach Image to a Task in List from Camera
Steps to Execute:
User get into the List 
Click on Plus button at the bottom of the screen 
Choose Camera 
Take Picture 
Click Use Photo 
Expected Results:
Image attached in attachments section at the screen bottom 
Actual Results: 
Image attached in attachments section at the screen bottom
Prioritization: High 
Status: Pass


Test Case ID: TC - Verify User can attach Video to a List from Camera
Steps to Execute:
User get into the List 
Click on Plus button at the bottom of the screen 
Choose Camera 
Take Video 
Stop Video 
Click Use Video 
Expected Results:
Video attached in attachments section at the screen bottom 
Actual Results: 
Video attached in attachments section at the screen bottom 
Prioritization: High 
Status: Pass


Test Case ID: TC - Verify User can attach Image to a List from Gallery
Steps to Execute:
User get into the List 
Click on Plus button at the bottom of the screen 
Choose Gallery
Choose image 
Expected Results:
Image attached in attachments section at the bottom of the screen 
Actual Results: 
Image attached in attachments section at the screen bottom 
Prioritization: High 
Status: Pass


Test Case ID: TC - Verify User can attach Video to a Task in a List from Gallery
Steps to Execute:
User get into the List 
Click on Plus button at the bottom of the screen 
Choose Gallery  
Select any Video 
Click Choose 
Expected Results:
Video attached in attachments section at the screen button 
Actual Results: 
Apps lags
Choose/ Cancel buttons get unclickable
Video is not uploaded  
No error messages 
Prioritization: High 
Status: Fail


Test Case ID: TC - Verifying User Attach File to Task in a List 
Steps to Execute:
User Open App
User get into List containing at least one Task 
User click on task
User click on Plus icon at the right bottom of the screen 
Choose Attachment 
Choose preferred file 
Expected Results:
File attached to Task
File displayed in Task Attachments 
Actual Results: 
File not attached
No any error messages 
Prioritization: High
Status: Fail

Test Case ID: TC - Verifying User attach Voice Note to a Task in a List 
Steps to Execute:
User Open App
User get into List containing at least one Task 
User click on task
User click on Plus icon at the right bottom of the screen 
Choose Voice note
User Press to Record
User toggle on right icon  
Expected Results:
Voice Note attached to Task
Actual Results: 
Voice Note successfully attached
Prioritization: High
Status: Pass



Test Case ID: TC - Verifying User cannot save task in the past 
Steps to Execute:
Enter the preferred List 
Click on Plus button on the right side of the screen
Write the task 
Click on Custom date
Choose date in the past 
Expected Results:
Task should not be saved as type of validation 
Actual Results: 
Task is not saved 
Prioritization: High 
Status: Pass


Test Case ID: TC - Verifying Free Plan user cannot all Tags to Tasks 
Steps to Execute:
Get into the preferred List 
Click on the Task
Click on Add Tags
Choose any Tag rather than Priority Tag 
Click Save 
Expected Results:
Premium Tags are not clickable 
Nothing Change after Save 
Actual Results: 
Premium Tags are not clickable 
Nothing Change after Save 
Prioritization: High
Status: Pass


Test Case ID: TC - Verify User can delete Task from a List 
Steps to Execute: 
Get into the preferred List 
Click on the Task
Click on settings icon on the upper left 
Choose to Archive Task 
Click Delete Task 
Expected Result:
Task deleted 
Task no more displayed in the List 
Actual Results:
Task Deleted 

Prioritization: High
Status: Pass

Test Scenario 4: Calendar Management 
Pre- Conditions:
User Signed In
User choose Calendar view


Test Case ID: TC - Verifying User can add event in calendar view
Steps to Execute:
Get into the calendar from bottom menu
Create Event
Name Event 
Set start date
Set end date
Click Confirm
Click on Up icon/button
Click on Add event on displayed screen 
Expected Results:
Event created
Event displayed in Calendar
Actual Results: 
Event created & displayed 
Prioritization: High
Status: Pass

Test Case ID: TC - Verify User can edit event on Calendar
Steps to Execute:
Get into the calendar from bottom menu
Click on any event or create one
Click Edit on the upper right
Change what is needed 
Click Done on Upper right
Expected Results:
New event change dispalyed 
Actual Results:
Changes dispalyed 
Prioritization: High
Status: Pass


Test Case ID: TC - Verifying user can change Calendar View 
Steps to Execute: 
Get into Calendar View 
Click on menu on top left of the screen 
Choose preferred view 
Expected Results: 
View change depending on choice
Actual Results:
View changed
Prioritization: High
Status: Pass


Test Scenario 5: Performance
Test Case 1: CPU Idle State
Launch the app and let it idle in the background.

Test Case 2: Normal Usage


Perform common app actions like creating tasks, lists, mark as done

Test Case 3: Heavy Load


Perform resource-intensive tasks like uploading large files,  high-resolution videos

Test Case 4: Memory Usage at Initial Launch
Launch the app for the first time 
Test Case 5: Memory Normal Usage


Perform various app actions and monitor memory usage over time.

Performance Testing Report 

Device Information:
Device Model: Samsung SM-A325F
App Name: AnyDo
Performance Metrics:
CPU Usage:
App CPU Usage: 0%
Others CPU Usage: 6%
Threads: 30
Memory Usage:
Total Memory: 23.9 MB
Java Heap: 512 KB
Native Heap: 2.2 MB
Graphics: 728 KB
Stack: 196 KB
Code: 80 KB
Others: 20.2 MB
Allocated Memory: N/A
Additional Information:
Timestamp: 04:31:51
Date: 11/13/2024
Time: 7:21 PM
Analysis: 
CPU Usage: The app's CPU usage is very low (0%). This indicates that the app is not resource-intensive and is running efficiently.
Memory Usage: The app's memory usage is relatively low (23.9 MB). However, the "Others" category accounts for a significant portion of the memory usage (20.2 MB). Further analysis is needed to identify the cause of this high "Others" usage.




Medium Priority Scenarios 
Test Scenario 6: User profile handling 
Test Case ID: TC - Verify Hid Email when Signing with Apple 
Test Scenario: 
Pre- Conditions: 
Application Downloaded successfully
User Signed In with Apple 
Use chose to Hide the email while signing In 
Steps to Execute:
Click on settings button on Top Right of the screen 
Choose Settings from the menu 
Choose Profile 
Expected Results:
Name is displayed 
Encrypted Email is displayed 
Actual Results: 
Name is displayed 
Encrypted Email is displayed 
Prioritization: Medium
Status: Pass

Test Case ID: TC - Verify User can update his mail
Steps to Execute: 
Get into account settings 
Click on edit icon beside email
Agree on change 
Enter email password 
Expected Results:
Email changes 
New email displayed on profile 
Actual Results:
Email changed and displayed 
Prioritization: Medium
Status: Pass

Test Case ID: TC - Verify User Add profile photo
Steps to Execute:
Get into account settings 
Get into Profile
User click on User Photo 
User choose to Take Photo / Choose from Library 
User choose Upload 
Expected Results: 
Image Displays in account profile
Actual Results:
Image displayed 
Prioritization: Medium
Status: Pass


Test Case ID: TC - Verify User can delete profile photo
Steps to Execute:
Get into account settings 
Get into Profile
User click on User Photo 
User choose to Take Photo / Choose from Library 
User choose Upload 
User try to delete profile photo
Expected Results: 
User can delete photo
Photo not displayed anymore 
Actual Results:
User cannot delete image 
Prioritization: Medium
Status: Fail


Test Case ID: TC - Verify User can Sign Out 
Steps to Execute:
Get into account settings 
Get into Profile
User click Sign out
User click Yes on Message Box 
Expected Results: 
User logs out 
Actual Results:
User logged out
Prioritization: Medium
Status: Pass


Test Scenario 7: User account type handling
Pre- Conditions
User Open App
User Signed In

Test Case ID: TC - Verifying Free plan user can upgrade to Premium
Steps to Execute: 
User get into List/ Calendar view 
User click on 2 dots menu on top left of screen
User click settings
User click profile
User click on Upgrade to Premium
User select best plan from available 
Click Continue
User click Subscribe 
User Scan Face ID for Apple Payment (current saved payment method)
Expected Results:
Account Upgraded 
New features appear 
Actual Results: 
Account upgraded with new features
Prioritization: Medium
Status: Pass


Test Case ID: TC1- Verifying User can Manage Subscription 
Steps to Execute: 
User get into List/ Calendar view 
User click on 2 dots menu on top left of screen
User click settings
User click profile
User click on Manage Subscription
User Plan listed (if found)
User choose to Cancel 
Click Continue
Expected Results:
Subscription Cancelled 
Actual Results: 
Subscription Cancelled
Prioritization: Medium
Status: Pass


Test Scenario 8: Account Integration 
Pre- Conditions
User Open App
User Signed In
User has WhatsApp or Slack


Test Case ID: TC - Verifying Premium User can Integrate with WhatsApp
Steps to Execute: 
User get into List/ Calendar view 
User click on 2 dots menu on top left of screen
User click settings
User click Integration
User Click WhatsApp


Test Case ID: TC - Verify User can Integrate with Slack 
Steps to Execute: 
User get into List/ Calendar view 
User click on 2 dots menu on top left of screen
User click settings
User click Integration
User Click Slack
User Sign In to Slack work space 
User click Continue 
Expected Results: 
User Any.do and Slack accounts are integrated 
Slack Tasks get into Any.do
Actual Results: 
User Any.do and Slack accounts are integrated
Prioritization: Medium
Status: Pass



Test Scenario 9: Notifications and Alerts

Test Case ID: TC - Verify User can see Notifications 
Pre- Conditions
User Open App
User Signed In

Steps to Execute: 
User get into List/ Calendar view 
User set Task or Meeting 
User wait for assigning time to see Notification 

Expected Results: 
Notification Displayed on Time
Actual Results: 
Notification Displayed on Time
Prioritization: Medium
Status: Pass

Low Priority Scenarios 
Test Scenario 10: User Accessibility 
Pre- Conditions
User Open App
User Signed In


Test Case ID: TC - Verify User can change Themes
Steps to Execute: 
User get 3 dots settings menu 
User choose preferred themes from available 

Expected Results: 
App theme changes
Actual Results: 
App theme changed
Prioritization: Low
Status: Pass



Test Case ID: TC - Verify User can Language and Speech
Steps to Execute: 
User get 3 dots settings menu 
User choose Language/Speech
User change preferred Language 
Expected Results: 
Language changes as selected 
Actual Results: 
Language changed as selected 
Prioritization: Low
Status: Pass



Test Case ID: TC - Verify User can On /Off sound
Steps to Execute: 
User get 3 dots settings menu 
User choose Sounds
User choose ON or OF

Expected Results: 
Sounds are ON if this option is chosen
Sounds are OF if this option is chosen
Actual Results: 
Sounds ON for ON option
Sounds OF for OF option
Prioritization: Low
Status: Pass
Test Scenario 11: User Usability 
Pre- Conditions
User Open App
User Signed In


Test Case ID: TC - Verify User can change preferred Home Screen
Steps to Execute: 
User get 3 dots settings menu  
User Click Preferred Home Screen 
User keep clicking until reaching preferred option 
Expected Results: 
Home screen is as user preference 
Actual Results: 
Home screen is now as user preference 
Prioritization: Low
Status: Pass



Test Case ID: TC - Verify User have Support option
Steps to Execute: 
User get 3 dots settings menu  
User Click on Support
User choose FAQs, Report a Bug, Feature Request 

Expected Results: 
User get support 
Actual Results: 
User got needed support 
Prioritization: Low
Status: Pass

