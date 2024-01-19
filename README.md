# Compression

## Current Status:
I haven't worked on this project in a while, I've been incredibly busy; however, I do plan to complete this project eventually.

## The Plan:

### Completed Tasks:
Completed hash table and compression and decompression.

### Current Task:
GUI!!!

### Future Tasks:
Possibly encryption (may ruin the purpose of compressing all those files)
Calling a computer vision API and/or a LLM like GPT 3-4 in order to automatically categorize files.

## Random Thoughts:
I don't want to get too ahead of myself but I want to write some of my thoughts about encryption down just to document my thought process. On one hand encryption is good, it protects one's data from bad actors. On the other hand if the user has sensitive data anyways, they should probably be encrypting it on their own, or storing it securely offsite.

Additionally, the extra space required to encrypt data may negate the storage gains from compressing one's data.

Perhaps it would be best to add encryption as a secondary feature for users in the GUI. I could use the AES dependency if I want to implement it.

I think I'd like the GUI to look like Google Drive, even if the actual file explorer on the user's computer looks completely different. I'll probably end up using a hashmap for the category system, which dynamically scales as the user adds additional categories. This would be a good way to ensure some optimization.

## Included Files:
main.py
readme.md

## Execution Instructions:
Will update when the program is functional, eventually I would like the GUI to be an executable.
