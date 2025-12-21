from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Proposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer_name = models.CharField(max_length=100)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.freelancer_name


class Contract(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer_name = models.CharField(max_length=100)
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.freelancer_name
