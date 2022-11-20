def read_book(file_reader):
    """ (_io.TextIOWrapper) -> int

    The function is to read the digital book "the boy who lived.txt", and then
    counts how many potter or Potter occurs in the book. Actually, it can even
    detect poTTer or PoTTeR.

    The return value should be the amount value after this counting.
    """
    ### You would see the comments like this to illustrate the topic.
    ## You would see the comments like this to explain the details.
    # You would see the comments like this to give you a short hint.

    # ==== You can only edit your codes when you see this pattern. ==== #

    # ==================== Start your code HERE ======================= #
    # ==================== End your code HERE ========================= #

    ### The function contains three essential parts:
    ### 1. Initialize necessary variables
    ### 2. Read and count with the loop workflow
    ### 3. Wrap things up and return the result.

    ### 1. Initialize necessary variables
    count = 0
    stringToBeCount = "harry"
    stillReading = True

    ### 2. Read and count with the loop workflow
    while stillReading:


        # ==================== Start your code HERE ======================= #
        # Hint: line should be read from the _io.TextIOWrapper
        line = None
        # ==================== End your code HERE ========================= #


        ## This block help us to prevent continue read when the file is finished.
        if not line:
            stillReading = False
            continue


        # ==================== Start your code HERE ======================= #
        # Hint: words is a list that contains words from the string line
        words = []
        # ==================== End your code HERE ========================= #
        

        for word in words:
            if word.lower().strip().startswith(stringToBeCount):
                count += 1

    ### 3. Wrap things up and return the result.
    # ==================== Start your code HERE ======================= #
    # Hint: what integer should you return from the documentation? think about
    # it and answer will be straight forward.
    return 0
    # ==================== End your code HERE ========================= #
