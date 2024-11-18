
from groq import Groq
from pypdf import PdfReader
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


client = Groq(api_key="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")


reader = PdfReader('C:/Users/varsh/Downloads/example.pdf')
full_resume = ""
for page in reader.pages:
	full_resume +=  "\n" + page.extract_text()

completion = client.chat.completions.create(
	model="llama3-70b-8192",
	messages=[
		{
			"role": "user",
			"content": "Given the resume content give make optimisations and give result in text format in ``` quotes " + full_resume
		}
	],
	temperature=1,
	max_tokens=1024,
	top_p=1,
	stop=None,
)

result = completion.choices[0].message.content
print(str(result))