# Generated by Django 2.2.12 on 2020-06-02 16:57

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hub", "0005_auto_20200526_1748"),
    ]

    operations = [
        migrations.CreateModel(
            name="Domain",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("name", models.CharField(max_length=254, unique=True, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
            ],
            options={"verbose_name": "Domain", "verbose_name_plural": "Domains",},
        ),
        migrations.AlterModelOptions(name="city", options={"verbose_name": "City", "verbose_name_plural": "Cities"},),
        migrations.AlterField(
            model_name="candidate",
            name="domain",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="candidates", to="hub.Domain"
            ),
        ),
        migrations.AlterField(
            model_name="candidatevote",
            name="domain",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="votes", to="hub.Domain"),
        ),
        migrations.AlterField(
            model_name="organization",
            name="domain",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="orgs", to="hub.Domain"),
        ),
        migrations.AlterField(
            model_name="organizationvote",
            name="domain",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="+", to="hub.Domain"),
        ),
    ]
