import conducto as co

def happy() -> co.Serial:
    with co.Serial() as node:
        co.Exec(":", name="happy")
    return node

def sad() -> co.Serial:
    with co.Serial() as node:
        co.Exec("false", name="sad")
    return node

if __name__ == "__main__":
    co.main(default=happy)

