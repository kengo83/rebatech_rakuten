from django.db import models

# Create your models here.

sort_methods = (('standard','楽天標準ソート順'),('+affiliateRate','アフィリエイト料率順(昇順)'),('-affiliateRate','アフィリエイト料率順(降順)'),('+reviewCount','レビュー件数順(昇順)'),('-reviewCount','レビュー件数順(降順)'),('+itemPrice','価格順(昇順)'),('-itemPrice','価格順(降順)'),('+reviewAverage','レビュー平均順(昇順)'),('-reviewAverage','レビュー平均順(降順)'),('+updateTimestamp','商品更新日時順(昇順)'),('-updateTimestamp','商品更新日時順(降順)'))

class SearchModel(models.Model):
    keyword = models.CharField(max_length=100)
    ng_keyword = models.CharField(max_length=100,blank=True,null=True)
    sort = models.CharField(
        max_length=30,
        choices = sort_methods
    )
    file = models.CharField(max_length=30)
    folda = models.CharField(max_length=30)
