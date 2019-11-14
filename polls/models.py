from django.db import models

# Create your models here.
# 질문목
class Question(models.Model):
    # 문자열 저장 CharField, 시간 DateTimeField
    # 어떤 색상을 좋아하세요?
    question_text = models.CharField(max_length=200)
    # 2019년 11월 12일
    # 캐릭터 한글은 문제가 있다.
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # CASCADE 질문삭제하면 같이 삭제 하겠다.
    question_id = models.ForeignKey(Question, related_name='choice', on_delete=models.CASCADE)
    # 빨강색, 초록색, 파란색
    choice_text = models.CharField(max_length=200)
    # 0 몇번 선택받았는지 카운트 센다.
    votes = models.IntegerField(default=0)

    def __str__ (self):
        return self.choice_text