def create_codon_dict(file_path):
    codon2aa = {}
    # Use the provided file_path argument instead of hardcoding
    file_text = open(file_path,"r")
    rows = file_text.readlines()
    file_text.close()

    for r in rows:
      parts = r.strip().split('\t')
      if len(parts) >= 3:
       key = parts[0]
       value = parts[2]
       codon2aa[key] = value
    # The function needs to return the dictionary, not just print it.
    return codon2aa
