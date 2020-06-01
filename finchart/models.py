from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField("会社名", max_length=30, blank=False)

    def __str__(self):
        return str(self.name)

class Fstatement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    fiscal_year = models.DateField("決算日")
    bs_current_assets = models.IntegerField("流動資産（百万円）", default=0)
    bs_fixed_assets = models.IntegerField("固定資産（百万円）", default=0)
    bs_deferred_assets = models.IntegerField("繰延資産（百万円）", default=0)
    bs_current_liabilities = models.IntegerField("流動負債（百万円）", default=0)
    bs_fixed_liabilities = models.IntegerField("固定負債（百万円）", default=0)
    bs_net_assets = models.IntegerField("純資産（百万円）", default=0)
    pl_gross_sales = models.IntegerField("総売上（百万円）", default=0)
    pl_gross_profit = models.IntegerField("売上総利益（百万円）", default=0)
    pl_operating_profit = models.IntegerField("営業利益（百万円）", default=0)
    pl_ordinary_income = models.IntegerField("経常利益（百万円）", default=0)
    pl_income_before_tax = models.IntegerField("税引前当期純利益（百万円）", default=0)
    pl_net_income = models.IntegerField("当期純利益（百万円）", default=0)
    cf_operating = models.IntegerField("営業ＣＦ（百万円）", default=0)
    cf_investment = models.IntegerField("投資ＣＦ（百万円）", default=0)
    cf_finance = models.IntegerField("財務ＣＦ（百万円）", default=0)

    def __str__(self):
        return str(self.company) + '決算日：【 ' + str(self.fiscal_year) + '】'