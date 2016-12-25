# -*- coding: utf-8 -*-
import xlwt
from datetime import datetime

from django.http import HttpResponse
from django.utils.dateparse import parse_date

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

import reports.styles as styles

class Report(ViewSet):

    file_name = 'base_report'
    sheet_name = 'base_sheet_name'
    table_headers = []

    def initial(self, request, *args, **kwargs):
        self.request = request
        self.title = self.get_title(**kwargs)
        self.response = HttpResponse(content_type='application/ms-excel')
        disposition = 'attachment; filename={file_name}.xls'.format(
            file_name=self.file_name)
        self.response['Content-Disposition'] = disposition
        self.wb = xlwt.Workbook(encoding='utf-8')
        self.ws = self.wb.add_sheet(self.sheet_name)
        self.ws.write_merge(0, 0, 0, len(self.table_headers) - 1, self.title)
        return super(Report, self).initial(request, *args, **kwargs)

    def get_title(self, **kwargs):
        return u'String need to replace by report.'

    def get_fdate(self):
        fdate = self.request.query_params.get('fdate')
        if fdate:
            return datetime.strptime(fdate, '%d.%m.%Y')
        else:
            return datetime.now()

    def get_tdate(self):
        fdate = self.request.query_params.get('tdate')
        if fdate:
            return datetime.strptime(fdate, '%d.%m.%Y')
        else:
            return datetime.now()

    def get_data(self):
        raise ('Need update by child')

    def write_data(self):
        raise ('Need update by child')

    def write_bottom(self):
        raise ('Need update by child')

    def write_heads(self):
        headers = self.table_headers
        self.ws.row(self.row_num).height_mismatch = True
        self.ws.row(self.row_num).height = 35*20
        for col_num in xrange(len(headers)):
            self.ws.write(
                self.row_num, col_num, headers[col_num][0], styles.styleth)
            # set column width
            self.ws.col(col_num).width = headers[col_num][1]

    def write_sheet(self):
        self.row_num = 2
        self.write_heads()
        self.row_num += 1
        self.write_data()
        self.row_num += 2
        self.write_bottom()

    def list(self, request, **kwargs):
        """
        Return a list of all users.
        """
        self.write_sheet()
        self.wb.save(self.response)
        return self.response
