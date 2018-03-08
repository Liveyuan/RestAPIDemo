# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-07 13:06
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner', verbose_name='\u8f6e\u64ad\u56fe\u7247')),
                ('index', models.IntegerField(default=0, verbose_name='\u8f6e\u64ad\u987a\u5e8f')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8f6e\u64ad\u5546\u54c1',
                'verbose_name_plural': '\u8f6e\u64ad\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_sn', models.CharField(default='', max_length=50, verbose_name='\u5546\u54c1\u552f\u4e00\u8d27\u53f7')),
                ('name', models.CharField(max_length=100, verbose_name='\u5546\u54c1\u540d')),
                ('click_num', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u91cf')),
                ('sold_num', models.IntegerField(default=0, verbose_name='\u9500\u552e\u6570\u91cf')),
                ('fav_num', models.IntegerField(default=0, verbose_name='\u6536\u85cf\u6570')),
                ('goods_num', models.IntegerField(default=0, verbose_name='\u5e93\u5b58\u6570\u91cf')),
                ('market_price', models.FloatField(default=0, verbose_name='\u5e02\u573a\u4ef7\u683c')),
                ('shop_price', models.FloatField(default=0, verbose_name='\u5e97\u94fa\u4ef7\u683c')),
                ('goods_brief', models.TextField(default='', max_length=500, verbose_name='\u77ed\u63cf\u8ff0')),
                ('goods_desc', DjangoUeditor.models.UEditorField(default='', verbose_name='\u8be6\u60c5\u63cf\u8ff0')),
                ('ship_free', models.BooleanField(default=True, verbose_name='\u662f\u5426\u5305\u90ae')),
                ('goods_front_image', models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='\u5c01\u9762\u56fe')),
                ('is_new', models.BooleanField(default=False, verbose_name='\u662f\u5426\u65b0\u54c1')),
                ('is_hot', models.BooleanField(default=False, verbose_name='\u662f\u5426\u70ed\u9500')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u4fe1\u606f',
                'verbose_name_plural': '\u5546\u54c1\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='\u7c7b\u522b\u540d', max_length=30, verbose_name='\u7c7b\u522b\u540d')),
                ('code', models.CharField(default='', help_text='\u7c7b\u522bcode', max_length=30, verbose_name='\u7c7b\u522bcode')),
                ('desc', models.TextField(default='', help_text='\u7c7b\u522b\u63cf\u8ff0', verbose_name='\u7c7b\u522b\u63cf\u8ff0')),
                ('category_type', models.IntegerField(choices=[(1, '\u4e00\u7ea7\u7c7b\u76ee'), (2, '\u4e8c\u7ea7\u7c7b\u76ee'), (3, '\u4e09\u7ea7\u7c7b\u76ee')], help_text='\u7c7b\u76ee\u7ea7\u522b', verbose_name='\u7c7b\u76ee\u7ea7\u522b')),
                ('is_tab', models.BooleanField(default=False, help_text='\u662f\u5426\u5bfc\u822a', verbose_name='\u662f\u5426\u5bfc\u822a')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('parent_category', models.ForeignKey(blank=True, help_text='\u7236\u76ee\u5f55', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='\u7236\u7c7b\u76ee\u5f55\u7ea7')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u7c7b\u522b',
                'verbose_name_plural': '\u5546\u54c1\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='\u54c1\u724c\u540d', max_length=30, verbose_name='\u54c1\u724c\u540d')),
                ('desc', models.TextField(default='', help_text='\u54c1\u724c\u63cf\u8ff0', max_length=200, verbose_name='\u54c1\u724c\u63cf\u8ff0')),
                ('image', models.ImageField(max_length=200, upload_to='brands/')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.GoodsCategory', verbose_name='\u5546\u54c1\u7c7b\u76ee')),
            ],
            options={
                'db_table': 'goods_goodsbrand',
                'verbose_name': '\u54c1\u724c',
                'verbose_name_plural': '\u54c1\u724c',
            },
        ),
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='\u70ed\u641c\u8bcd')),
                ('index', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u70ed\u641c\u8bcd',
                'verbose_name_plural': '\u70ed\u641c\u8bcd',
            },
        ),
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='goods.GoodsCategory', verbose_name='\u5546\u54c1\u7c7b\u76ee')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.Goods')),
            ],
            options={
                'verbose_name': '\u9996\u9875\u5546\u54c1\u7c7b\u522b\u5e7f\u544a',
                'verbose_name_plural': '\u9996\u9875\u5546\u54c1\u7c7b\u522b\u5e7f\u544a',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='\u5546\u54c1\u5206\u7c7b'),
        ),
        migrations.AddField(
            model_name='banner',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='\u5546\u54c1'),
        ),
    ]
