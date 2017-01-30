import xlwt

# top prefix head
styleph = xlwt.XFStyle()
alignment = xlwt.Alignment()
alignment.wrap = 1
alignment.horz = xlwt.Alignment.HORZ_RIGHT
alignment.vert = xlwt.Alignment.VERT_JUSTIFIED
styleph.alignment = alignment
font = xlwt.Font()
font.height = 6*20
styleph.font = font
# reports HEAD
styleh = xlwt.XFStyle()
styleh.font.bold = True
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
styleh.alignment = alignment
# simple borders for table usually use
borders = xlwt.Borders()
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
# One side borders
borders_l = xlwt.Borders()
borders_l.left = xlwt.Borders.THIN
borders_r = xlwt.Borders()
borders_r.right = xlwt.Borders.THIN
borders_t = xlwt.Borders()
borders_t.top = xlwt.Borders.THIN
borders_b = xlwt.Borders()
borders_b.bottom = xlwt.Borders.THIN
# One side Medium borders
borders_lm = xlwt.Borders()
borders_lm.left = xlwt.Borders.MEDIUM
borders_rm = xlwt.Borders()
borders_rm.right = xlwt.Borders.MEDIUM
borders_tm = xlwt.Borders()
borders_tm.top = xlwt.Borders.MEDIUM
borders_bm = xlwt.Borders()
borders_bm.bottom = xlwt.Borders.MEDIUM
borders_cm = xlwt.Borders()
borders_cm.right = xlwt.Borders.MEDIUM
borders_cm.left = xlwt.Borders.MEDIUM
borders_cmb = xlwt.Borders()
borders_cmb.right = xlwt.Borders.MEDIUM
borders_cmb.left = xlwt.Borders.MEDIUM
borders_cmb.bottom = xlwt.Borders.MEDIUM
# Table head
styleth = xlwt.XFStyle()
styleth.font.bold = True
styleth.borders = borders
styleth.alignment = alignment
# Table head date
stylethd = xlwt.XFStyle()
stylethd.font.bold = True
stylethd.borders = borders
stylethd.num_format_str = "DD.MM.YYYY"
# Table head finance  
stylethf = xlwt.XFStyle()
stylethf.font.bold = True
stylethf.borders = borders
stylethf.num_format_str = "# ##0.00"

# All data
style = xlwt.XFStyle()
style.borders = borders
# Red back ground data 
style_red = xlwt.XFStyle()
style_red.font.bold = True
style_red.font.colour_index = xlwt.Style.colour_map['white']
style_red.borders = borders
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = xlwt.Style.colour_map['red']
style_red.pattern = pattern

# All data date
styled = xlwt.XFStyle()
styled.borders = borders
styled.num_format_str = "DD.MM.YYYY"
# All data date time
styledt = xlwt.XFStyle()
styledt.borders = borders
styledt.num_format_str = "DD.MM.YYYY HH:MM"
# All data time
stylet = xlwt.XFStyle()
stylet.borders = borders
stylet.num_format_str = "HH:MM"
# All data finance  
stylef = xlwt.XFStyle()
stylef.borders = borders
stylef.num_format_str = "# ##0.00"