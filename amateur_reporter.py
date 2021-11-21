# import csv
from fpdf import FPDF
import time
# import pandas as pd
# from pandas import DataFrame
import os

timestr_file = time.strftime("%Y-%m-%d__%H-%M-%S")
timestr = time.strftime("%Y.%m.%d %H:%M:%S")

# *out,

# data = pd.read_csv(os.path.join('QCTerror_res', 'tables', 'overrepresented_sequences1.tsv'), sep="\t")
# df = DataFrame(data)
# df1 = df.astype(str)
# records = df1.to_records(index=False)
# longone = list(records)

# with open(os.path.join('QCTerror_res', 'tables', 'basic_statistics.tsv')) as f:
# reader = csv.DictReader(f, delimiter='\t')

# data1 = pd.read_csv(os.path.join('QCTerror_res', 'tables', 'basic_statistics.tsv'), sep="\t")
# df2 = DataFrame(reader)
# df2 = reader.astype(str)
# records = df2.to_records(index=False)
# stat = list(records)


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image(os.path.join("QCTerror_logo.png"), 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "QC report", 1, 0, "C")
        self.set_font("helvetica", "U", 7)
        self.cell(50)
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
# 0
# 1 Basic Statistics
# 2 Per base sequence quality
# 3 Per tile sequence quality
# 4 Per sequence quality scores
# 5 Per base sequence content
# 6 Per sequence GC content
# 7 Per base N content
# 8 Sequence Length Distribution
# 9 Sequence Duplication Levels
# 10 Overrepresented sequences
# 11 Adapter Content

# 1
# pdf.add_page()
# pdf.set_font("Times", size=7)
# line_height = pdf.font_size * 2.5
# col_width = pdf.epw / 4  # distribute content evenly
# for row in stat:
# for datum in row:
# pdf.multi_cell(col_width, line_height, datum, border=1, ln=3, max_line_height=pdf.font_size)
# pdf.ln(line_height)

# 2
pdf.add_page()
pdf.set_font("Courier", size=20)
pdf.image("./QCTerror_res/pictures/Per_base_quality.png", w=pdf.epw)
pdf.cell(0, 10, "Per base quality", 1, 1, align='C')

# 3
# pdf.add_page()
# pdf.set_font("Courier", size=12)
# pdf.image("./QCTerror_res/pictures/Per_Tile_Sequence_Quality.png", w=pdf.epw)
# pdf.cell(0, 10, "Per tile sequence quality", 0, 1)

# 4
# pdf.add_page()
# pdf.set_font("Courier", size=12)
# pdf.image("./QCTerror_res/pictures/Per_sequence_quality_scores.png", w=pdf.epw)
# pdf.cell(0, 10, "Per sequence quality scores", 0, 1)

# 5
pdf.add_page()
pdf.set_font("Courier", size=20)
pdf.image("./QCTerror_res/pictures/Per_base_sequence_content.png", w=pdf.epw)
pdf.cell(0, 10, "Per base sequence content", 1, 1, align='C')

# 6
pdf.add_page()
pdf.set_font("Courier", size=20)
pdf.image("./QCTerror_res/pictures/GC_content.png", w=pdf.epw)
pdf.cell(0, 10, "GC content", 1, 1, align='C')

# 7
# pdf.add_page()
# pdf.set_font("Courier", size=12)
# pdf.image("./QCTerror_res/pictures/Per_base_N_content.png", w=pdf.epw)
# pdf.cell(0, 10, "Per base N content", 0, 1)

# 8
pdf.add_page()
pdf.set_font("Courier", size=20)
pdf.image("./QCTerror_res/pictures/Sequence_length_distribution.png", w=pdf.epw)
pdf.cell(0, 10, "Sequence length distribution", 1, 1, align='C')

# 9
pdf.add_page()
pdf.set_font("Courier", size=20)
pdf.image("./QCTerror_res/pictures/duplication_level.png", w=pdf.epw)
pdf.cell(0, 10, "duplication level", 1, 1, align='C')

# 10
# pdf.add_page()
# pdf.set_font("Courier", size=7)
# line_height = pdf.font_size * 2.5
# col_width = pdf.epw / 4  # distribute content evenly
# for row in longone:
# for datum in row:
# pdf.cell(line_height, col_width, datum, border=1, ln=3)
# pdf.ln(line_height)

# *out,pdf.font_size max_line_height=1

pdf.output(os.path.join('QCTerror_res', 'reports', 'amateur_final_report_{}.pdf'.format(timestr_file)))
