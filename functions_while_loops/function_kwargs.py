def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


def create_profile(username, email, **kwargs):
    print(f"--- Profile for {username} ---")
    print(f"Email: {email}")

    for key, value in kwargs.items():
        print(f"{key.title().replace('_', ' ')}: {value}")
    print()


create_profile("johndoe", "john@email.com")

create_profile(
    "baker",
    "baker@email.com",
    location="Paris",
    favorite_food="Croissants"
)

create_profile(
    "gamer",
    "gg@email.com",
    age=24,
    status="Active",
    favorite_game="Elden Ring"
)