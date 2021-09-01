from django.db import models

# Create your models here.

class Lession(models.Model):
    Name=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Name}'


class LessionScore(models.Model):
    Lession= models.ForeignKey(to=Lession,on_delete=models.PROTECT)
    Score=models.IntegerField()

    def __str__(self):
        return f'{self.Lession.Name} - {self.Name}'

    def avrage(self):
        text=''

        for lession in Lession.objects.all():
            avg=0
            sum=0
            counter=0
            for scorelession in LessionScore.objects.all():
                if scorelession.Lession.id==lession.id :
                    sum+=scorelession.Score
                    counter+=1
            if counter!=0:
                avg=sum/counter

            text+= str(avg)+','

        return text
