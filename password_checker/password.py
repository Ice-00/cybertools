def password_strength_checker(password):
    score = 0
    feedback = []

    #rule 1: Check lenght
    if len(password) >= 8:
        score +=1
    else:
        feedback.append("Make it at least 8 Characters long")

    #Rule 2: Check for a number
    has_number = any(char.isdigit() for char in password)
    if has_number:
        score += 1
    else:
        feedback.append("Add at least one number.")

    #Rule 3: Check for an uppercase letter
    has_upper = any(char.isupper() for char in password)
    if has_upper:
        score += 1
    else:
        feedback.append("add at least one capital letter. ")
    return score, feedback


user_password = input("Enter a password to test:")

#Run the password through our checekr function
final_score, suggestions = password_strength_checker(user_password)

#print the results based on the score
print("\n--- RESULTS ---")

if final_score == 3:
    print("STRENGHT: STRONG")

elif final_score == 2:
    print("STRENGHT: MEDIUM")

else:
    print("STRENGHT: WEAK")

# If there are fixes needed, print them out 
if suggestions:
    print("\nSUggestions to improve:")
    for tip in suggestions:
        print(f"_{tip}")


