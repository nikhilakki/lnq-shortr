from nanoid import generate


def generate_url_hash(size: int = 7):
    return generate(size=size)
