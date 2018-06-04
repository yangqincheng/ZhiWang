from urllib.parse import unquote
url="""
http://kns.cnki.net/kns/brief/vericode.aspx?rurl=%2fkns%2fbrief%2fbrief.aspx%3fcurpage%3d17%26RecordsPerPage%3d20%26QueryID%3d12%26ID%3
d%26turnpage%3d1%26tpagemode%3dL%26dbPrefix%3dSCDB%26Fields%3d%26DisplayMode%3dlistmode%26PageName%3dASP.brief_result_aspx
"""
print(unquote(url))