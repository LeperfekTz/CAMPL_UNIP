# Generated by Django 5.1.2 on 2024-11-18 21:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0002_usuario_alter_aula_options_alter_estudante_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aula',
            options={},
        ),
        migrations.AlterModelOptions(
            name='estudante',
            options={},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={},
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='bairro',
            new_name='nome_responsavel',
        ),
        migrations.RemoveField(
            model_name='estudante',
            name='email',
        ),
        migrations.RemoveField(
            model_name='estudante',
            name='email_responsavel',
        ),
        migrations.RemoveField(
            model_name='estudante',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='estudante',
            name='nome_responsavel',
        ),
        migrations.RemoveField(
            model_name='estudante',
            name='telefone',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='materia',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='URLimagem',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='dataCriacao',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='papel',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='rua',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='senha',
        ),
        migrations.AddField(
            model_name='aula',
            name='dataCriacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudante',
            name='dataCriacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudante',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meuapp.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='dataCriacao',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='disciplina',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meuapp.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='email_responsavel',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='aula',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuapp.professor')),
            ],
        ),
        migrations.AlterField(
            model_name='aula',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuapp.classe'),
        ),
        migrations.CreateModel(
            name='Emprego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=30, unique=True)),
                ('rg', models.CharField(max_length=30, unique=True)),
                ('cnpj', models.CharField(max_length=30, unique=True)),
                ('compania', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=30)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='meuapp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Gerente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuapp.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meuapp.usuario')),
            ],
        ),
        migrations.DeleteModel(
            name='Turma',
        ),
    ]