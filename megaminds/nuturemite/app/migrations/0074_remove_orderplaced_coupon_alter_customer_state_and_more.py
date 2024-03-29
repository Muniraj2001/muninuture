# Generated by Django 4.2.7 on 2023-12-29 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='coupon',
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Jammu & Kashmir', 'Jammu & Kashmir'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Chattisgarh', 'Chattisgarh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Gujrat', 'Gujrat'), ('Assam', 'Assam'), ('Delhi', 'Delhi'), ('Bihar', 'Bihar'), ('Daman and Diu', 'Daman and Diu'), ('Haryana', 'Haryana'), ('Goa', 'Goa'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Andhra Pradesh', 'Andhra Pradesh')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Packed', 'packed'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('SH', 'Sexual health'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('SH', 'Sexual health'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('SH', 'Sexual health'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('SH', 'Sexual health'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('SH', 'Sexual health'), ('GH', 'General Health'), ('DH', 'Digestive Health'), ('OG', 'Organic'), ('VM', 'Vitamins&Minerals'), ('PC', 'Personal Care'), ('MH', 'Men Health'), ('IH', 'Immune Health'), ('AN', 'Antioxidants'), ('HS', 'Herbal, Specialty Supplements'), ('WH', 'Women health'), ('AV', 'Ayurvedic')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]
