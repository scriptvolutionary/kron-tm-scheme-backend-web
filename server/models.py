from django.db import models


class Facility(models.Model):
    facility_parent_id = models.IntegerField('Идентификатор родительского объекта', blank=True, null=True)
    facility_type_id = models.IntegerField('Идентификатор типа объекта', blank=True, null=True)
    field_id = models.IntegerField('Идентификатор месторождения', blank=True, null=True)
    cluster_id = models.IntegerField('Идентификатор куста', blank=True, null=True)
    facility_name = models.CharField('Название объекта', max_length=40)
    facility_process_rate = models.SmallIntegerField('Период обновления', default='30', blank=True, null=True)
    facility_position = models.IntegerField('Позиция', unique=True, blank=True, null=True)
    facility_coord_ltd = models.FloatField('Широта', blank=True, null=True)
    facility_coord_lng = models.FloatField('Долгота', blank=True, null=True)
    script_id = models.IntegerField('Идентификатор на вид обработки в интерфейсе', blank=True, null=True)
    facility_actual = models.BooleanField('Актуальность объекта', default=1, blank=True, null=True)
    facility_mode_id = models.IntegerField('Режим объекта', default='1', help_text='1 - Актуальный, 2 - Тест, 3 - Не актуальный', blank=True, null=True)
    dept_id = models.IntegerField('Привязка к подразделению (месторождению)', blank=True, null=True)
    facility_create_date = models.DateTimeField('Дата заведения объекта', default='01-01-1999', blank=True, null=True)

    class Meta:
        verbose_name = 'объект'
        verbose_name_plural = 'объекты'

    def __str__(self):
        return self.facility_name


class Script(models.Model):
    script_name = models.CharField('Название скрипта', max_length=40, unique=True)
    construction_script = models.TextField('Сценарий скрипта')
    facility_changed_script = models.TextField('Изменение сценария объектом')
    facility_process_script = models.TextField('Процесс сценария объекта')
    design_form = models.TextField('Дизайн формы')
    script_tag_mask = models.IntegerField('Маска')
    design_web = models.TextField('Дизайн веб')

    class Meta:
        verbose_name = 'скрипт'
        verbose_name_plural = 'скрипты'

    def __str__(self):
        return self.script_name


class Property(models.Model):
    device_id = models.IntegerField('Идентификатор устройства')
    facility_id = models.ForeignKey(
        'Facility',
        on_delete=models.CASCADE,
        verbose_name='Идентификатор объекта',
    )
    active_flange_no = models.SmallIntegerField('Номер активного фланца')
    active_flange_id = models.IntegerField('Идентификатор активного фланца')
    property_type_id = models.IntegerField('Идентификатор типа свойства')
    unit_id = models.IntegerField('Идентификатор блока')
    property_path = models.CharField('Пусть свойства', max_length=255)
    property_formula = models.CharField('Формула свойства', max_length=1000, blank=True, null=True)
    property_factor = models.FloatField('Фактор свойства')
    property_refresh_rate = models.SmallIntegerField('Частота обновления свойства')
    property_process_rate = models.IntegerField('Скорость процесса собственности')
    property_save_rate = models.IntegerField('Коэффициент сохранения имущества')
    property_desc = models.CharField('Описание свойства', max_length=1000, blank=True, null=True)
    property_is_fast = models.BooleanField('Быстрое свойство')
    property_is_visible_form = models.BooleanField('Cвойство является видимой формой')
    property_is_not_calc_rate = models.BooleanField('Свойство не рассчитано', blank=True, null=True)
    property_is_use_active_facility_flange = models.BooleanField('Свойство использует активный фланец объекта', blank=True, null=True)
    property_expression = models.CharField('Выражение свойства', max_length=1000, blank=True, null=True)
    property_use_source = models.BooleanField('Источник использования имущества')
    property_color = models.IntegerField('Цвет свойства', blank=True, null=True)

    class Meta:
        verbose_name = 'свойство'
        verbose_name_plural = 'свойства'

    def __str__(self):
        return 'Свойство: {}'.format(self.id)


class Form(models.Model):
    form_class = models.CharField('Класс формы', max_length=255)
    form_name = models.CharField('Название формы', max_length=40)
    form_row = models.BooleanField('Строка формы')
    form_image_index = models.IntegerField('Идентификатор изображения формы')
    form_desc = models.CharField('Описание формы', max_length=255, blank=True, null=True)
    form_active = models.BooleanField('Форма активна')
    form_settings = models.CharField('Настройки формы', max_length=1000, blank=True, null=True)
    is_facility_main_form = models.BooleanField('Основная форма объекта')

    class Meta:
        verbose_name = 'форма'
        verbose_name_plural = 'формы'

    def __str__(self):
        return self.form_name


class FacilityType(models.Model):
    facility_type_sysname = models.CharField('Системное имя типа объекта', max_length=40)
    facility_type_class = models.CharField('Класс типа объекта', max_length=255)
    facility_type_name = models.CharField('Имя типа объекта', max_length=255)
    node_type_id = models.IntegerField('Идентификатор типа узла')
    event_category_mast = models.BigIntegerField('Битовая маска', blank=True, null=True)
    facility_type_sname = models.CharField('Сокращенное имя типа объекта', max_length=40)

    class Meta:
        verbose_name = 'тип объекта'
        verbose_name_plural = 'типы объекта'

    def __str__(self):
        return self.facility_type_name


class Event(models.Model):
    event_type_id = models.IntegerField('Идентификатор типа события')
    event_type_base_id = models.IntegerField('Идентификатор базового типа события', blank=True, null=True)
    event_date = models.DateTimeField('Дата события')
    flange_id = models.IntegerField('Идентификатор фланца')
    facility_id = models.ForeignKey('Facility', on_delete=models.CASCADE, verbose_name='Идентификатор свойства')
    flange_no = models.IntegerField('Номер фланца')
    property_id = models.ForeignKey('Property', on_delete=models.CASCADE, verbose_name='Идентификатор свойства')
    property_value = models.FloatField('Значение свойства')
    event_date_confirm = models.DateTimeField('Дата подтверждения события', blank=True, null=True)

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'события'

    def __str__(self):
        return self.id


class FormScript(models.Model):
    form_id = models.ForeignKey('Form', on_delete=models.CASCADE, verbose_name='Идентификатор формы')
    facility_type_id = models.ForeignKey('FacilityType', on_delete=models.CASCADE, verbose_name='Идентификатор типа объекта')
    facility_id = models.ForeignKey('Facility', on_delete=models.CASCADE, verbose_name='Идентификатор объекта')
    script_id = models.ForeignKey('Script', on_delete=models.CASCADE, verbose_name='Идентификатор скрипта')
    design_form_facility_type = models.CharField('Форма конструкции тип объекта', max_length=255)

    class Meta:
        verbose_name = 'сценарий формы'
        verbose_name_plural = 'сценарии формы'

    def __str__(self):
        return self.id
