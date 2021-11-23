import time
from sys import exit
# tell horoscope based on date of birth
print("Input Format Example: 1 22 (January 22)");
time.sleep(2)

x = input("Birthday Month (numerical value, ex: 1 (Jan)): ")
s = int(x)
if s > 12 or s < 1:
    print("Please try again and enter a valid month.")
    exit(0)
y = input("Day of Birth: ")
p = int(y)

if p > 31 or p < 1:
    print("Please try again and enter a valid calendar date.")
    exit(0)

n = input("What is your name/nickname? : ")
print("Scanning the universe now. . . .")
time.sleep(4)

# change cancer and everything after it
# AQUARIUS
if s == 1 and p >= 20 and p <= 31 or s == 2 and p >= 1 and p <= 18:
    print(f"Your results are in, {n}. You are a aquarius!")
# ARIES
if s == 3 and p >= 21 and p <= 31 or s == 4 and p >= 1 and p <= 19:
    print(f"Your results are in, {n}. You are a aries!")
# CAPRICORN
if s == 1 and p >= 1 and p <= 19 or s == 12 and p >= 22 and p <= 31:
    print(f"Your results are in, {n}. You are a capricorn!")
# CANCER
if s == 6 and p >= 21 and p <= 30 or s == 7 and p >= 1 and p <= 22:
    print(f"Your results are in, {n}. You are a cancer!")
# GEMINI
if s == 5 and p >= 21 and p <= 31 or s == 6 and p >= 1 and p <= 20:
    print(f"Your results are in, {n}. You are a gemini!")
# LIBRA
if s == 9 and p >= 23 and p <= 30 or s == 10 and p >= 1 and p <= 22:
    print(f"Your results are in, {n}. You are a libra!")
# LEO
if s == 7 and p >= 22 and p <= 31 or s == 8 and p >= 1 and p <= 22:
    print(f"Your results are in, {n}. You are a leo!")
# TAURUS
if s == 4 and p >= 20 and p <= 30 or s == 5 and p >= 1 and p <= 20:
    print(f"Your results are in, {n}. You are a taurus!")
# VIRGO
if s == 8 and p >= 23 and p <= 31 or s == 9 and p >= 1 and p <= 22:
    print(f"Your results are in, {n}. You are a virgo!")
# SCORPIO
if s == 10 and p >= 23 and p <= 31 or s == 11 and p >= 1 and p <= 21:
    print(f"Your results are in, {n}. You are a scorpio!")
# SAGITTARIUS
if s == 11 and p >= 22 and p <= 30 or s == 12 and p >= 1 and p <= 21:
    print(f"Your results are in, {n}. You are a sagittarius!")
# PISCES
if s == 2 and p >= 19 and p <= 29 or s == 3 and p >= 1 and p <= 20:
    print(f"Your results are in, {n}. You are a pisces!")

