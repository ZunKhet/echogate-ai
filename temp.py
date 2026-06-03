from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6JtMZtkiJVMdhPk9Q7zdyyfYZFwdFmdvmbGrLl0m63mOQ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello from Gemini."
)

print(response.text)
