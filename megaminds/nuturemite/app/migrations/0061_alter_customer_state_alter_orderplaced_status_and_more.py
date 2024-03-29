# Generated by Django 4.2.7 on 2023-12-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0060_shopnow_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Delhi', 'Delhi'), ('Gujrat', 'Gujrat'), ('Chattisgarh', 'Chattisgarh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Chandigarh', 'Chandigarh'), ('Daman and Diu', 'Daman and Diu'), ('Haryana', 'Haryana'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Bihar', 'Bihar'), ('Goa', 'Goa')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Cancel', 'Cancel'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('Pending', 'Pending'), ('Packed', 'packed'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('VM', 'Vitamins&Minerals')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('VM', 'Vitamins&Minerals')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('VM', 'Vitamins&Minerals')], max_length=2),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('VM', 'Vitamins&Minerals')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('GH', 'General Health'), ('OG', 'Organic'), ('HS', 'Herbal, Specialty Supplements'), ('PC', 'Personal Care'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('MH', 'Men Health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('WH', 'Women health'), ('VM', 'Vitamins&Minerals')], max_length=2),
        ),
    ]
