from django.db import models

from .common import BaseModel


class Todo(BaseModel):  # 필드와 그 옵션을 정의합니다.
    title = models.CharField(
        max_length=64,
        verbose_name="To Do 제목",
        help_text="To Do 제목 입니다."
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name="To Do 설명",
        help_text="To Do 설명 입니다."
    )
    author = models.CharField(
        max_length=16,
        verbose_name="To Do 작성자",
        help_text="To Do 작성자를 나타냅니다."
    )
    due_date = models.DateTimeField(
        verbose_name="To Do 마감일",
        help_text="To Do 마감일을 나타냅니다."
    )
    completed = models.BooleanField(
        default=False,
        verbose_name="To Do 완료 여부",
        help_text="To Do 완료 여부를 나타냅니다."
    )

    class Meta:
        verbose_name = 'To Do 리스트'
        verbose_name_plural = 'To Do 리스트(들)'
        ordering = ['-created_at']

    def __str__(self):
        return f"Todo-{self.author}-{self.created_at}"