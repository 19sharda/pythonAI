# Write a function called analyze_scores(scores) that:
#
# Loops through the list of scores.
#
# Uses conditionals to:
#
# Ignore invalid scores (less than 0 or greater than 100).
#
# Classify each valid score:
#
# >= 85 → "Distinction"
#
# 60–84 → "Pass"
#
# < 60 → "Fail"
#
# Counts how many students fall into each category.
#
# Calculates the average score of only valid marks.
#
# Uses:
#
# continue when skipping invalid data
#
# break if you encounter a score of exactly 0 (exam cancelled scenario)
#
# Returns (not prints) a dictionary like:
# {
#   "average": 66.2,
#   "distinction": 3,
#   "pass": 2,
#   "fail": 3
# }


def analyze_scores(scores):
    a=0
    d=0
    p=0
    f=0
    t=0
    topper=0
    failed_percentage=0
    count=0
    for i in scores:

        if i==0:
            break
        elif i>100 or i<0:
            continue
        if i>topper:
            topper=i
            count+=1
        elif i>=85:
            d+=1
            count += 1
        elif (i>=60) and (i<=84):
            p+=1
            count += 1
        else:
            f+=1




        t += i
    failed_percentage = f / count
    print(count)
    print(t)
    return {"Failed Percentage":failed_percentage,"Topper":topper,"Average":t/count,"Distinction":d,"Pass":p,"Fail":f}


scores = [45, 78, 88, 32, 90, 67, 55, 40, 99]
print(analyze_scores(scores))