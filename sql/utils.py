from run import username

def pwd():
    while True:
        # -------------choose a password-----------------------------
        password = str(getpass('Choose a password: '))
        password1 = str(getpass('Please confirm password: '))
        # -------------check if both entries match-----------------------
        if password == password1:
            # -------------match-----------------------------
            # --------------send all entries to db---------------------
            with sqlite3.connect('db/db.sqlite') as db:
                cursor0 = db.cursor()
                cursor0.execute(
                    "UPDATE Users SET Username = ?", username)
                var_insert.pop(0)
                var_insert.insert(0, password1)
                cursor0.execute(
                    "UPDATE Users SET Password = ?  WHERE Username = ? ", username)
                db.commit()
                cursor0.close()
                time.sleep(2)
                break
        else:
            # -------------no match-----------------------
            print('Passwords does not match')
