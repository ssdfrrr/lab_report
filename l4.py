from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
from Bio.Seq import UndefinedSequenceError


def calculate_gc_content(record):
    """Вычисляет GC-состав с обработкой ошибок"""
    try:
        if not hasattr(record, 'seq') or record.seq is None:
            return 0.0
        return gc_fraction(record.seq) * 100
    except UndefinedSequenceError:
        return 0.0


def process_genbank_file(input_file, output_file):
    """Обрабатывает GenBank файл и сохраняет результаты"""
    try:
        # Чтение и фильтрация записей
        records = list(SeqIO.parse(input_file, "genbank"))
        valid_records = [r for r in records if hasattr(r, 'seq') and r.seq is not None]

        if not valid_records:
            print("Нет валидных последовательностей для анализа!")
            return

        # Сортировка и сохранение
        sorted_records = sorted(valid_records, key=calculate_gc_content)
        with open(output_file, "w") as f:
            for record in sorted_records:
                gc = calculate_gc_content(record)
                f.write(f">{record.id}|GC={gc:.2f}%\n{record.seq}\n\n")

        print(f"Готово! Обработано {len(sorted_records)} последовательностей.")

    except Exception as e:
        print(f"Ошибка: {e}")


# Пример использования
process_genbank_file("C:/Users/lalin/Downloads/sequence.gb", "output.txt")
