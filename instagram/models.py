from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # User모델(auth.User를 말한다)은 언제든 변경될 수 있으므로 settings.AUTH_USER_MODEL로 지정하여 좀 더 콘크리트하게 정할 수 있다.
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%y/%m/%d')
    tag_set = models.ManyToManyField('Tag', blank=True)
    # tag_set에서 blank=True옵션이 의미가 있는 이유는
    # 포스팅에 태그를 하나도 지정하지 않았을시에 유효성검사를 실패하기 때문에 default값인 False를 True로 바꿔준다.
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString 같은 기능
    def __str__(self):
        return self.message

    class Meta:
        ordering = ['-id']

    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             limit_choices_to = {'is_public':True}) # post_id 필드가 생성이 된다.
    # Form을 통한 Choice 위젯에서 선택항목 제한 가치
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # unique=True 해당 태그 하나가 생성되면 해당 테이블 내에서는 유니크함을 보장 받아야 한다.
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name