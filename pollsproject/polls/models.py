from django.db import models
import datetime
from django.utils import timezone

#自分好みでテーブル名を変更することも可能！その際には、Metaクラスを付与する必要性はある。
    #ex) 
    #class Book(models.Model):
    # title = models.CharField(max_length=100)
    # author = models.CharField(max_length=50)
    # published_date = models.DateField()

    # class Meta:
    #     db_table = 'books'  # テーブル名を明示的に指定



class Question(models.Model):

    #question_text や pub_date などのFieldインスタンスは、Pythonコードで使うとともに、データベースも列の名前としても使う
    #この場合、実際のテーブル名は、polls_questionとなる
    #命名規則は、pollsのQuestionクラスを使用してるから　テーブル名のQuestionの小文字を採用
    #CharField は文字のフィールド

    #max_lengthはバリデーション
    question_text = models.CharField(max_length=200)
    #DateTimeField は日時フィールド
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # ForeignKey を使用してリレーションシップが定義されていることに注目してください。
    # これは、それぞれの Choice が一つの Question に関連付けられることを Django に伝えます。 
    # Django は 多対一、多対多、そして一対一のような一般的なデータベースリレーションシップすべてをサポートします。

    #この場合、実際のテーブル名は、polls_choiceとなる

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text