from fpdf import FPDF
import time
import pandas as pd
from pandas import DataFrame

timestr_file = time.strftime("%Y-%m-%d__%H-%M-%S")
timestr = time.strftime("%Y.%m.%d %H:%M:%S")

data = pd.read_csv("./QCTerror_res/tables/overrepresented_sequences.tsv", sep="\t")
df = DataFrame(data)
df1 = df.astype(str)
records = df1.to_records(index=False)
result = list(records)

# 2
# Basic Statistics
# Per base sequence quality
# Per tile sequence quality
# Per sequence quality scores
# Per base sequence content
# Per sequence GC content
# Per base N content
# Sequence Length Distribution
# Sequence Duplication Levels
# Overrepresented sequences
# Adapter Content


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("./QCTerror_logo.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "QC report", 1, 0, "C")
        self.set_font("helvetica", "U", 7)
        self.cell(80)
        self.write(3, f'{timestr}')
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", 0, 0, "C")


# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()

# 1
# pdf.add_page()
# pdf.set_font("Times", size=12)
# pdf.image("./QCTerror_res/pictures/Per_base_quality.png", w=pdf.epw)
# pdf.cell(0, 10, f"Raw statistic for your fasta file ", 0, 1)

# 2
# pdf.add_page()
# pdf.set_font("Times", size=12)
# pdf.image("./QCTerror_res/pictures/duplication_level.png", w=pdf.epw)
# pdf.cell(0, 10, f"Raw statistic for your fasta file ", 0, 1)

# 3
# pdf.add_page()
# pdf.set_font("Times", size=12)
# pdf.image("./QCTerror_res/pictures/Per_base_sequence_content.png", w=pdf.epw)
# pdf.cell(0, 10, f"Raw statistic for your fasta file ", 0, 1)

# 4
# pdf.add_page()
# pdf.set_font("Times", size=12)
# pdf.image("./QCTerror_res/pictures/Sequence_length_distribution.png", w=pdf.epw)
# pdf.cell(0, 10, f"Raw statistic for your fasta file ", 0, 1)

# 0
pdf.add_page()
pdf.set_font("Times", size=7)
line_height = pdf.font_size * 2.5
col_width = pdf.epw / 2  # distribute content evenly
for row in result:
    for datum in row:
        pdf.multi_cell(col_width, line_height, datum, border=1, ln=3, max_line_height=pdf.font_size)
    pdf.ln(line_height)

pdf.output(f"QCTerror_res/reports/amateur_final_report_" + timestr_file + ".pdf")
