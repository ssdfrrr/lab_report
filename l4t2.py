from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


records = list(SeqIO.parse("combined_records.gb", "genbank"))



def translate_cds(record):
    translations = []
    for feature in record.features:
        if feature.type == "CDS":

            seq = feature.extract(record.seq)
            protein = seq.translate()


            location = str(feature.location)


            protein_record = SeqRecord(
                protein,
                id=record.id,
                description=f"{record.description}\nCoding sequence location = {location}"
            )
            translations.append(protein_record)
    return translations



all_translations = []
for record in records:
    all_translations.extend(translate_cds(record))


for translation in all_translations:
    print(f"\n{translation.id}: {translation.description.split('\n')[0]}")
    print(f"Coding sequence location = {translation.description.split('\n')[1]}")
    print("Translation =")
    print(translation.seq)