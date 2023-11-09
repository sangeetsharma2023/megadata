from django.db import models

class AccountHeads(models.Model):
    ACCT_TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Bank Account', 'Bank Account'),
        ('Debt', 'Debt'),
        ('Advance', 'Advance'),
        ('Cards', 'Cards'),
        ('Wallet', 'Wallet'),
    ]

    ACCT_CATEGORY_CHOICES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]

    acctname = models.CharField(max_length=50)
    accttype = models.CharField(max_length=50, choices=ACCT_TYPE_CHOICES)
    acctcategory = models.CharField(max_length=50, choices=ACCT_CATEGORY_CHOICES)
    acctdescription = models.TextField(blank=True, null=True)
    openingbal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.acctname

class IncomeCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name
    
class ExpenseCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name

class ExpenseSubCategory(models.Model):
    subcategory_name = models.CharField(max_length=50)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.subcategory_name} : {self.category}"
    
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Transaction(models.Model):
    TRAN_TYPE_CHOICES = [
        ('NRML', 'Normal'),
        ('Transfer', 'Transfer'),
    ]

    TRAN_CATEGORY_CHOICES = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
        ('Investment', 'Investment'),
        ('Investment Liquidate', 'Investment Liquidate'),
        ('Debt', 'Debt'),
        ('Advance', 'Advance'),
        ('Adjustment', 'Adjustment'),
    ]

    datetime = models.DateTimeField()
    debit_acct = models.ForeignKey(AccountHeads, on_delete=models.CASCADE, related_name='debit_transactions')
    credit_acct = models.ForeignKey(AccountHeads, on_delete=models.CASCADE, related_name='credit_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    trantype = models.CharField(max_length=15, choices=TRAN_TYPE_CHOICES)
    trantcategory = models.CharField(max_length=20, choices=TRAN_CATEGORY_CHOICES)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, blank=True, null=True)
    expense_subcategory = models.ForeignKey(ExpenseSubCategory, on_delete=models.SET_NULL, blank=True, null=True)
    persona = models.ForeignKey(Person, on_delete=models.SET_NULL, blank=True, null=True)
    particular = models.TextField(blank=True, null=True)

    def __str__(self):
        # Format the datetime to display only the date
        formatted_date = self.datetime.strftime('%Y-%m-%d')
        return f"Transaction on {formatted_date} - {self.debit_acct.acctname} to {self.credit_acct.acctname}: {self.amount}"


class ItemTag(models.Model):
    ITEM_UNIT_CHOICES = [
        ('Kg', 'Kilogram'),
        ('Ltr', 'Liter'),
        ('Pcs', 'Piece'),
    ]

    itemname = models.CharField(max_length=100)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    unit = models.CharField(max_length=5, choices=ITEM_UNIT_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    remark = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.itemname