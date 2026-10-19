"""Sample app for the secret-scan demo. Contains no secrets."""
import os


def get_greeting(name: str) -> str:
    return f"Hello, {name}! Secret scanning demo."


def main() -> None:
    name = os.environ.get("USER_NAME", "world")
    print(get_greeting(name))


if __name__ == "__main__":
    main()
