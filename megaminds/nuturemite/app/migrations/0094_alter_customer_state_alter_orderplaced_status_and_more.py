# Generated by Django 4.2.7 on 2024-01-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0093_remove_orderplaced_delivery_partner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Goa', 'Goa'), ('Daman and Diu', 'Daman and Diu'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Delhi', 'Delhi'), ('Chandigarh', 'Chandigarh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Gujrat', 'Gujrat'), ('Bihar', 'Bihar'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Assam', 'Assam'), ('Haryana', 'Haryana'), ('Chattisgarh', 'Chattisgarh')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Pending', 'Pending'), ('Packed', 'packed'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('VM', 'Vitamins&Minerals'), ('DH', 'Digestive Health'), ('K', 'Vitamin K'), ('D3', 'Vitamin D3'), ('C', 'Vitamin C'), ('WH', 'Women health'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('B12', 'Vitamin B12'), ('PC', 'Personal Care'), ('MH', 'Men Health'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('AV', 'Ayurvedic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('VM', 'Vitamins&Minerals'), ('DH', 'Digestive Health'), ('K', 'Vitamin K'), ('D3', 'Vitamin D3'), ('C', 'Vitamin C'), ('WH', 'Women health'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('B12', 'Vitamin B12'), ('PC', 'Personal Care'), ('MH', 'Men Health'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('AV', 'Ayurvedic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('VM', 'Vitamins&Minerals'), ('DH', 'Digestive Health'), ('K', 'Vitamin K'), ('D3', 'Vitamin D3'), ('C', 'Vitamin C'), ('WH', 'Women health'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('B12', 'Vitamin B12'), ('PC', 'Personal Care'), ('MH', 'Men Health'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('AV', 'Ayurvedic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('VM', 'Vitamins&Minerals'), ('DH', 'Digestive Health'), ('K', 'Vitamin K'), ('D3', 'Vitamin D3'), ('C', 'Vitamin C'), ('WH', 'Women health'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('B12', 'Vitamin B12'), ('PC', 'Personal Care'), ('MH', 'Men Health'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('AV', 'Ayurvedic')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('VM', 'Vitamins&Minerals'), ('DH', 'Digestive Health'), ('K', 'Vitamin K'), ('D3', 'Vitamin D3'), ('C', 'Vitamin C'), ('WH', 'Women health'), ('E', 'Vitamin E'), ('GH', 'General Health'), ('OG', 'Organic'), ('A', 'Vitamin A'), ('IH', 'Immune Health'), ('SH', 'Sexual health'), ('B12', 'Vitamin B12'), ('PC', 'Personal Care'), ('MH', 'Men Health'), ('HS', 'Herbal, Specialty Supplements'), ('AN', 'Antioxidants'), ('AV', 'Ayurvedic')], max_length=3),
        ),
    ]
