from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title


class HomeAnouncement(models.Model):
    id = models.BigAutoField(primary_key=True)
    text_input = models.CharField(max_length=200)
    date_input = models.DateField()

    class Meta:
        db_table = "home_anouncement"


class StudentMaster(models.Model):
    rank = models.IntegerField(db_column="rank", blank=True, null=True)
    roll_no = models.OneToOneField(
        "StudentScores", models.DO_NOTHING, db_column="roll_no", primary_key=True
    )
    name = models.CharField(db_column="name", max_length=39)
    course = models.CharField(
        db_column="course", max_length=7, blank=True, null=True
    )  # Removed db_collation
    year = models.IntegerField(db_column="year", blank=True, null=True)
    branch = models.CharField(db_column="branch", max_length=10, blank=True, null=True)
    sec = models.CharField(
        db_column="sec", max_length=1, blank=True, null=True
    )  # Removed db_collation
    hackerrank_username = models.CharField(
        db_column="hackerrank_username", max_length=48, blank=True, null=True
    )  # Removed db_collation
    codeforces_username = models.CharField(
        db_column="codeforces_username", max_length=40, blank=True, null=True
    )  # Removed db_collation
    codechef_username = models.CharField(
        db_column="codechef_username", max_length=92, blank=True, null=True
    )  # Removed db_collation
    spoj_username = models.CharField(
        db_column="spoj_username", max_length=22, blank=True, null=True
    )  # Removed db_collation
    interviewbit_username = models.CharField(
        db_column="interviewbit_username", max_length=42, blank=True, null=True
    )  # Removed db_collation
    leetcode_username = models.CharField(
        db_column="leetcode_username", max_length=29, blank=True, null=True
    )  # Removed db_collation
    gfg_username = models.CharField(
        db_column="gfg_username", max_length=48, blank=True, null=True
    )  # Removed db_collation

    class Meta:
        db_table = "student_master"


class StudentScores(models.Model):
    roll_no = models.CharField(db_column="roll_no", primary_key=True, max_length=10)
    hackerrank = models.TextField(db_column="hackerrank", blank=True, null=True)
    hackerrank_score = models.IntegerField(db_column="hackerrank_score")
    codeforces = models.TextField(db_column="codeforces", blank=True, null=True)
    codeforces_score = models.IntegerField(db_column="codeforces_score")
    codechef = models.TextField(db_column="codechef", blank=True, null=True)
    codechef_score = models.IntegerField(db_column="codechef_score")
    spoj = models.TextField(db_column="spoj", blank=True, null=True)
    spoj_score = models.IntegerField(db_column="spoj_score")
    interviewbit = models.TextField(db_column="interviewbit", blank=True, null=True)
    interviewbit_score = models.IntegerField(db_column="interviewbit_score")
    leetcode = models.TextField(db_column="leetcode", blank=True, null=True)
    leetcode_score = models.IntegerField(db_column="leetcode_score")
    gfg = models.TextField(db_column="gfg", blank=True, null=True)
    gfg_score = models.IntegerField(db_column="gfg_score")
    overall_score = models.IntegerField(db_column="overall_score")
    daily_scores = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "student_scores"


class Averages(models.Model):
    averages = models.CharField(db_column="averages", primary_key=True, max_length=45)
    cse = models.DecimalField(max_digits=10, decimal_places=2)
    it = models.DecimalField(max_digits=10, decimal_places=2)
    ece = models.DecimalField(max_digits=10, decimal_places=2)
    eee = models.DecimalField(max_digits=10, decimal_places=2)
    csm = models.DecimalField(max_digits=10, decimal_places=2)
    aiml = models.DecimalField(max_digits=10, decimal_places=2)
    mec = models.DecimalField(max_digits=10, decimal_places=2)
    civ = models.DecimalField(max_digits=10, decimal_places=2)
    aids = models.DecimalField(max_digits=10, decimal_places=2)
    college = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "averages"
