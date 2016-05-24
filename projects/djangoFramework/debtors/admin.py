from django.contrib import admin
from import_export import resources, fields
# from debtors.models import Crime, Debtor, Company
from import_export.admin import ImportExportModelAdmin
from import_export import widgets
from import_export.widgets import ForeignKeyWidget

# Register your models here.
from .models import Company, Debtor, Debt, Comment, Crime

#class DebtorWidget(widgets.ForeignKeyWidget):
#    def clean(selfself, value):
#        return self.model.objects.get_or_create


class CompanyResource(resources.ModelResource):
    class Meta:
        model = Company


class CrimeResource(resources.ModelResource):
    #debtor = fields.Field(column_name='debtor', attribute='debtor', widget = ForeignKeyWidget(Debtor, 'debtor_name'))
    #debtor = fields.Field(column_name='debtor_id', attribute='debtor',  widget=ForeignKeyWidget(Debtor, 'debtor_id'))

    class Meta:
        model = Crime
        import_id_fields = ['id']
        #exclude = ( 'dob', )

        #widgets = { 'dob' : { 'format' : '%Y.%m.%Y' }, }
        #fields = ('debtor_id')
        #def dehydrate_school_id(self, crime):
        #    return crime.debtor.debtor_name
        #import_id_fields = ('id')
       # fields = ('causeNumber', 'sex', 'race', 'offense_text', 'offense_type', 'case_text', 'disposition_text',
        #          'judgment_text', 'sentence_text', 'fine_amount', 'debtor_name')


class DebtorResource(resources.ModelResource):

    class Meta:
        import_id_fields = ['id']
        model = Debtor
        #fields = ('debtor_id', 'debtor_name', 'debtor_added_by')

class DebtAdmin(ImportExportModelAdmin):
    pass

class CommentAdmin(ImportExportModelAdmin):
    pass

class CompanyAdmin(ImportExportModelAdmin):
    pass


class CrimeAdmin(ImportExportModelAdmin):
    pass

class DebtorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = DebtorResource
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Debtor, DebtorAdmin)
admin.site.register(Debt, DebtAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Crime, CrimeAdmin)

