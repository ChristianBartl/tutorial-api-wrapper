from tmdbwrapper import TV

def test_tv_info():
    """Tests an API call to get a TV show's info"""
    pass

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID should be in the response"
