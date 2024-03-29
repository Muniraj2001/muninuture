# Generated by Django 4.2.7 on 2023-11-30 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_remove_product_images_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='product_images', to='app.productimage'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Bihar', 'Bihar'), ('Delhi', 'Delhi'), ('Assam', 'Assam'), ('Goa', 'Goa'), ('Chandigarh', 'Chandigarh'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Gujrat', 'Gujrat'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Daman and Diu', 'Daman and Diu'), ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'), ('Haryana', 'Haryana'), ('Chattisgarh', 'Chattisgarh'), ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancel', 'Cancel'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Packed', 'packed'), ('On The Wey', 'On The Way')], default='pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='popular',
            name='category',
            field=models.CharField(choices=[('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('WH', 'Women health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('GH', 'General Health'), ('OG', 'Organic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('WH', 'Women health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('GH', 'General Health'), ('OG', 'Organic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product1',
            name='category',
            field=models.CharField(choices=[('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('WH', 'Women health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('GH', 'General Health'), ('OG', 'Organic')], max_length=2),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='category',
            field=models.CharField(choices=[('PC', 'Personal Care'), ('VM', 'Vitamins&Minerals'), ('AV', 'Ayurvedic'), ('AN', 'Antioxidants'), ('IH', 'Immune Health'), ('WH', 'Women health'), ('DH', 'Digestive Health'), ('SH', 'Sexual health'), ('HS', 'Herbal, Specialty Supplements'), ('MH', 'Men Health'), ('GH', 'General Health'), ('OG', 'Organic')], max_length=2),
        ),
    ]
