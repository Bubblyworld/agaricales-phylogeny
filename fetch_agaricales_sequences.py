from Bio import Entrez, SeqIO

# Replace 'your.email@example.com' with your actual email address
Entrez.email = "your.email@example.com"
query = "Agaricales[Orgn] AND (ITS1 OR ITS2)"

# Fetching sequence IDs
search_handle = Entrez.esearch(db="nucleotide", term=query, retmax=500)
search_results = Entrez.read(search_handle)
search_handle.close()
ids = search_results['IdList']

# Fetching sequences
fetch_handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta", retmode="text")
data = fetch_handle.read()
fetch_handle.close()

# Save the sequences to a file
with open("agaricales_sequences.fasta", "w") as file:
    file.write(data)
