#Write a Python program that invoke square root function after specific milliseconds. 
import math
import time


number = int(input())
m_seconds = int(input())

seconds = m_seconds / 1000

time.sleep(seconds)
print(f"Square root of {number}  after {m_seconds}  miliseconds is {math.sqrt(number)}")