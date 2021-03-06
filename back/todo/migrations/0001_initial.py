# Generated by Django 3.0.8 on 2020-07-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='데이터가 생성된 날짜입니다.', verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='데이터가 수정된 날짜입니다.', verbose_name='수정 일시')),
                ('title', models.CharField(help_text='To Do 제목 입니다.', max_length=64, verbose_name='To Do 제목')),
                ('description', models.CharField(blank=True, help_text='To Do 설명 입니다.', max_length=256, null=True, verbose_name='To Do 설명')),
                ('author', models.CharField(help_text='To Do 작성자를 나타냅니다.', max_length=16, verbose_name='To Do 작성자')),
                ('due_date', models.DateTimeField(help_text='To Do 마감일을 나타냅니다.', verbose_name='To Do 마감일')),
                ('completed', models.BooleanField(default=False, help_text='To Do 완료 여부를 나타냅니다.', verbose_name='To Do 완료 여부')),
            ],
            options={
                'verbose_name': 'To Do 리스트',
                'verbose_name_plural': 'To Do 리스트(들)',
                'ordering': ['-created_at'],
            },
        ),
    ]
