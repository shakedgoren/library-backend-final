from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publishedYear = models.CharField(max_length=50)
    bookType = models.IntegerField()
    bookStatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.bookName},{self.bookStatus}"

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    clientName = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    clientStatus = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.clientName},{self.clientStatus}"
    
class Loan(models.Model):
    bookID =models.ForeignKey(Book,on_delete=models.SET_NULL,null=True)
    clientID =models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    id = models.AutoField(primary_key=True)
    startDate = models.DateField()
    endDate = models.DateField()
    loanStatus = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id},{self.bookID},{self.clientID},{self.loanStatus}"