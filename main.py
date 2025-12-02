from fastapi import FastAPI

app = FastAPI()

# ---------------------------
#   Fake In-Memory "Database"
# ---------------------------

users_db = {
    "Jannat": {"pin": 1818, "bank_balance": 5000},
    "Ahmed": {"pin": 1222, "bank_balance": 3000},
    "Horia": {"pin": 3299, "bank_balance": 7000}
}

# ---------------------------
#    AUTHENTICATE ENDPOINT
# ---------------------------

@app.post("/authenticate")
def authenticate(name: str, pin_number: int):
    if name not in users_db:
        return {"message": "User not found"}

    if users_db[name]["pin"] != pin_number:
        return {"message": "Incorrect PIN"}

    return {
        "message": "Login successful",
        "name": name,
        "bank_balance": users_db[name]["bank_balance"]
    }


# ---------------------------
#         DEPOSIT
# ---------------------------

@app.post("/deposit")
def deposit(name: str, amount: int):
    if name not in users_db:
        return {"message": "User not found"}

    if amount <= 0:
        return {"message": "Invalid amount"}

    # update balance
    users_db[name]["bank_balance"] += amount

    return {
        "message": "Amount Deposited Successfully",
        "updated_balance": users_db[name]["bank_balance"]
    }


# ---------------------------
#       BANK TRANSFER
# ---------------------------

@app.post("/bank-transfer")
def bank_transfer(sender_name: str, receipents_name: str, amount: int):

    if sender_name not in users_db or receipents_name not in users_db:
        return {"message": "Sender or Recipient does not exist"}

    if amount <= 0:
        return {"message": "Invalid transfer amount"}

    if users_db[sender_name]["bank_balance"] < amount:
        return {"message": "Insufficient Balance"}

    # deduct sender balance
    users_db[sender_name]["bank_balance"] -= amount

    # add to receiver
    users_db[receipents_name]["bank_balance"] += amount

    return {
        "message": "Transfer Successful",
        "sender_new_balance": users_db[sender_name]["bank_balance"],
        "receiver_new_balance": users_db[receipents_name]["bank_balance"]
    }
