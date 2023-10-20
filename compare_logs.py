import re
from logs import *

def strip_timestamp_and_thread(line):
    # The regex matches a pattern like '[00.249](0) '
    return re.sub(r'\[\d+\.\d+\]\(\d+\) ', '', line)

def normalize_and_split(log):
    # Strip off the timestamp and thread number for each line
    log = '\n'.join(strip_timestamp_and_thread(line) for line in log.split('\n'))
    return sorted(log.strip().split('\n'))

def compare_logs(log1, log2):
    split_log1 = normalize_and_split(log1)
    split_log2 = normalize_and_split(log2)
    
    return split_log1 == split_log2

# Test Cardreader
print("Cardreader Tests")
print(compare_logs(cardreader_1_reference, cardreader_1_submission))
print(compare_logs(cardreader_2_reference, cardreader_2_submission))
print(compare_logs(cardreader_3_reference, cardreader_3_submission))
print()

# Test Door
print("Door Tests")
print(compare_logs(door_1_reference, door_1_submission))
print(compare_logs(door_2_reference, door_2_submission))
print()

# Test Callpoint
print("Callpoint Tests")
print(compare_logs(callpoint_1_reference, callpoint_1_submission))
print()

# Test Firealarm
print("Firealarm Tests")
# print(compare_logs(firealarm_1_reference, firealarm_1_submission))
print(compare_logs(firealarm_2_reference, firealarm_2_submission))
print(compare_logs(firealarm_3_reference, firealarm_3_submission))
print()