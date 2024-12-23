from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Participation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE) 
    role = models.CharField(max_length=100)
    hours_worked = models.PositiveIntegerField()
    date_assigned = models.DateField()

    def __str__(self):
        return f"{self.employee.name} working on {self.project.name} as {self.role}"



class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Employee, related_name="teams")

    def __str__(self):
        return self.name

