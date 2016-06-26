#coding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re

html = '''

<div class='divInvalid' style='font-size:14px;line-height:30px;' onclick="SelectTime('1；2','1978599；1978600')" id='divTime1；2'><span id='span1；2'>08:00-09:00</span><input type='checkbox' id='chk1；2' value='1978599；1978600' name='chkTime' style='display:none' />
</div><div class='divInvalid' style='font-size:14px;line-height:30px;' onclick="SelectTime('3；4','1978601；1978602')" id='divTime3；4'><span id='span3；4'>09:00-10:00</span><input type='checkbox' id='chk3；4' value='1978601；1978602' name='chkTime' style='display:none' />
</div><div class='divInvalid' style='font-size:14px;line-height:30px;' onclick="SelectTime('5；6','1978603；1978604')" id='divTime5；6'><span id='span5；6'>10:00-11:00</span><input type='checkbox' id='chk5；6' value='1978603；1978604' name='chkTime' style='display:none' />
</div><div class='divInvalid' style='font-size:14px;line-height:30px;' onclick="SelectTime('7；8','1978605；1978606')" id='divTime7；8'><span id='span7；8'>11:00-12:00</span><input type='checkbox' id='chk7；8' value='1978605；1978606' name='chkTime' style='display:none' />
</div><div class='divInvalid' style='font-size:14px;line-height:30px;' onclick="SelectTime('9；10','1978611；1978612')" id='divTime9；10'><span id='span9；10'>14:00-15:00</span><input type='checkbox' id='chk9；10' value='1978611；1978612' name='chkTime' style='display:none' />
</div><div class='divInvalid' style='font-size:14px;line-height:30px;' onclick="SelectTime('11；12','1978613；1978614')" id='divTime11；12'><span id='span11；12'>15:00-16:00</span><input type='checkbox' id='chk11；12' value='1978613；1978614' name='chkTime' style='display:none' />
</div><div class='divInvalid' style='font-size:14px;line-height:30px;' onclick="SelectTime('13；14','1978615；1978616')" id='divTime13；14'><span id='span13；14'>16:00-17:00</span><input type='checkbox' id='chk13；14' value='1978615；1978616' name='chkTime' style='display:none' />
</div>

'''
results = re.search(r'SelectTime\(.*\)', html)

print re.sub("'", "", results.group(0).split(',')[1].split(')')[0])