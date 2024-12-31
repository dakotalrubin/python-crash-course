def make_shirt(size='large', message='I love Python.'):
    """Print a sentence summarizing the shirt size and message to be printed."""
    print(f"Making you a size {size} shirt with the message:")
    print(f"\t'{message}'")

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Hi')