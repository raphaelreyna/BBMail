# BBMail
## A BlackBoard interface via email.

Using BlackBoard can be a pain, both through their website and through their official app.
This is a project that aims to act as a way to be able to use blackboard through email.

### How it works

BBMail works by keeping an eye on an email account, acting only on emails it receives from you.
When you email BBMail with a subject "(COURSE ID) SUBJECT" it creates an announcement in the course corresponding to COURSE ID. The announcement will have the subject SUBJECT and the body of the email will be used as the body of the announcement. BBMail does not use BlackBoards official API, instead, it automatically interacts with the Blackboard website directly using a headless browser.

Because BBMail does not use BlackBoards official API, it must be updated to handle changes to Blackboard's website.
