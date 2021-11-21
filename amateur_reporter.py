from fpdf import FPDF
from datetime import datetime, timedelta
import os

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
        self.image("./QC-Terror.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "QC report", 1, 0, "C")
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
pdf.add_page()
pdf.set_font("Times", size=12)
pdf.image("./pictures/Per_base_quality.png", w=pdf.epw)
pdf.cell(0, 10, f"Raw statistic for your fasta file {i}", 0, 1)

# 2
pdf.add_page()
pdf.set_font("Times", size=12)
pdf.image("./pictures/duplication_level.png", w=pdf.epw)
pdf.cell(0, 10, f"Raw statistic for your fasta file {i}", 0, 1)

# 3
pdf.add_page()
pdf.set_font("Times", size=12)
pdf.image("./pictures/duplication_level.png", w=pdf.epw)
pdf.cell(0, 10, f"Raw statistic for your fasta file {i}", 0, 1)

pdf.output("reports/amateur_final_report.pdf")
