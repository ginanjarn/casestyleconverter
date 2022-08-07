import converter


if __name__ == "__main__":
    assert "helloWorld" == converter.to_camel("hello_world")
    assert "HelloWorld" == converter.to_upper_camel("hello_world")
    assert "hello_world" == converter.to_snake("HelloWorld")
    assert "HELLO_WORLD" == converter.to_upper_snake("helloWorld")

    assert "__main__" == converter.to_camel("__main__")
    assert "__Main__" == converter.to_upper_camel("__main__")
    assert "__main__" == converter.to_snake("__main__")
    assert "__MAIN__" == converter.to_upper_snake("__main__")

    assert "__time__default__" == converter.to_camel("__time__default__")
    assert "__Time__Default__" == converter.to_upper_camel("__time__default__")
    assert "__time__default__" == converter.to_snake("__time__default__")
    assert "__TIME__DEFAULT__" == converter.to_upper_snake("__time__default__")
