# Generated by Django 3.1.7 on 2021-04-12 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_auto_20210411_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bank',
            options={'verbose_name_plural': 'Банки'},
        ),
        migrations.AlterModelOptions(
            name='bs',
            options={'verbose_name_plural': 'Бухгалтерские счета'},
        ),
        migrations.AlterModelOptions(
            name='fo',
            options={'verbose_name_plural': 'Формы организации'},
        ),
        migrations.AlterModelOptions(
            name='fp',
            options={'verbose_name_plural': 'Финансовые показатели'},
        ),
        migrations.AlterModelOptions(
            name='nk',
            options={'verbose_name_plural': 'Налоговые комитеты'},
        ),
        migrations.AlterModelOptions(
            name='pb',
            options={'verbose_name_plural': 'Предприятия_банки'},
        ),
        migrations.AlterModelOptions(
            name='predpriyatie',
            options={'verbose_name_plural': 'Предприятия'},
        ),
        migrations.AlterModelOptions(
            name='pvd',
            options={'verbose_name_plural': 'Предприятия_виды деятельности'},
        ),
        migrations.AlterModelOptions(
            name='vhd',
            options={'verbose_name_plural': 'Виды хозяйственной деятельности'},
        ),
        migrations.AlterField(
            model_name='bank',
            name='address',
            field=models.CharField(max_length=60, unique=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Код банка'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='bs',
            name='kod',
            field=models.CharField(max_length=4, primary_key=True, serialize=False, unique=True, verbose_name='Код счета'),
        ),
        migrations.AlterField(
            model_name='bs',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='fo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='fo',
            name='name',
            field=models.CharField(choices=[('ТОО', 'Товарищество с ограниченной ответственностью'), ('ИП', 'Индивидуальный предприниматель'), ('ООО', 'Общество с ограниченной ответственностью'), ('АО', 'Акционерное общество'), ('ЗАО', 'Закрытое акционерное общество')], max_length=50, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='fp',
            name='bin_fp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.predpriyatie', verbose_name='БИН'),
        ),
        migrations.AlterField(
            model_name='fp',
            name='bs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.bs', verbose_name='Код счета'),
        ),
        migrations.AlterField(
            model_name='fp',
            name='date',
            field=models.DateField(verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='fp',
            name='kvartal',
            field=models.CharField(choices=[('Первый', '1'), ('Второй', '2'), ('Третий', '3'), ('Четвертый', '4')], max_length=50, verbose_name='Квартал'),
        ),
        migrations.AlterField(
            model_name='fp',
            name='priznak',
            field=models.CharField(choices=[('Дебет', 'Дт'), ('Кредит', 'Кт')], max_length=50, verbose_name='Признак'),
        ),
        migrations.AlterField(
            model_name='fp',
            name='summa',
            field=models.PositiveIntegerField(verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='nk',
            name='address',
            field=models.CharField(max_length=60, unique=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='nk',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Код комитета'),
        ),
        migrations.AlterField(
            model_name='nk',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='pb',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.bank', verbose_name='Код банка'),
        ),
        migrations.AlterField(
            model_name='pb',
            name='bin_pb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.predpriyatie', verbose_name='БИН'),
        ),
        migrations.AlterField(
            model_name='pb',
            name='schet',
            field=models.CharField(max_length=20, unique=True, verbose_name='Лицевой счет'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='address',
            field=models.CharField(max_length=60, unique=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='bin_id',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, unique=True, verbose_name='БИН'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='chislo_rab',
            field=models.PositiveIntegerField(verbose_name='Число работников'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='date',
            field=models.DateField(verbose_name='Дата постановки на учет'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='fio_ruk',
            field=models.CharField(max_length=50, unique=True, verbose_name='ФИО руководителя'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='form_org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.fo', verbose_name='Код формы организации'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='full_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Полное наименование'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='nalog_kom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.nk', verbose_name='Код налогового комитета'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='phone',
            field=models.CharField(max_length=11, unique=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='sh_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Сокращенное наименование'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='uchrediteli',
            field=models.CharField(max_length=200, unique=True, verbose_name='Учредители'),
        ),
        migrations.AlterField(
            model_name='predpriyatie',
            name='vid_hoz_d',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.vhd', verbose_name='Код основного вида хозяйственной деятельности'),
        ),
        migrations.AlterField(
            model_name='pvd',
            name='bin_pvd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.predpriyatie', verbose_name='БИН'),
        ),
        migrations.AlterField(
            model_name='pvd',
            name='vid_hoz_d',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebApp.vhd', verbose_name='Код вида хозяйственной деятельности'),
        ),
        migrations.AlterField(
            model_name='vhd',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Код вида хозяйственной деятельности'),
        ),
        migrations.AlterField(
            model_name='vhd',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Наименование'),
        ),
    ]
