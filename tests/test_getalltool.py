from tools import get_alltool

def test_get_alltool_detail():

    URL = "https://simple-tool-rental-api.glitch.me/tools"
    
    result=get_alltool.get_all_tool_detail(URL)
        
    assert result == 200