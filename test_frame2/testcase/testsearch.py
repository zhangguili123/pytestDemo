from test_frame.app import App


def test_search():
    app=App()
    result=app.start().gotoMain().goto_market().goto_search().search()
    assert   result
def test_mine():
    app = App()
    result = app.start().gotoMain().goto_me()
    #assert result