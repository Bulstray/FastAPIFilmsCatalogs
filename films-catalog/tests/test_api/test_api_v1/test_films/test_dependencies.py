from api.api_v1.films.dependencies import UNSAFE_METHODS


class TestUnsafeMethods:
    def test_unsafe_methods_doesnt_contain_safe_methods(self) -> None:
        safe_methods = {
            "GET",
            "HEAD",
            "OPTIONS",
        }

        assert not UNSAFE_METHODS & safe_methods

    def test_all_methods_are_upper(self) -> None:
        assert all(method.isupper() for method in UNSAFE_METHODS)
