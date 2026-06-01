from utils.audio_processor import process_input
from src.transcriber import transcribe_all
source = "https://www.youtube.com/watch?v=UEm0mHeXdxk&t=29s"


chunk = process_input(source)
transcript = transcribe_all(chunk)

print(transcript)