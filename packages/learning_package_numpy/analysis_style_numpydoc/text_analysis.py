def count_words(filepath, words_list):
    """

    [According documentation style 'numpydoc' at MODULE level]

    Terminal command | pyment -w -o numpydoc inches_to_feet.py
    Flags
    -w          | overwrite
    -o <style>  | styleput in NumPy documentation style

    Parameters
    ----------
    filepath : <type>
        <indented description>

    words_list : <type>
        <indented description>

    Returns
    -------
    <type>


    [According documentation style 'numpydoc' at MODULE level]

    """

    # Open the text file
    with open(filepath) as file:
        text = file.read()

    n = 0
    for word in text.split():
        # Count the number of times the words in the list appear
        if word.lower() in ['cat', 'cats']:
            n += 1

    print('Lewis Carroll uses the word "cat" {} times'.format(n))

    return n
