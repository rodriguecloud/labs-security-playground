from flask import Flask, request
import time

# Simulated database
balance = 100 

app = Flask(__name__)

@app.route('/withdraw', methods=['POST'])
def withdraw():
    global balance
    amount = int(request.form.get('amount'))

    # VULNERABILITY: Check-then-Act Race Condition
    # 1. CHECK
    if balance >= amount:
        # Simulate a slight delay (network latency or DB load)
        time.sleep(1) 
        
        # 2. ACT
        balance -= amount
        return f"Withdrawal successful! Remaining: {balance}"
    
    return "Insufficient funds!"
