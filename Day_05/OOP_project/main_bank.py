from bank_account import * #using * to import all 

Long = Bank_account(1000, "Long")
Meo = Bank_account(1000, "Meo")
Long.deposit(34.5)

Long.withdraw(5000)

Long.transfer(1500, Meo)

Halo = SavingAccount(1000, "Halo")
Halo.withdraw(500)

Halo.transfer(200,Long)