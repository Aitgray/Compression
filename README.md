# Compression

## The Plan:

### Completed Tasks:
N/A (I just started)

### Current Task:
Getting main.py ready, starting to implement some of the compression/decompression methods.

### Future Tasks:
GUI - will provide more details in the future.
Possibly encryption (may ruin the purpose of compressing all those files)
Calling a computer vision API and/or a LLM like GPT 3-4 in order to automatically categorize files.

## Random Thoughts:
I don't want to get too ahead of myself but I want to write some of my thoughts about encryption down just to document my thought process. On one hand encryption is good, it protects one's data from bad actors. On the other hand if the user has sensitive data anyways, they should probably be encrypting it on their own, or storing it securely offsite.

Additionally, the extra space required to encrypt data may negate the storage gains from compressing one's data.

Perhaps it would be best to add encryption as a secondary feature for users in the GUI. I could use the AES dependency if I want to implement it.

I think I'd like the GUI to look like Google Drive, even if the actual file explorer on the user's computer looks completely different. I'll probably end up using a hashmap for the category system, which dynamically scales as the user adds additional categories. This would be a good way to ensure some optimization.

## Included Files:
main.py

readme.md (duh)

## Execution Instructions:
Will update when the program is functional, eventually I would like the GUI to be an executable.
The Rust backend should work without needing to be called.
