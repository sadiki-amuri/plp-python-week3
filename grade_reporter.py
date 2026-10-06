
scores = [72, 45, 90, 61, 38]

passed_count = 0
failed_count = 0
total_score = 0

for score in scores:

    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
        print(f"Score: {score} -> Grade: {grade}")
    
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1
        

    total_score += score

average_score = round(total_score / len(scores), 1)

print(f"Learners Passed: {passed_count}")
print(f"Learners Failed: {failed_count}")
print(f"Average Score: {average_score}")

