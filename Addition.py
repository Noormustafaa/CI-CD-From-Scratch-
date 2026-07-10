# 1. Aik function banaya jo do numbers ko add karke value RETURN karta hai
def add_numbers(a, b):
    return a + b

# 2. AUTOMATED TEST: Hum khud check kar rahe hain ke kya hamara function sahi kaam kar raha hai?
expected_answer = 10
actual_answer = add_numbers(7, 3) # 7 + 3 ideally 10 hona chahiye

print(f"Testing started...")
print(f"Expected: {expected_answer}, Got: {actual_answer}")

# Agar answer sahi nahi aaya, toh program error de kar ruk jayega
if actual_answer == expected_answer:
    print("SUCCESS: Addition function bilkul sahi kaam kar raha hai! 🎉")
else:
    # Yeh line program mein jaan bator error paida karegi agar calculation galat hui
    raise ValueError("FAILED: Addition function mein koi galti hai! ❌")