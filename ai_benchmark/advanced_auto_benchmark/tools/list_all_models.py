try:
    import google.generativeai as genai
except ImportError:
    genai = None
for m in genai.list_models():
    print(m.name.split("/")[-1])