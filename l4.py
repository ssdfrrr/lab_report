from Bio import Entrez, SeqIO
import os


Entrez.email = " "



def download_genbank_records(species, num_records=5):
    handle = Entrez.esearch(db="nucleotide", term=f"{species}[Organism] AND complete cds", retmax=num_records)
    record = Entrez.read(handle)
    handle.close()

    if not record["IdList"]:
        print(f"Не найдено записей для вида: {species}")
        return []


    handle = Entrez.efetch(db="nucleotide", id=record["IdList"], rettype="gb", retmode="text")
    records = list(SeqIO.parse(handle, "genbank"))
    handle.close()

    return records



betula_records = download_genbank_records("Betula platyphylla")
bacteria_records = download_genbank_records("Candidatus Versatilivorator vitaminiformans")


all_records = betula_records + bacteria_records


output_file = "combined_records.gb"
with open(output_file, "w") as f:
    SeqIO.write(all_records, f, "genbank")

print(f"Создан файл {output_file} с {len(all_records)} записями")