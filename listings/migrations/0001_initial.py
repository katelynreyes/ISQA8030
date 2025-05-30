# Generated by Django 5.2 on 2025-05-04 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="listing",
            fields=[
                ("listing_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("street", models.CharField(max_length=250)),
                ("city", models.CharField(max_length=30)),
                ("state", models.CharField(max_length=2)),
                ("zip", models.CharField(max_length=5)),
                ("description", models.CharField(max_length=1000)),
                (
                    "property_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("bedrooms", models.IntegerField()),
                ("bathrooms", models.IntegerField()),
                ("sq_footage", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Available", "Available"),
                            ("Pending", "Pending"),
                            ("Sold", "Sold"),
                        ],
                        max_length=10,
                    ),
                ),
                ("created_date", models.DateField()),
                ("updated_date", models.DateField()),
                ("is_visible", models.BooleanField(default=True)),
                ("is_featured", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="neighborhood",
            fields=[
                (
                    "neighborhood_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                (
                    "neighborhood_name",
                    models.CharField(
                        choices=[
                            ("Aksarben Village", "Aksarben Village"),
                            ("Benson", "Benson"),
                            ("Blackstone", "Blackstone"),
                            ("Downtown", "Downtown"),
                            ("Dundee", "Dundee"),
                            ("Elkhorn", "Elkhorn"),
                            ("Field Club", "Field Club"),
                            ("Midtown Crossing", "Midtown Crossing"),
                            ("Millard", "Millard"),
                            ("Old Market", "Old Market"),
                            ("Regency", "Regency"),
                            ("South Omaha", "South Omaha"),
                            ("West Omaha", "West Omaha"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="price_search",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("label", models.CharField(default="Unspecified", max_length=100)),
                ("min_price", models.IntegerField(default=0)),
                ("max_price", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="property_type",
            fields=[
                ("property_id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "property_type",
                    models.CharField(
                        choices=[
                            ("Bungalow", "Bungalow"),
                            ("Colonial", "Colonial"),
                            ("Condominium", "Condominium"),
                            ("Craftsman", "Craftsman"),
                            ("Log Cabin", "Log Cabin"),
                            ("Modern", "Modern"),
                            ("Ranch", "Ranch"),
                            ("Split Level", "Split Level"),
                            ("Townhome", "Townhome"),
                            ("Tudor", "Tudor"),
                            ("Victorian", "Victorian"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="listing_photo",
            fields=[
                ("photo_id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "photo_url",
                    models.ImageField(blank=True, upload_to="listing_images/"),
                ),
                ("order", models.PositiveIntegerField(default=0)),
                (
                    "listing",
                    models.ForeignKey(
                        null="True",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="listings.listing",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.AddField(
            model_name="listing",
            name="neighborhood",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="listings.neighborhood"
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="price_search",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="listings.price_search"
            ),
        ),
        migrations.AddField(
            model_name="listing",
            name="property_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="listings.property_type"
            ),
        ),
        migrations.CreateModel(
            name="SearchLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "neighborhood",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="listings.neighborhood",
                    ),
                ),
                (
                    "price_search",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="listings.price_search",
                    ),
                ),
                (
                    "property_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="listings.property_type",
                    ),
                ),
            ],
        ),
    ]
