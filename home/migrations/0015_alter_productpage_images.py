# Generated by Django 4.2.10 on 2024-03-10 07:46

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_productfirstmenu_page_ptr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpage',
            name='images',
            field=wagtail.fields.StreamField([('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.RichTextBlock(required=False))]))], blank=True, use_json_field=True),
        ),
    ]
