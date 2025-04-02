import hashlib
import sys
import time

target_hash = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"

def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit = "0123456789"
special = "!@#$"
lower = "abcdefghijklmnopqrstuvwxyz"

target_counts = {"upper": 1, "digit": 1, "special": 1, "lower": 3}
max_len = 6

recursive_calls = 0
found = False
start_time = time.time()

def char_type(ch):
    if ch in upper:
        return "upper"
    elif ch in digit:
        return "digit"
    elif ch in special:
        return "special"
    elif ch in lower:
        return "lower"
    return None

def backtrack(current, count_upper, count_digit, count_special, count_lower):
    global recursive_calls, found, start_time
    recursive_calls += 1

    if recursive_calls % 1000000 == 0:
        elapsed = time.time() - start_time
        print(f"Candidate generate: {recursive_calls}, timp scurs: {elapsed:.2f} secunde")

    if found:
        return

    if len(current) == max_len:
        if (count_upper == target_counts["upper"] and 
            count_digit == target_counts["digit"] and 
            count_special == target_counts["special"] and 
            count_lower == target_counts["lower"]):
            candidate_hash = get_hash(current)
            if candidate_hash == target_hash:
                print("Parola găsită:", current)
                print("Număr apeluri recursive:", recursive_calls)
                found = True
                sys.exit(0)
        return

    remaining_positions = max_len - len(current)
    remaining_upper = target_counts["upper"] - count_upper
    remaining_digit = target_counts["digit"] - count_digit
    remaining_special = target_counts["special"] - count_special
    remaining_lower = target_counts["lower"] - count_lower
    if (remaining_upper + remaining_digit + remaining_special + remaining_lower) > remaining_positions:
        return

    for ch in (upper + digit + special + lower):
        typ = char_type(ch)
        new_upper = count_upper + (1 if typ == "upper" else 0)
        new_digit = count_digit + (1 if typ == "digit" else 0)
        new_special = count_special + (1 if typ == "special" else 0)
        new_lower = count_lower + (1 if typ == "lower" else 0)
        if (new_upper > target_counts["upper"] or 
            new_digit > target_counts["digit"] or 
            new_special > target_counts["special"] or 
            new_lower > target_counts["lower"]):
            continue
        backtrack(current + ch, new_upper, new_digit, new_special, new_lower)
        if found:
            return

backtrack("", 0, 0, 0, 0)
print("Nu s-a găsit nicio parolă care să corespundă condițiilor.")
