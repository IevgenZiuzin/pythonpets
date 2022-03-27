"""Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of ab"""

a, b = map(int, input('Type numbers using "SPACE" between them: ').split())
print('SUM: %.d\nDIFF: %.f\nPRODUCT: %.f\nQUOTIENT: %.f\nREMAINDER: %.f\nRATE: %.f' % \
    ((a + b), (max(a, b) - min(a, b)), (a * b), (a / b), (a % b), (a ** b)))