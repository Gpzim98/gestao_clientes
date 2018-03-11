from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.html import strip_tags
from django.contrib import messages
import csv


def export_as_xls(modeladmin, request, queryset):
    """
    Generic xls export admin action.
    """
    fields = []

    # PUT THE LIST OF FIELD NAMES YOU DON'T WANT TO EXPORT
    exclude_fields = []

    # foreign key related fields
    extras = ['']

    if not request.user.is_staff:
        raise PermissionDenied

    for f in modeladmin.list_display:
        if f not in exclude_fields:
            fields.append(f)
    fields.extend(extras)

    opts = modeladmin.model._meta

    wb = Workbook()
    ws0 = wb.add_sheet('0')
    col = 0
    field_names = []

    # write header row
    for field in fields:
        ws0.write(0, col, field)
        field_names.append(field)
        col = col + 1
    row = 1

    # Write data rows
    for obj in queryset:
        col = 0
        for field in field_names:
            if field in extras:
                try:
                    val = [eval('obj.' + field)]  # eval sucks but easiest way to deal
                except:
                    val = ['None']
            else:
                try:
                    val = lookup_field(field, obj, modeladmin)
                except:
                    val = ['None']
            ws0.write(row, col, str(strip_tags(val[-1])).strip())
            col = col + 1

        row = row + 1

    wb.save('/tmp/output.xls')
    response = HttpResponse(open('/tmp/output.xls', 'r').read(),
                            mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s.xls' % unicode(opts).replace('.', '_')
    return response


export_as_xls.short_description = "Export selected to XLS"