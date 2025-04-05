import pandas as pd
from fpdf import FPDF

df = pd.read_csv("data.csv")

summary = df.groupby('Subject')['Marks'].agg(['mean', 'max', 'min']).reset_index()

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Student Performance Report', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def chapter_body(self, data):
        self.set_font('Arial', '', 11)
        for index, row in data.iterrows():
            self.cell(0, 10, f"{row['Subject']}: Avg={row['mean']:.2f}, Max={row['max']}, Min={row['min']}", ln=True)
        self.ln()

pdf = PDF()
pdf.add_page()
pdf.chapter_title("Marks Summary by Subject")
pdf.chapter_body(summary)
pdf.output("student_report.pdf")

print("✅ PDF report generated: student_report.pdf")
