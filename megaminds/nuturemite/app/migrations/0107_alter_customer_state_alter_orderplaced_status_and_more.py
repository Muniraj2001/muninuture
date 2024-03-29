# Generated by Django 4.2.7 on 2024-01-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0106_alter_customer_state_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Delhi', 'Delhi'), ('Daman and Diu', 'Daman and Diu'), ('Gujrat', 'Gujrat'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Assam', 'Assam'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Bihar', 'Bihar'), ('Chattisgarh', 'Chattisgarh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Goa', 'Goa'), ('Chandigarh', 'Chandigarh'), ('Haryana', 'Haryana')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Packed', 'packed'), ('On The Wey', 'On The Way'), ('Cancel', 'Cancel'), ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('GH', 'General Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('E', 'Vitamin E'), ('HS', 'Herbal, Specialty Supplements'), ('C', 'Vitamin C'), ('B12', 'Vitamin B12'), ('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('AN', 'Antioxidants'), ('VM', 'Vitamins&Minerals'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('K', 'Vitamin K'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('GH', 'General Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('E', 'Vitamin E'), ('HS', 'Herbal, Specialty Supplements'), ('C', 'Vitamin C'), ('B12', 'Vitamin B12'), ('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('AN', 'Antioxidants'), ('VM', 'Vitamins&Minerals'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('K', 'Vitamin K'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('GH', 'General Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('E', 'Vitamin E'), ('HS', 'Herbal, Specialty Supplements'), ('C', 'Vitamin C'), ('B12', 'Vitamin B12'), ('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('AN', 'Antioxidants'), ('VM', 'Vitamins&Minerals'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('K', 'Vitamin K'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='shopnow',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('GH', 'General Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('E', 'Vitamin E'), ('HS', 'Herbal, Specialty Supplements'), ('C', 'Vitamin C'), ('B12', 'Vitamin B12'), ('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('AN', 'Antioxidants'), ('VM', 'Vitamins&Minerals'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('K', 'Vitamin K'), ('WH', 'Women health')], max_length=3),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('A', 'Vitamin A'), ('GH', 'General Health'), ('AV', 'Ayurvedic'), ('PC', 'Personal Care'), ('E', 'Vitamin E'), ('HS', 'Herbal, Specialty Supplements'), ('C', 'Vitamin C'), ('B12', 'Vitamin B12'), ('D3', 'Vitamin D3'), ('IH', 'Immune Health'), ('MH', 'Men Health'), ('SH', 'Sexual health'), ('AN', 'Antioxidants'), ('VM', 'Vitamins&Minerals'), ('OG', 'Organic'), ('DH', 'Digestive Health'), ('K', 'Vitamin K'), ('WH', 'Women health')], max_length=3),
        ),
    ]
