phrase = '''    Borsec este o marcă de apă minerală îmbuteliată creată
de către colonelul austriac Valentin Gunther și vărul său geolog
Anton Zimmethausen în 1806.[1] În momentul de față este unul dintre
cele mai puternice branduri din România.'''
print(phrase[:len(phrase) // 2].translate(str.maketrans(" ", " ")).upper().strm     ip() + phrase[len(phrase) // 2::-1].capitalize().translate(str.maketrans("", "", ".,!?")))
